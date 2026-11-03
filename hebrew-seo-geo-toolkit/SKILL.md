---
name: hebrew-seo-geo-toolkit
description: Audit and optimize Israeli websites for Hebrew SEO and GEO (Generative Engine Optimization) on Google.co.il and AI search engines (ChatGPT, Perplexity, Gemini, Copilot, Claude), ending in a prioritized fix list. Use when user asks to audit a site's SEO or AI visibility, Hebrew keyword research, Israeli SEO, .co.il domain optimization, hreflang, Hebrew schema.org markup, AI crawler access in robots.txt, GEO optimization, EEAT, or asks about "kidum atarim", "milot mafteach", "SEO", "GEO", or Israeli search ranking. Includes a free audit script with per-crawler checks, Hebrew keyword variants checked against Search Console data, Princeton GEO methods, Google's AI-features guidance, and Israeli business schema (Shabbat and holiday hours, kosher certification). Do NOT use for paid advertising campaigns or social media marketing.
license: MIT
compatibility: Requires network access for the audit and keyword scripts. Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex. The DataForSEO scripts need a paid DataForSEO account.
---


# Hebrew SEO & GEO Toolkit

## Instructions

The deliverable is a **prioritized fix list** for the user's site (Step 10), not a tutorial. Steps 1-9 gather the evidence for it. Every finding you report must cite what you observed (script output, a URL, a Search Console screen), never a general best practice.

### Step 0: Intake

Ask before auditing, because the fix-first order depends on the answers:

1. The URL, and two or three important inner pages (a service page, a product page, an article).
2. Site type: local service, e-commerce, content/publisher, or SaaS.
3. Target area: specific cities, all of Israel, or international.
4. Hebrew-only, or Hebrew plus English (or Arabic/Russian).
5. The five searches they most want to win, in their own words.
6. Access: Google Search Console, Google Business Profile, Bing Webmaster Tools, the CDN dashboard (yes/no each).
7. Platform (Wix, WordPress, Shopify, custom) and whether a developer is available. This decides whether a fix is "owner can do it" or "needs a developer".
8. Opening hours, including Shabbat and holidays. Do not assume the business closes on Shabbat.

### Step 1: Run the Automated Audit

```bash
python3 scripts/seo_audit.py "https://example.co.il"
python3 scripts/seo_audit.py "https://example.co.il/service" --json
```

Run it on the home page and on each inner page from intake. It audits one URL per run and does not crawl. It reports, already sorted P0 > P1 > P2:

- page status and redirect chain; `noindex`, `nosnippet` or `max-snippet:0` in meta robots or `X-Robots-Tag`; canonical
- title, description, H1, viewport, Open Graph, and `<html lang>` / `dir` (accessibility and rendering; Google says it does not use `lang` to detect a page's language)
- hreflang on the page and whether it lists the page itself
- JSON-LD types, blocks that fail to parse, and markup Google no longer rewards (FAQPage, HowTo, Speakable)
- robots.txt evaluated per crawler **for the audited path**, with `*` and `$` wildcards; declared `Sitemap:` lines; a robots.txt that answers 5xx (Google then stops crawling the site for 12 hours and afterwards relies on its last good copy)
- the same page requested with the Googlebot, OAI-SearchBot, PerplexityBot and Claude-SearchBot user agents, to catch a CDN or firewall refusing AI crawlers while robots.txt allows them
- how much text sits in the raw HTML (JavaScript-injected text is invisible to crawlers that do not render)

Read its limits before reporting:

- **Exit 2** means this machine could not run the audit (usually Python without current root certificates). It is not a finding about the site.
- **HTTP 401/403/429 to the script** usually means a firewall refused a scripted client. If the page opens in a browser, audit by hand instead of reporting downtime. A 503 can be either a firewall or a real outage: retry, and check in a browser and in Search Console.
- A bot user agent getting 403 is a strong lead, not proof. CDNs verify real crawlers by IP, so confirm in the CDN dashboard or access logs. In July 2025 Cloudflare announced it was "changing the default to block AI crawlers", so check its bot settings on any Cloudflare site.

**No-code route for a non-developer:** view-source in the browser (title, description, `lang`, canonical), the site address followed by /robots.txt in a browser tab, Google's Rich Results Test (structured data), PageSpeed Insights (Core Web Vitals on mobile), and Search Console URL Inspection (what Google actually indexed).

### Step 2: Checks That Need the Owner's Accounts

The script cannot see these. Ask the owner to open them, or to share screenshots:

1. **Search Console > Security & Manual actions.** Any manual action or security issue (hacked pages are common on unpatched WordPress sites) goes to the top of the fix list, above everything else.
2. **Search Console > Pages (indexing) and URL Inspection** on the key pages: excluded pages, the canonical Google chose, and crawl errors.
3. **Search Console > Settings > Search generative AI control.** Google states that "a site must be included in Search generative AI features in Search Console to be eligible for display in generative AI features on Google Search". As of 31 August 2026 the control is rolled out to all websites. It is on by default, but if someone switched it off, the site disappears from AI Overviews, AI Mode and Discover's generative features within 1-2 days. It does not affect AI training; that is `Google-Extended`.
4. **Google Business Profile** (local businesses): primary category, hours including holidays, Hebrew description, reviews, and that name, address and phone match the site exactly. For a local service business this often matters more than any on-page fix.
5. **Google Merchant Center** (online shops): product feed status and errors. For merchant listings Google requires an `Offer` with an active price above zero (use `ILS`) and recommends availability (Google's merchant listing documentation).
6. **Bing Webmaster Tools**: indexed by Bing (Copilot grounds on it), plus the AI Performance report.
7. **Core Web Vitals** (PageSpeed Insights or Search Console): LCP, INP and CLS on mobile. INP replaced FID as a Core Web Vital; do not report FID.

### Step 3: Hebrew Keyword Coverage

Israelis search in Hebrew script, and the same concept surfaces in several written forms. Prefix forms (ה, ו, ב, כ, ל, מ, ש and clusters like וה, מה, כש) attach to the first word; after ב, כ or ל the article ה is not written (בבית, not בהבית). Acronyms appear with and without gershayim (נדל"ן, נדל״ן, נדלן). Plurals, construct state (smikhut), ktiv male versus ktiv haser (תוכנית / תכנית), and Hebrew versus English terms (קידום אתרים / SEO) also vary; those need judgment, not a script.

```bash
python3 scripts/analyze_keywords.py --keywords 'נדל"ן,דירה להשכרה'
python3 scripts/analyze_keywords.py --keywords 'נדל"ן' --gsc-queries Queries.csv
```

The second form is the real check. Export Search Console > Performance > Queries as CSV, and the script reports which generated forms actually appear in the site's queries, with impressions, and which spelling searchers typed. Do not claim that missing prefix forms lose "most of the traffic": measure it from the export. Absence from the export is weak evidence, since rare queries may not appear in it; treat "not seen" as "not seen yet", not as zero.

**Free keyword sources:** the Search Console Queries export, Google Trends filtered to Israel, Google autocomplete and "People also ask" in a browser set to Hebrew.

**Paid, optional (DataForSEO):** `keyword_research.py`, `related_keywords.py`, `autocomplete_ideas.py`, `serp_analysis.py`, `competitor_gap.py`, `domain_overview.py`, `backlinks.py`. All default to Israel (`2376`) and Hebrew (`he`). DataForSEO is pay-as-you-go with a $50 minimum top-up and a $1 trial credit for new accounts; set `DATAFORSEO_SANDBOX=1` to test request shapes for free against dummy data. Labs endpoints hold only Hebrew and Arabic data for Israel, so the Labs scripts refuse `--language en` with Israel. Google Ads endpoints allow 12 requests per minute per account. Credentials are read from `DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD` only; never put them in a command line.

### Step 4: Language, Domain and hreflang

```html
<link rel="alternate" hreflang="he" href="https://example.co.il/page" />
<link rel="alternate" hreflang="en" href="https://example.co.il/en/page" />
<link rel="alternate" hreflang="x-default" href="https://example.co.il/en/page" />
```

Rules, per Google's localized-versions documentation:

1. A language code alone is valid ("you can specify a language code by itself"). Use `he`; add a region (`he-IL`) only when you have more than one Hebrew version to distinguish. Either is correct for a single Hebrew site.
2. Every version must list itself and every other version, or the pair is ignored.
3. HTML tags, HTTP headers and the sitemap are three equivalent methods. Pick one; using several adds no benefit and makes mismatches more likely.
4. `x-default` serves visitors whose browser language matches none of your versions, so on a Hebrew + English site they are by definition not matched by `he`. English is usually the better fallback for them; choose Hebrew only if most of those visitors are in Israel anyway (for example Israelis whose browsers are set to Russian or Arabic). Decide from the audience; Google's spec does not prescribe a language.
5. Set `lang="he"` and `dir="rtl"` on Hebrew pages for rendering and screen readers. Google says it does not use the `lang` attribute (or hreflang) to detect a page's language, so this is not a ranking fix.
6. **URL slugs:** Google recommends words in the audience's language and UTF-8 for non-ASCII characters, so Hebrew slugs are fine. They turn into long percent-encoded strings when pasted into messages, which is a usability trade-off, not an SEO one. Pick one style, keep slugs short, and 301-redirect if you ever change them.

**Domain and geography:** a `.co.il` domain is a strong country signal on its own. Google's multi-regional guide lists "Server location irrelevant" for a country-code domain, so do not move hosting to Israel for SEO (do it for speed if your users are slow). Search Console has no country targeting any more (the International Targeting report is no longer supported), and its properties are your own domains: if you own both `example.co.il` and `example.com`, verify each.

### Step 5: Apply GEO to Content

Google's own AI optimization guide says that optimizing for generative AI search "is optimizing for the search experience, and thus still SEO", that no special files or markup are needed, and that creating separate pages for every query variation "primarily to manipulate rankings or generative AI responses" violates its scaled content abuse policy. Answer the adjacent sub-questions on the main page instead of spinning up one page per variation.

The **Princeton GEO paper** (Aggarwal et al., KDD 2024) tested nine content edits on a research engine and on Perplexity. Its order, from Table 1 on Position-Adjusted Word Count:

| Method | Effect vs no optimization | How to apply |
|--------|--------------------------|--------------|
| **Quotation Addition** | Strongest | Add real expert quotes with attribution |
| **Statistics Addition** | Very strong | Add specific numbers, each with its source |
| **Fluency Optimization** | Strong | Improve readability and flow |
| **Cite Sources** | Strong | Link authoritative references |
| **Technical Terms** | Moderate | Use the domain's real terminology |
| **Easy-to-understand** | Moderate | Simplify complex concepts |
| **Authoritative Tone** | Modest | Confident, expert language |
| **Unique Words** | Negligible | Grouped with the non-performing methods |
| ~~Keyword Stuffing~~ | **Below baseline** | Avoid |

The headline: the best methods improve on the baseline by 41% on Position-Adjusted Word Count and 28% on Subjective Impression, and the strongest pair was Fluency Optimization plus Statistics Addition. Two caveats to pass on: on the Subjective Impression metric Authoritative Tone ranks higher and keyword stuffing is not below baseline, so "worse than doing nothing" holds for word count only; and the paper tested English queries against 2023 engines, so its effect on Hebrew pages in today's engines is untested.

**Never invent a statistic or a quote** to apply these methods. Every number and every quotation must come from a real, linkable source. An invented figure on a YMYL page (health, finance, legal) is a trust problem and can be a legal one.

**Structure that helps extraction** (practice, not a Google requirement): a direct answer at the top of each section, a clear H1 > H2 > H3 hierarchy, lists and tables for comparisons, and question-shaped headings for common questions.

### Step 6: Know What Each AI Platform Documents

| Platform | What the vendor documents | Action |
|----------|---------------------------|--------|
| Google AI Overviews / AI Mode | Google index; no extra requirements; may use "query fan-out"; both available in Hebrew and in Israel | Normal SEO, plus the Search generative AI control left on |
| Gemini app | `Google-Extended` governs Gemini training AND grounding in Gemini Apps | Blocking `Google-Extended` does not affect Search |
| ChatGPT search | `OAI-SearchBot` decides inclusion; sites opted out "will not be shown in ChatGPT search answers" | Allow `OAI-SearchBot` even if you block `GPTBot` |
| Perplexity | `PerplexityBot` indexes for search and is "not used to crawl content for AI foundation models" | Allow `PerplexityBot` |
| Claude | `Claude-SearchBot` indexes for search; blocking it "may reduce your site's visibility" | Allow `Claude-SearchBot` even if you block `ClaudeBot` |
| Copilot | Grounds on Bing; Bing's AI Performance report shows Copilot citations | Allow Bingbot, verify in Bing Webmaster Tools |

**On Claude's search backend:** third-party reports attribute Claude's web search to Brave, but Anthropic's crawler documentation names no search provider. Do not state it as fact to a client. Similarly, do not tell a client that ChatGPT or Perplexity "fall back" to Bing or Google: neither vendor's crawler documentation says so.

The full crawler list (OpenAI, Anthropic, Perplexity, Google, Apple, Mistral, Meta, Common Crawl), with what blocking each one does, is in [references/platform-algorithms.md](./references/platform-algorithms.md).

### Step 7: Apply EEAT Principles

Google's E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) applies to classic and AI results alike. Israeli signals:

- **Experience:** real Israeli examples and case studies.
- **Expertise:** named authors with credentials; references to the Israeli regulation that applies.
- **Authoritativeness:** mentions and links from Israeli publications and .co.il sites.
- **Trustworthiness:** HTTPS, a Hebrew contact page with a +972 number, a Hebrew privacy policy.

For YMYL pages in Hebrew (medical, financial, legal), have a licensed Israeli professional review the content. See [references/eeat-principles.md](./references/eeat-principles.md).

### Step 8: Build Israeli Structured Data

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rehov Example 42",
    "addressLocality": "Tel Aviv-Yafo",
    "postalCode": "6100000",
    "addressCountry": "IL"
  },
  "telephone": "+972-3-555-0000",
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification",
     "dayOfWeek": ["Sunday","Monday","Tuesday","Wednesday","Thursday"],
     "opens": "09:00", "closes": "18:00"},
    {"@type": "OpeningHoursSpecification",
     "dayOfWeek": "Friday", "opens": "09:00", "closes": "14:00"}
  ],
  "specialOpeningHoursSpecification": [
    {"@type": "OpeningHoursSpecification",
     "validFrom": "2027-04-21", "validThrough": "2027-04-21",
     "opens": "09:00", "closes": "12:00"},
    {"@type": "OpeningHoursSpecification",
     "validFrom": "2027-04-22", "validThrough": "2027-04-22",
     "opens": "00:00", "closes": "00:00"}
  ]
}
```

Israeli specifics:

1. **Week:** model the hours the intake gave you. The example is the common Sunday-Thursday plus short Friday pattern. Many businesses open on Shabbat, so ask. To mark a day closed explicitly, Google says to "set both opens and closes properties to "00:00"".
2. **Holidays:** use `specialOpeningHoursSpecification` (schema.org: it overrides the general hours) for Rosh Hashana, Yom Kippur, Pesach and so on (the example closes on the first day of Pesach 2027, 22 April, and opens a short Erev Pesach the day before), and set the same special hours in Google Business Profile. Keep `dayOfWeek` values in English: Google supports only the standard schema.org enumeration values, in English.
3. **Phone:** Google's local-business documentation says "Be sure to include the country code and area code", so use `+972`. A local `03-` number is not a validation error, just weaker.
4. **Kosher:** state the certifying body (Rabbanut, Badatz) in visible text; Google has no kosher-specific structured data.
5. **Currency:** `ILS`. For an online shop, use `Product` with an `Offer` carrying the price in `ILS` and availability, and keep it consistent with the Merchant Center feed.

**Markup not to recommend for Google benefit:** Google stopped showing FAQ rich results on 7 May 2026, removed HowTo rich results in September 2023, and limits Speakable to English-language news publishers in the US. FAQPage remains valid schema.org and other consumers may read it, but do not promise a client any Google result from it. Full templates: [references/schema-templates.md](./references/schema-templates.md).

### Step 9: Set the Crawler Policy (robots.txt) and llms.txt

If the audit found no crawler blocked, change nothing here. Otherwise merge the relevant groups below into the existing file:

```
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# Search-index crawlers: these decide AI-search citation eligibility
User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

# Training crawlers: allow or disallow as a business decision
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

# Google-Extended: Gemini training AND Gemini app grounding (not Search)
User-agent: Google-Extended
Allow: /

Sitemap: https://example.co.il/sitemap.xml
```

**Decisions to make with the owner:**

- Blocking a training crawler (`GPTBot`, `ClaudeBot`, `Applebot-Extended`, `MistralAI-Training`, `CCBot`) opts out of training without losing search citations, as long as the search crawler stays allowed.
- `Google-Extended` is different: it also controls grounding in the Gemini app. Blocking it keeps the site in Google Search, AI Overviews and AI Mode, but removes it as a grounding source in Gemini Apps. Decide that separately.
- **One group per crawler.** Google's spec says "Only one group is valid for a particular crawler": a crawler that has its own group ignores the `*` group completely. Before adding a named group, copy every `Disallow` line from `*` into it, or the named bot loses those restrictions. The template above has no `*` rules; merge it into the site's existing file, do not paste it over.
- User-triggered fetchers (`ChatGPT-User`, `Claude-User`, `Perplexity-User`) are a third category: OpenAI says robots.txt "may not apply" to `ChatGPT-User`, and Perplexity says `Perplexity-User` "generally ignores robots.txt rules".
- Changes are not instant: OpenAI says about 24 hours for search, Perplexity up to 24 hours.

**llms.txt: optional, and NOT a ranking or citation signal.** Google says Search does not use it, and no AI engine has announced reading it as a ranking input. The proposal (Jeremy Howard, 2024, revised to v2 in August 2026) is cheap to ship, but ship it after the fundamentals and never sell it to a client as an AI-visibility win.

### Step 10: Assemble the Fix List (the deliverable)

Merge the script output (Step 1), the account checks (Step 2), the keyword coverage (Step 3) and anything else observed into one table, ordered by this ladder:

1. **Penalties and access blockers:** manual actions or security issues, page errors, `noindex`, unintended `nosnippet` / `max-snippet:0`, a robots.txt answering 5xx, robots.txt blocking Googlebot/Bingbot or a search-index AI crawler, CDN refusing AI crawlers, Search generative AI control switched off, text not in the raw HTML.
2. **Local presence** (local businesses): Google Business Profile category, hours and NAP match.
3. **Indexing hygiene:** canonicals, redirect chains, duplicate or doorway pages (one near-identical page per city is a named Google spam pattern).
4. **Content versus the five target searches:** missing pages or sections, Hebrew forms seen in Search Console but not on the page.
5. **Core Web Vitals on mobile** (LCP, INP, CLS).
6. **Structured data** that is valid and useful (LocalBusiness with holiday hours, Organization, Product, Article).
7. **GEO content edits:** real sourced statistics and quotes, answer-first sections.
8. **Optional extras:** llms.txt.

| # | Finding | Evidence | Why it matters | Who fixes it | Fix | How to confirm |
|---|---------|----------|----------------|--------------|-----|----------------|
| 1 | robots.txt blocks Claude-SearchBot on /services | seo_audit.py line "robots.txt blocks Claude-SearchBot" | Not eligible for Claude search citations | Owner (robots.txt editor) | Add a Claude-SearchBot group that repeats the site's other `*` Disallow lines, except the one covering /services | Re-run seo_audit.py |

Write the table in the user's language.

End with a **"Do not spend on"** list where it applies: llms.txt as a ranking lever, FAQ rich results, Speakable on a Hebrew site, moving hosting to Israel for rankings, one page per city or per query variation.

### Step 11: Monitor in Four Layers

GEO outcomes lag and are confounded, so separate the fast proxy from the slow outcome:

| Layer | Question | Latency |
|-------|----------|---------|
| 1. Crawler access | Can the bots fetch and parse the page? | Instant |
| 2. Citability | Given the page, is it extractable and answer-shaped? | Minutes |
| 3. Surfacing | Does an engine cite you for a bare query, unprompted? | Days to weeks |
| 4. Rankings and clicks | Position, impressions, CTR | Weeks to months |

Check layer 1 before concluding anything about content: "not crawled yet" and "crawled but not chosen" look identical in the answer box. For layer 3, ask a fixed panel of Hebrew and English queries in each assistant without giving the URL, and record citations over time against a page you did not edit.

**Search Console Generative AI performance reports** (launched 3 June 2026, rolled out to all websites as of 31 August 2026) cover AI Overviews, AI Mode and Discover's generative features. Google lists impressions by page, country, device and date, and documents no click, CTR, position or query data in them. **Bing's AI Performance report** shows Copilot citations and a sample of grounding queries. Third-party trackers (Otterly.ai, Profound, SE Ranking) automate layer 3. Watch referral traffic from chatgpt.com, perplexity.ai, gemini.google.com and copilot.microsoft.com in analytics.

See [references/tools-and-apis.md](./references/tools-and-apis.md) for tools.

## Examples

### Example 1: Audit and Fix List for a Local Business
User says: "Audit my accounting firm's site in Ramat Gan and tell me what to fix first"
Actions:
1. Intake: local service, Ramat Gan plus Tel Aviv, Hebrew only, five target searches, has Search Console and Google Business Profile, WordPress behind Cloudflare, closed on Shabbat and holidays.
2. Run `seo_audit.py` on the home page and the two service pages. It reports Claude-SearchBot blocked by robots.txt and a 403 to OAI-SearchBot from the CDN.
3. Owner checks Search Console: the generative AI control is on; two service pages are "Crawled, currently not indexed".
4. Business Profile shows no holiday hours and a phone number that differs from the site.
5. Search Console export shows "רואה חשבון ברמת גן" with impressions but no page targeting it.
Note: the owner can change Cloudflare's bot settings here. On a hosted builder such as Wix, the owner edits robots.txt in the dashboard, but Wix documents no owner control over its own CDN or firewall, so a CDN-level 403 there is a request to the platform's support, not an owner fix.
Result: a fix list with the robots.txt and CDN fixes first, then the profile NAP and holiday hours, then the two unindexed pages, then one new service section, plus a "do not spend on" note about FAQ schema.

### Example 2: Bilingual hreflang
User says: "Set up hreflang for my Hebrew/English .co.il site"
Actions:
1. Pair each Hebrew page with its English version.
2. Choose one method (HTML tags in the head), with each page listing itself and its counterpart.
3. Set `x-default` to the English page, since visitors matched by neither `he` nor `en` are more likely to read English (Hebrew only if they are mostly Israelis on non-Hebrew browsers).
4. Run `seo_audit.py` on one page of each pair to confirm self-reference, then open the counterpart to confirm the return link.
Result: reciprocal `he` / `en` / `x-default` annotations in one method.

### Example 3: GEO for an Israeli SaaS Page
User says: "Why doesn't ChatGPT or Claude mention our product?"
Actions:
1. Layer 1 first: `seo_audit.py` shows the page text is injected by JavaScript (under 500 characters in the raw HTML) and the CDN returning 403 to OAI-SearchBot.
2. Fix rendering and the CDN bot setting before touching copy.
3. Then apply GEO edits using the company's own published benchmark numbers and a named customer quote, each linked.
4. Set up a fixed query panel and re-check weekly against an unedited control page.
Result: access fixed first, sourced content edits second, measurement in place.

### Example 4: Kosher Restaurant Structured Data
User says: "Create structured data for my kosher restaurant in Jerusalem"
Actions:
1. Ask the actual hours, including Friday, Saturday night and holidays.
2. Build Restaurant JSON-LD with Israeli address, +972 phone, `ILS`, and `specialOpeningHoursSpecification` for the holidays.
3. State the kashrut certificate in visible text.
4. Mirror the holiday hours in Google Business Profile.
Result: valid LocalBusiness markup and a matching Business Profile, with no FAQ or Speakable markup promised as a Google feature.

### Example 5: Hebrew Keyword Coverage
User says: "Which Hebrew keywords am I missing for my real estate site?"
Actions:
1. Export Search Console Queries as CSV.
2. Run `analyze_keywords.py --keywords 'נדל"ן,דירה להשכרה' --gsc-queries Queries.csv`.
3. Note which forms and spellings searchers actually use, then check those words appear on the target pages.
4. Optionally run `related_keywords.py 'דירה להשכרה'` (paid) for volume and difficulty.
Result: a list of real query forms mapped to pages, measured rather than guessed.

## Bundled Resources

### Scripts
- `scripts/seo_audit.py`: single-page SEO + GEO audit ending in a P0/P1/P2 fix list; per-crawler robots.txt and user-agent checks; `--json` output. Free, no API. Exit 0 audit ran, 1 page unreachable, 2 this machine could not run it.
- `scripts/analyze_keywords.py`: Hebrew prefix and spelling variants; with `--gsc-queries`, coverage against a Search Console Queries export. Free.
- `scripts/keyword_research.py`, `serp_analysis.py`, `autocomplete_ideas.py`, `related_keywords.py`, `competitor_gap.py`, `domain_overview.py`, `backlinks.py`: DataForSEO (paid). Default Israel and Hebrew; `--location` / `--language` to change; `DATAFORSEO_SANDBOX=1` for free request testing.
- `scripts/dataforseo_api.py`, `scripts/credential.py`: shared client; credentials from environment variables only.

### References
- `references/platform-algorithms.md`: what each AI platform and crawler vendor documents, the full crawler list, and what blocking each one does. Consult before writing robots.txt or explaining AI visibility.
- `references/seo-checklist.md`: prioritized checklist behind the Step 10 ladder. Consult for a full manual audit.
- `references/hebrew-seo.md`: .co.il, RTL, Israeli directories and NAP, Hebrew search behaviour.
- `references/geo-research.md`: the Princeton GEO methods with examples and caveats.
- `references/schema-templates.md`: JSON-LD templates and which ones Google still rewards.
- `references/aeo-considerations.md`: answer-engine content structure and AI crawler management.
- `references/eeat-principles.md`: E-E-A-T and YMYL handling.
- `references/tools-and-apis.md`: free and paid tools, including DataForSEO setup.
- `references/domain-checklist.md`: coverage checklist for this skill.

## Gotchas

- Agents report a script failure as a site problem. A TLS error from a local Python, or a 403 from a firewall that refuses scripts, says nothing about the site. The audit script separates these (exit 2, "audit blocked"); keep the distinction in the report.
- Agents still recommend FAQPage and Speakable "for rich results". Google stopped showing FAQ rich results on 7 May 2026 and Speakable is limited to English-language US news. Recommending them as a Google win is wrong.
- Agents apply hreflang folklore: "always he-IL", "the sitemap is required", "x-default must be English". Google allows a bare `he`, treats the three methods as equivalent, and sets no language for `x-default`.
- Agents assume Saturday closed and Monday-Friday hours. Ask; then model Sunday-Thursday, Friday, Shabbat and holidays as the business actually runs.
- Agents allow `GPTBot` and `ClaudeBot` and think AI search is covered. Those are training crawlers; citation eligibility comes from `OAI-SearchBot`, `Claude-SearchBot` and `PerplexityBot`.
- Agents invent statistics to "apply GEO". Every number and quote must have a real source.
- Agents "fix" robots.txt by adding `User-agent: OAI-SearchBot` / `Allow: /`. A named group replaces the `*` group for that bot, so every existing Disallow stops applying to it. Copy the `*` rules into each named group.
- Agents run DataForSEO with English for Israel. Labs has only Hebrew and Arabic data for Israel; the scripts default to `he` and refuse `en` there.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Google AI features guidance | https://developers.google.com/search/docs/appearance/ai-features | Requirements for AI Overviews and AI Mode |
| Google AI optimization guide | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | Google's position on GEO, fan-out pages, special markup |
| Search generative AI control | https://support.google.com/webmasters/answer/16908024?hl=en | Opt-out and eligibility for AI Overviews and AI Mode |
| Search Console generative AI reports | https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports | Which metrics the AI reports expose |
| Google Search documentation updates | https://developers.google.com/search/updates | Rich result deprecations (FAQ, HowTo) |
| Google localized versions (hreflang) | https://developers.google.com/search/docs/specialty/international/localized-versions | Language codes, x-default, methods |
| Google multi-regional sites | https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites | ccTLD and server location |
| Google local business structured data | https://developers.google.com/search/docs/appearance/structured-data/local-business | Phone format, opening hours |
| OpenAI bot docs | https://developers.openai.com/api/docs/bots | `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `OAI-AdsBot` |
| Anthropic crawler docs | https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler | `ClaudeBot`, `Claude-SearchBot`, `Claude-User` |
| Perplexity crawler docs | https://docs.perplexity.ai/docs/resources/perplexity-crawlers | `PerplexityBot`, `Perplexity-User` |
| Princeton GEO paper | https://arxiv.org/abs/2311.09735 | GEO methods and their measured effects |
| Bing Webmaster Tools AI Performance | https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview | Copilot citation reporting |
| DataForSEO docs | https://docs.dataforseo.com/v3/ | Endpoints, locations and languages |
| llms.txt proposal | https://llmstxt.org | Convention for an AI-readable site index |

## Troubleshooting

### Error: "seo_audit.py exits 2 with a TLS failure"
Cause: this machine's Python has no certificate store, or one older than the site's root CA (confirmed on gov.il with an outdated bundle). Verified not to be a site fault when other clients load the page.
Solution: run your Python's "Install Certificates" step, or set `SSL_CERT_FILE` to a current CA bundle, and re-run. Only if a current store still fails, check the site's chain in an SSL checker.

### Error: "HTTP 403 to this script" but the site works in a browser
Cause: the site's firewall refuses scripted clients regardless of user agent (gov.il does this).
Solution: audit by hand: view-source, Rich Results Test, Search Console URL Inspection. Do not report downtime.

### Error: "Not appearing in AI search results"
Cause: check in this order, because the symptoms look identical: (1) a manual action, or robots.txt or the CDN blocking the search-index crawler; (2) the Search generative AI control is off, or `nosnippet` / `max-snippet:0` limits what Google can show (Google surfaces only); (3) the text is injected by JavaScript; (4) the content is not answer-shaped enough to be chosen.
Solution: run `seo_audit.py` and fix any P0 first. Check the Search Console control. Only after access is green, apply the GEO content edits.

### Error: "hreflang ignored"
Cause: the pair is not reciprocal, or a page does not list itself.
Solution: make every version list itself and every other version, in one method.

### Error: "Rich Results Test shows no FAQ result"
Cause: Google no longer shows FAQ rich results for any site.
Solution: nothing to fix. Keep the markup only if another consumer uses it.

### Error: "DataForSEO script prints an error 40501 or no data for Israel"
Cause: likeliest an unsupported location and language pair (Labs has no English for Israel) or an undocumented field; not verified against a live account.
Solution: use `--language he`, and test with `DATAFORSEO_SANDBOX=1` before spending credit.
