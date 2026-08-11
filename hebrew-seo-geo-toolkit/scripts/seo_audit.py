#!/usr/bin/env python3
"""
SEO audit script (no API required)
Usage: python3 scripts/seo_audit.py "https://example.com"
"""
import argparse
import urllib.request
import urllib.parse
import re
import time
import sys
import ssl
import urllib.error


# A bare tool token gets refused by a large share of real sites (CDN and WAF bot
# rules), which made this script report "Could not fetch URL" for sites that are
# perfectly reachable in a browser. Identify as a normal browser, with the tool
# name appended so the traffic is still attributable in a server log.
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36 SEO-Audit/1.1"
)


def fetch_url(url: str, timeout: int = 30) -> tuple:
    """Fetch URL and return (content, headers, load_time).

    On failure returns (None, None, None) plus the reason on stderr, so a
    blocked or TLS-failed fetch is distinguishable from an empty page instead
    of surfacing as a bare "Could not fetch URL".
    """
    try:
        start = time.time()
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "he-IL,he;q=0.9,en;q=0.8",
            },
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read().decode("utf-8", errors="ignore")
            headers = dict(resp.headers)
            load_time = time.time() - start
            return content, headers, load_time
    except urllib.error.HTTPError as e:
        print(f"  [fetch] HTTP {e.code} for {url}", file=sys.stderr)
        return None, None, None
    except urllib.error.URLError as e:
        # urllib wraps TLS failures inside URLError, so check the cause rather
        # than catching ssl.SSLError directly, which never fires here.
        if isinstance(getattr(e, "reason", None), ssl.SSLError):
            print(
                f"  [fetch] TLS failure for {url}: {e.reason}. If this is a "
                "local Python without root certificates, run the 'Install "
                "Certificates' step for your Python installation.",
                file=sys.stderr,
            )
        else:
            print(f"  [fetch] network error for {url}: {e.reason}", file=sys.stderr)
        return None, None, None
    except Exception as e:
        print(f"  [fetch] {type(e).__name__} for {url}: {e}", file=sys.stderr)
        return None, None, None


def extract_meta(html: str) -> dict:
    """Extract meta tags from HTML"""
    result = {}
    
    # Title
    title_match = re.search(r"<title[^>]*>([^<]+)</title>", html, re.I)
    result["title"] = title_match.group(1).strip() if title_match else None
    
    # Meta description
    desc_match = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
    if not desc_match:
        desc_match = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']description["\']', html, re.I)
    result["description"] = desc_match.group(1).strip() if desc_match else None
    
    # OG tags
    og_match = re.search(r'<meta[^>]+property=["\']og:title["\']', html, re.I)
    result["og_tags"] = bool(og_match)
    
    # JSON-LD
    jsonld_count = len(re.findall(r'application/ld\+json', html, re.I))
    result["jsonld_count"] = jsonld_count
    
    # H1 (handle inline tags like <br>)
    h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.DOTALL)
    if h1_match:
        h1_text = re.sub(r"<[^>]+>", " ", h1_match.group(1))  # Remove inner tags
        h1_text = re.sub(r"\s+", " ", h1_text).strip()  # Normalize whitespace
        result["h1"] = h1_text[:100]
    else:
        result["h1"] = None
    
    return result


# Search-index crawlers govern AI citation eligibility. Allowing only the
# training crawlers (GPTBot, ClaudeBot) leaves a site ineligible to be cited in
# ChatGPT search and Claude search, which is the single most common
# misconfiguration in this area.
SEARCH_BOTS = ["OAI-SearchBot", "Claude-SearchBot", "PerplexityBot"]
TRAINING_BOTS = ["GPTBot", "ClaudeBot"]
LIVE_FETCHERS = ["ChatGPT-User", "Claude-User", "Perplexity-User"]


def parse_robots(content: str) -> dict:
    """Parse robots.txt into {user-agent (lowercased): [(directive, path), ...]}.

    Consecutive User-agent lines share the group that follows them, per the
    robots.txt convention.
    """
    groups: dict = {}
    current: list = []
    expecting_agents = False
    for raw in content.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        field, _, value = line.partition(":")
        field = field.strip().lower()
        value = value.strip()
        if field == "user-agent":
            if not expecting_agents:
                current = []
                expecting_agents = True
            current.append(value.lower())
            groups.setdefault(value.lower(), [])
        elif field in ("allow", "disallow"):
            expecting_agents = False
            for agent in current:
                groups[agent].append((field, value))
    return groups


def is_allowed(groups: dict, agent: str, path: str = "/") -> tuple:
    """Return (allowed: bool, matched_group: str) for `agent` fetching `path`.

    A crawler obeys the group matching its own name; only if no such group
    exists does it fall back to the wildcard group. Longest matching rule wins,
    and Allow beats Disallow on an equal-length match.
    """
    key = agent.lower()
    matched = key if key in groups else ("*" if "*" in groups else None)
    if matched is None:
        return True, "none"
    best_len, best_allow = -1, True
    for directive, value in groups[matched]:
        # An empty Disallow value means "allow everything".
        if directive == "disallow" and value == "":
            if 0 > best_len:
                best_len, best_allow = 0, True
            continue
        if value and path.startswith(value.rstrip("*")):
            length = len(value)
            if length > best_len or (length == best_len and directive == "allow"):
                best_len, best_allow = length, directive == "allow"
    return best_allow, matched


def check_robots(url: str) -> dict:
    """Check robots.txt and resolve AI-bot access by parsing rules, not by
    looking for bot names in the text. A bot listed under `Disallow: /` is
    blocked, not present, and a bot with no rule of its own inherits the
    wildcard group."""
    parsed = urllib.parse.urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    content, _, _ = fetch_url(robots_url)

    result = {
        "exists": False,
        "ai_bots": [],
        "blocked_search_bots": [],
        "implicit_search_bots": [],
    }
    if content:
        result["exists"] = True
        groups = parse_robots(content)
        for bot in SEARCH_BOTS + TRAINING_BOTS + LIVE_FETCHERS:
            allowed, matched = is_allowed(groups, bot)
            state = "allowed" if allowed else "BLOCKED"
            source = "explicit" if matched == bot.lower() else f"via '{matched}'"
            result["ai_bots"].append(f"{bot}={state} ({source})")
            if bot in SEARCH_BOTS:
                if not allowed:
                    result["blocked_search_bots"].append(bot)
                elif matched != bot.lower():
                    result["implicit_search_bots"].append(bot)
    return result


def check_sitemap(url: str) -> bool:
    """Check if sitemap.xml exists"""
    parsed = urllib.parse.urlparse(url)
    sitemap_url = f"{parsed.scheme}://{parsed.netloc}/sitemap.xml"
    content, _, _ = fetch_url(sitemap_url)
    if not content:
        return False
    # Check for common sitemap indicators
    return "<urlset" in content.lower() or "<sitemapindex" in content.lower() or "<?xml" in content.lower()


def main():
    parser = argparse.ArgumentParser(description="SEO audit")
    parser.add_argument("url", help="URL to audit")
    args = parser.parse_args()
    
    url = args.url
    if not url.startswith("http"):
        url = f"https://{url}"
    
    print(f"=== SEO Audit: {url} ===")
    print()
    
    # Fetch page
    content, headers, load_time = fetch_url(url)
    if not content:
        print("error: Could not fetch URL")
        sys.exit(1)
    
    # Meta tags
    print("## Meta Tags")
    meta = extract_meta(content)
    title = meta["title"]
    print(f"title: {title[:60] if title else 'MISSING'}{'...' if title and len(title) > 60 else ''}")
    print(f"title_length: {len(title) if title else 0} chars")
    desc = meta["description"]
    print(f"description: {desc[:80] if desc else 'MISSING'}{'...' if desc and len(desc) > 80 else ''}")
    print(f"description_length: {len(desc) if desc else 0} chars")
    print(f"og_tags: {'yes' if meta['og_tags'] else 'no'}")
    print(f"h1: {meta['h1'] if meta['h1'] else 'MISSING'}")
    print()
    
    # Schema
    print("## Schema Markup")
    print(f"json_ld_blocks: {meta['jsonld_count']}")
    print()
    
    # Performance
    print("## Performance")
    print(f"load_time: {load_time:.2f}s")
    print(f"status: {'good' if load_time < 3 else 'slow'}")
    print()
    
    # robots.txt
    print("## robots.txt")
    robots = check_robots(url)
    print(f"exists: {'yes' if robots['exists'] else 'no'}")
    if robots["ai_bots"]:
        for entry in robots["ai_bots"]:
            print(f"  {entry}")
    else:
        print("ai_bots: no robots.txt to evaluate")
    if robots["blocked_search_bots"]:
        print(
            "CRITICAL: "
            f"{', '.join(robots['blocked_search_bots'])} "
            "cannot fetch this site. These are the search-index crawlers that "
            "govern AI citation eligibility, so the site is not eligible to be "
            "cited on those platforms."
        )
    if robots["implicit_search_bots"]:
        print(
            "NOTE: "
            f"{', '.join(robots['implicit_search_bots'])} "
            "are allowed only by the wildcard group, with no rule of their own. "
            "That works today, but tightening the wildcard would silently drop "
            "AI citations. Consider listing them explicitly."
        )
    print()
    
    # Sitemap
    print("## Sitemap")
    has_sitemap = check_sitemap(url)
    print(f"sitemap_xml: {'yes' if has_sitemap else 'no'}")
    print()
    
    print("=== Audit Complete ===")


if __name__ == "__main__":
    main()
