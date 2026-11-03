#!/usr/bin/env python3
"""
SEO + GEO audit of one page, ending in a prioritized fix list (free, no API).

Usage:
    python3 scripts/seo_audit.py "https://example.co.il"
    python3 scripts/seo_audit.py "https://example.co.il/page" --json
    python3 scripts/seo_audit.py "https://example.co.il" --no-bot-fetch

Checks, in priority order:
  P0 (blocks everything): page status, noindex / nosnippet / max-snippet:0
     (meta or X-Robots-Tag), robots.txt rules per crawler for the audited
     path, robots.txt answering 5xx, search-bot requests refused at the
     server/CDN.
  P1 (costs rankings or citations): canonical, title / description / H1,
     viewport, hreflang self-reference, JSON-LD that does not parse, redirect
     chains, sitemap discovery, little text in the raw HTML, a bot getting a
     page without the page text (challenge page).
  P2 (polish or no-value markup): <html lang> and dir (accessibility, not a
     Google language signal), search bots allowed only by a wildcard,
     FAQPage / HowTo / Speakable markup (no Google rich result), Open Graph,
     slow server response.

It audits ONE URL and does not crawl. Bot fetches send each crawler's
published user-agent string; a CDN that verifies bots by IP can still treat
the real crawler differently, so a 200 here is not proof of access and a
refusal here is a strong lead, not a verdict. Exit codes: 0 audit ran
(findings may exist), 1 the page itself could not be fetched, 2 this machine
could not run the audit (e.g. Python without root certificates).
"""
import argparse
import html as htmllib
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 SEO-Audit/2.0"
)

# Published example user-agent strings (the vendors note version numbers may
# change). Anthropic publishes the token but no full string, so the token is
# sent in a minimal compatible form.
BOT_UAS = {
    "Googlebot": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "OAI-SearchBot": (
        "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; "
        "OAI-SearchBot/1.4; +https://openai.com/searchbot"
    ),
    "PerplexityBot": "Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)",
    "Claude-SearchBot": "Mozilla/5.0 (compatible; Claude-SearchBot)",
}

# Crawlers whose robots.txt rules are evaluated for the audited path.
CLASSIC_BOTS = ["Googlebot", "Bingbot"]
SEARCH_BOTS = ["OAI-SearchBot", "Claude-SearchBot", "PerplexityBot"]
TRAINING_TOKENS = ["GPTBot", "ClaudeBot", "Google-Extended", "Applebot-Extended", "CCBot"]
LIVE_FETCHERS = ["ChatGPT-User", "Claude-User", "Perplexity-User"]

NO_GOOGLE_RICH_RESULT = {
    "FAQPage": "Google stopped showing FAQ rich results on 7 May 2026. Valid "
               "schema.org, no Google rich result; keep only if other consumers use it.",
    "HowTo": "Google removed HowTo rich results in September 2023. No Google rich result.",
    "SpeakableSpecification": "Google's speakable is a beta for English-language news "
                              "publishers on Google Assistant in the US. No effect for a "
                              "Hebrew business page.",
}

HEBREW_RE = re.compile(r"[֐-׿]")


class _Redirects(urllib.request.HTTPRedirectHandler):
    def __init__(self):
        self.chain = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.chain.append((code, newurl))
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch(url: str, ua: str = BROWSER_UA, timeout: int = 30) -> dict:
    """GET a URL. Returns status, final_url, headers, body, seconds, chain, error."""
    handler = _Redirects()
    opener = urllib.request.build_opener(handler)
    req = urllib.request.Request(url, headers={
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "he-IL,he;q=0.9,en;q=0.8",
    })
    out = {"status": None, "final_url": url, "headers": {}, "body": "",
           "seconds": None, "chain": handler.chain, "error": None, "local_tls": False}
    start = time.time()
    try:
        with opener.open(req, timeout=timeout) as resp:
            out["status"] = resp.status
            out["final_url"] = resp.geturl()
            out["headers"] = {k.lower(): v for k, v in resp.headers.items()}
            out["body"] = resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as e:
        out["status"] = e.code
        out["headers"] = {k.lower(): v for k, v in (e.headers or {}).items()}
        out["error"] = f"HTTP {e.code}"
    except urllib.error.URLError as e:
        # urllib wraps TLS failures inside URLError.
        if isinstance(getattr(e, "reason", None), ssl.SSLError):
            out["error"] = f"TLS failure: {e.reason}"
            # "unable to get local issuer certificate" is almost always THIS
            # machine's Python lacking root certificates, not the site's fault.
            out["local_tls"] = "local issuer" in str(e.reason)
        else:
            out["error"] = f"network error: {e.reason}"
    except Exception as e:  # noqa: BLE001 - report any fetch failure as data
        out["error"] = f"{type(e).__name__}: {e}"
    out["seconds"] = round(time.time() - start, 2)
    return out


# ---------------------------------------------------------------- robots.txt

def parse_robots(content: str) -> tuple:
    """Return ({agent_lower: [(directive, pattern)]}, [sitemap urls]).

    Consecutive User-agent lines share the group that follows them, and
    repeated groups for the same agent are combined (RFC 9309).
    """
    groups, sitemaps, current, expecting_agents = {}, [], [], False
    for raw in content.splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        field, _, value = line.partition(":")
        field, value = field.strip().lower(), value.strip()
        if field == "sitemap":
            sitemaps.append(value)
        elif field == "user-agent":
            if not expecting_agents:
                current, expecting_agents = [], True
            current.append(value.lower())
            groups.setdefault(value.lower(), [])
        elif field in ("allow", "disallow"):
            expecting_agents = False
            for agent in current:
                groups[agent].append((field, value))
    return groups, sitemaps


def _rule_matches(pattern: str, path: str) -> bool:
    """RFC 9309 matching: '*' is any sequence, a trailing '$' anchors the end."""
    anchored = pattern.endswith("$")
    body = pattern[:-1] if anchored else pattern
    rx = "".join(".*" if ch == "*" else re.escape(ch) for ch in body)
    return re.match(rx + ("$" if anchored else ""), path) is not None


def is_allowed(groups: dict, agent: str, path: str = "/") -> tuple:
    """(allowed, matched_group) for `agent` fetching `path`.

    The crawler's own group wins; only without one does it fall back to '*'.
    The longest matching rule wins; Allow wins a tie.
    """
    key = agent.lower()
    matched = key if key in groups else ("*" if "*" in groups else None)
    if matched is None:
        return True, "none"
    best_len, best_allow = -1, True
    for directive, pattern in groups[matched]:
        if pattern == "":
            continue  # an empty Disallow allows everything
        if _rule_matches(pattern, path):
            length = len(pattern)
            if length > best_len or (length == best_len and directive == "allow"):
                best_len, best_allow = length, directive == "allow"
    return best_allow, matched


# ---------------------------------------------------------------- HTML checks

def _attr(tag: str, name: str):
    m = re.search(rf'\b{name}\s*=\s*["\']([^"\']*)["\']', tag, re.I)
    return htmllib.unescape(m.group(1)).strip() if m else None


def _tags(html: str, tag: str) -> list:
    return re.findall(rf"<{tag}\b[^>]*>", html, re.I)


def _text(fragment: str) -> str:
    return re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def visible_text(html: str) -> str:
    stripped = re.sub(r"<(script|style|noscript|template)\b.*?</\1>", " ", html, flags=re.I | re.S)
    return _text(stripped)


def jsonld_types(html: str) -> tuple:
    """Return (types found, number of blocks that fail to parse)."""
    blocks = re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.I | re.S)
    types, bad = [], 0

    def walk(node):
        if isinstance(node, dict):
            t = node.get("@type")
            for v in (t if isinstance(t, list) else [t]):
                if isinstance(v, str):
                    types.append(v)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    for block in blocks:
        try:
            walk(json.loads(block.strip()))
        except ValueError:
            bad += 1
    return types, bad, len(blocks)


def audit(url: str, bot_fetch: bool = True) -> dict:
    findings = []

    def add(priority, area, finding, fix):
        findings.append({"priority": priority, "area": area, "finding": finding, "fix": fix})

    page = fetch(url)
    report = {"url": url, "final_url": page["final_url"], "status": page["status"],
              "server_seconds": page["seconds"], "redirects": page["chain"]}
    if page["local_tls"]:
        report["tool_error"] = (
            f"{page['error']}. The site was NOT audited. Usual cause: this Python's "
            "certificate store is missing or older than the site's root CA. Run your "
            "Python installation's 'Install Certificates' step (or pip install certifi "
            "and set SSL_CERT_FILE to its bundle), then re-run. If a current store still "
            "fails, the site may not be sending its intermediate certificate; check it in "
            "an SSL checker before reporting that to the owner.")
        report["findings"] = []
        return report
    if page["status"] in (401, 403, 429, 503):
        # Many WAFs refuse any non-browser client regardless of user agent
        # (gov.il does). That says nothing about what a real visitor or a
        # verified crawler gets, so it is NOT reported as a site finding.
        outage = (" A 503 can also be a real outage: retry, and check in a browser "
                  "and in Search Console." if page["status"] == 503 else "")
        report["error"] = (
            f"HTTP {page['status']} to this script. If the page opens normally in a "
            "browser, the site's firewall is refusing scripted clients and the automated "
            "checks could not run. Audit by hand (view-source, Rich Results Test, "
            "URL Inspection in Search Console) instead of treating this as downtime."
            + outage)
        report["findings"] = findings
        return report
    if page["status"] != 200 or not page["body"]:
        report["error"] = page["error"] or f"HTTP {page['status']}"
        add("P0", "access", f"Page did not load ({report['error']}).",
            "Fix the server response before anything else; nothing below matters until it does.")
        report["findings"] = findings
        return report

    html, headers = page["body"], page["headers"]
    final = page["final_url"]
    path = urllib.parse.urlparse(final).path or "/"
    if urllib.parse.urlparse(final).query:
        path += "?" + urllib.parse.urlparse(final).query

    # Redirects
    if len(page["chain"]) > 1:
        add("P1", "access", f"{len(page['chain'])} redirect hops before the page.",
            "Link and canonicalize to the final URL so crawlers reach it in one hop.")

    # Indexability
    robots_meta = " ".join((_attr(t, "content") or "") for t in _tags(html, "meta")
                           if (_attr(t, "name") or "").lower() in ("robots", "googlebot"))
    x_robots = headers.get("x-robots-tag", "")
    directives = robots_meta + " " + x_robots
    if re.search(r"\b(noindex|none)\b", directives, re.I):
        add("P0", "indexing", "Page carries noindex (meta robots or X-Robots-Tag).",
            "Remove noindex if this page should appear in Google or AI search.")
    if re.search(r"\bnosnippet\b|max-snippet\s*:\s*0\b", directives, re.I):
        add("P0", "indexing", "Page carries nosnippet or max-snippet:0 (meta robots or X-Robots-Tag).",
            "If unintended, remove it: Google names these as controls that limit what Search, "
            "including its AI features, shows from the page.")
    canonical = next((_attr(t, "href") for t in _tags(html, "link")
                      if (_attr(t, "rel") or "").lower() == "canonical"), None)
    report["canonical"] = canonical
    if canonical:
        canon_abs = urllib.parse.urljoin(final, canonical)
        if canon_abs.rstrip("/") != final.rstrip("/"):
            add("P1", "indexing", f"Canonical points elsewhere: {canon_abs}",
                "Confirm this is intended; Google may index the canonical target instead of this URL.")
    else:
        add("P2", "indexing", "No rel=canonical.",
            "Add a self-referencing canonical on indexable pages.")

    # Language and direction
    html_tag = (_tags(html, "html") or [""])[0]
    lang, direction = _attr(html_tag, "lang"), _attr(html_tag, "dir")
    text = visible_text(html)
    hebrew_share = len(HEBREW_RE.findall(text)) / max(1, len(re.findall(r"\w", text)))
    report.update({"html_lang": lang, "html_dir": direction,
                   "visible_text_chars": len(text), "hebrew_share": round(hebrew_share, 2)})
    if hebrew_share > 0.3:
        why = (" (rendering and screen readers; Google says it does not use lang to "
               "detect a page's language, so this is not a ranking fix)")
        if not (lang or "").lower().startswith("he"):
            add("P2", "hebrew", f"Mostly Hebrew text but <html lang=\"{lang}\">.",
                "Set lang=\"he\" on Hebrew pages" + why + ".")
        if (direction or "").lower() != "rtl":
            add("P2", "hebrew", "Mostly Hebrew text but no dir=\"rtl\" on <html>.",
                "Set dir=\"rtl\" on the html element of Hebrew pages" + why + ".")
    if not any((_attr(t, "name") or "").lower() == "viewport" for t in _tags(html, "meta")):
        add("P1", "mobile", "No viewport meta tag.", "Add <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">.")

    # Raw HTML text (what a non-rendering crawler can read)
    if len(text) < 500:
        add("P1", "rendering",
            f"Only {len(text)} characters of visible text in the raw HTML.",
            "Compare with the rendered page (URL Inspection > View crawled page). If the text "
            "is injected by JavaScript, server-render it; crawlers that do not execute "
            "JavaScript see only this raw HTML. A genuinely short page is fine.")

    # Title, description, H1, OG
    tm = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    title = _text(tm.group(1)) if tm else None
    desc = next((_attr(t, "content") for t in _tags(html, "meta")
                 if (_attr(t, "name") or "").lower() == "description"), None)
    h1m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    h1 = _text(h1m.group(1))[:120] if h1m else None
    report.update({"title": title, "description": desc, "h1": h1})
    if not title:
        add("P1", "on-page", "Missing <title>.", "Write a unique, descriptive title.")
    if not desc:
        add("P1", "on-page", "Missing meta description.", "Write a meta description that answers the query.")
    if not h1:
        add("P1", "on-page", "No <h1> in the raw HTML.", "Add one H1 that states the page topic.")
    if not any((_attr(t, "property") or "").lower() == "og:title" for t in _tags(html, "meta")):
        add("P2", "social", "No Open Graph tags.", "Add og:title, og:description and og:image.")

    # hreflang
    alternates = [(_attr(t, "hreflang"), urllib.parse.urljoin(final, _attr(t, "href") or ""))
                  for t in _tags(html, "link")
                  if (_attr(t, "rel") or "").lower() == "alternate" and _attr(t, "hreflang")]
    report["hreflang"] = alternates
    if alternates:
        if not any(href.rstrip("/") == final.rstrip("/") for _, href in alternates):
            add("P1", "hreflang", "hreflang set does not include this page itself.",
                "Each language version must list itself as well as every other version.")
        add("P2", "hreflang", "hreflang present; reciprocity was not checked (single-page audit).",
            "Open each alternate and confirm it links back; one-way pairs are ignored.")

    # Structured data
    types, bad, nblocks = jsonld_types(html)
    report["jsonld_types"] = sorted(set(types))
    if bad:
        add("P1", "schema", f"{bad} of {nblocks} JSON-LD block(s) do not parse.",
            "Fix the JSON syntax; an unparseable block is ignored entirely.")
    for t, note in NO_GOOGLE_RICH_RESULT.items():
        if t in types:
            add("P2", "schema", f"{t} markup present.", note)

    # robots.txt
    origin = f"{urllib.parse.urlparse(final).scheme}://{urllib.parse.urlparse(final).netloc}"
    rob = fetch(origin + "/robots.txt")
    bots = {}
    sitemaps = []
    if rob["status"] == 200 and rob["body"]:
        groups, sitemaps = parse_robots(rob["body"])
        for bot in CLASSIC_BOTS + SEARCH_BOTS + TRAINING_TOKENS + LIVE_FETCHERS:
            allowed, matched = is_allowed(groups, bot, path)
            bots[bot] = {"allowed": allowed,
                         "rule_from": "own group" if matched == bot.lower() else matched}
        for bot in CLASSIC_BOTS:
            if not bots[bot]["allowed"]:
                add("P0", "robots", f"robots.txt blocks {bot} from {path}.",
                    "Allow it; classic search and Copilot (Bing) depend on it.")
        blocked = [b for b in SEARCH_BOTS if not bots[b]["allowed"]]
        if blocked:
            add("P0", "robots", f"robots.txt blocks {', '.join(blocked)} from {path}.",
                "These search-index crawlers decide AI-search citation eligibility; allow them "
                "even if you block the training crawlers.")
        implicit = [b for b in SEARCH_BOTS if bots[b]["allowed"] and bots[b]["rule_from"] != "own group"]
        if implicit:
            add("P2", "robots", f"{', '.join(implicit)} allowed only via the '*' group.",
                "That is fine as is. If you add a named group for any of them, copy every "
                "'*' Disallow line into it: a crawler with its own group ignores '*' entirely.")
    elif rob["status"] is not None and (rob["status"] >= 500 or rob["status"] == 429):
        add("P0", "robots", f"robots.txt answers HTTP {rob['status']}.",
            "Google stops crawling the whole site for 12 hours when robots.txt returns a "
            "server error, then falls back to the last good copy. Make it return 200 or 404.")
    elif rob["status"] in (401, 403):
        add("P1", "robots", f"robots.txt answered HTTP {rob['status']} to this script.",
            "Open it in a browser. If a firewall is refusing scripts, check it in Search "
            "Console's robots.txt report instead.")
    elif rob["status"] is None:
        add("P1", "robots", f"Could not fetch robots.txt ({rob['error']}).",
            "Open it in a browser; a timeout for real crawlers is treated like a server error.")
    else:
        add("P2", "robots", f"No robots.txt (HTTP {rob['status']}).",
            "Everything is allowed by default; add one to declare your sitemap and AI-bot policy.")
    report["robots_bots"] = bots

    # Sitemap
    candidates = sitemaps or [origin + "/sitemap.xml"]
    report["sitemaps_declared"] = sitemaps
    found = False
    for sm in candidates[:3]:
        r = fetch(sm)
        if r["status"] == 200 and re.search(r"<(urlset|sitemapindex)\b", r["body"], re.I):
            found = True
            break
    report["sitemap_found"] = found
    if not found:
        add("P1", "discovery", "No reachable XML sitemap (checked robots.txt Sitemap: lines and /sitemap.xml).",
            "Publish a sitemap and declare it in robots.txt.")

    # Bot fetches (server / CDN level)
    report["bot_fetch"] = {}
    if bot_fetch:
        probe = (h1 or title or "")[:40]
        for bot, ua in BOT_UAS.items():
            r = fetch(final, ua=ua)
            has_text = bool(probe) and probe in visible_text(r["body"] or "")
            report["bot_fetch"][bot] = {"status": r["status"], "page_text_present": has_text}
            if r["status"] == 200 and probe and not has_text:
                add("P1", "cdn", f"The {bot} user agent got HTTP 200 but not the page text "
                    "(likely a firewall challenge page).",
                    "Check the CDN/WAF bot settings and verified-bot allowlist.")
            if r["status"] != 200:
                pri = "P0" if bot in SEARCH_BOTS or bot == "Googlebot" else "P1"
                add(pri, "cdn", f"Request with the {bot} user agent got {r['status'] or r['error']} "
                    f"while a browser got 200.",
                    "Check the CDN/WAF bot settings (Cloudflare and others can block AI crawlers "
                    "independently of robots.txt). CDNs verify real bots by IP, so confirm in the "
                    "CDN dashboard or your access logs.")

    # Server response
    if page["seconds"] and page["seconds"] > 3:
        add("P2", "performance", f"Server took {page['seconds']}s for the HTML.",
            "This is one fetch, not Core Web Vitals; measure LCP, INP and CLS in PageSpeed Insights.")

    order = {"P0": 0, "P1": 1, "P2": 2}
    report["findings"] = sorted(findings, key=lambda f: order[f["priority"]])
    return report


def print_report(r: dict):
    print(f"=== SEO + GEO audit: {r['url']} ===")
    if r.get("tool_error"):
        print(f"tool error (not a site finding): {r['tool_error']}")
        return
    if r.get("error"):
        print(f"error: {r['error']}")
    else:
        print(f"final_url: {r['final_url']}  status: {r['status']}  server_seconds: {r['server_seconds']}")
        print(f"title: {r.get('title') or 'MISSING'}")
        print(f"h1: {r.get('h1') or 'MISSING'}")
        print(f"html lang/dir: {r.get('html_lang')}/{r.get('html_dir')}  hebrew_share: {r.get('hebrew_share')}")
        print(f"canonical: {r.get('canonical')}")
        print(f"jsonld_types: {', '.join(r.get('jsonld_types') or []) or 'none'}")
        print(f"hreflang: {len(r.get('hreflang') or [])} alternate(s)")
        print(f"sitemap_found: {r.get('sitemap_found')}")
        print("robots.txt per crawler (audited path):")
        for bot, v in (r.get("robots_bots") or {}).items():
            print(f"  {bot}: {'allowed' if v['allowed'] else 'BLOCKED'} ({v['rule_from']})")
        if r.get("bot_fetch"):
            print("server response per bot user agent:")
            for bot, v in r["bot_fetch"].items():
                print(f"  {bot}: {v['status']} text_present={v['page_text_present']}")
    print()
    print("## Fix list (fix P0 first)")
    if not r["findings"]:
        print("  The automated checks did not run (see error above)." if r.get("error")
              else "  No findings from the automated checks.")
    for i, f in enumerate(r["findings"], 1):
        print(f"  {i}. [{f['priority']}] {f['area']}: {f['finding']}")
        print(f"     fix: {f['fix']}")


def main():
    parser = argparse.ArgumentParser(description="SEO + GEO single-page audit with a prioritized fix list")
    parser.add_argument("url", help="URL to audit")
    parser.add_argument("--json", action="store_true", help="Print the report as JSON")
    parser.add_argument("--no-bot-fetch", action="store_true",
                        help="Skip the requests sent with crawler user agents")
    args = parser.parse_args()
    url = args.url if args.url.startswith("http") else f"https://{args.url}"
    report = audit(url, bot_fetch=not args.no_bot_fetch)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(report)
    sys.exit(2 if report.get("tool_error") else 1 if report.get("error") else 0)


if __name__ == "__main__":
    main()
