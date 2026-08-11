---
name: hebrew-seo-geo-toolkit
description: Optimize websites for Hebrew SEO and GEO (Generative Engine Optimization) on Google.co.il and AI search engines (ChatGPT, Perplexity, Gemini, Copilot, Claude). Use when user asks about Hebrew keyword research, Israeli SEO, .co.il domain optimization, Hebrew schema.org markup, AI search visibility, GEO optimization, EEAT, or asks about "kidum atarim", "milot mafteach", "SEO", "GEO", or Israeli search ranking. Includes Hebrew morphological analysis, Princeton GEO methods, platform-specific AI optimization, EEAT principles, JSON-LD structured data, and Israeli business schema (Shabbat hours, kosher certification). Do NOT use for paid advertising campaigns or social media marketing.
license: MIT
compatibility: Requires network access for keyword analysis and audits. Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---


# Hebrew SEO & GEO Toolkit

## Instructions

### Step 1: Audit Website (SEO + GEO)

Run a comprehensive audit covering both traditional SEO and AI search readiness.

**Quick SEO Audit (Free, no API needed):**
```bash
python3 scripts/seo_audit.py "https://example.co.il"
```

**Manual checks:**
```bash
# Check meta tags and schema markup
curl -sL "https://example.co.il" | grep -E "<title>|<meta name=\"description\"|<meta property=\"og:|application/ld\+json" | head -20

# Check robots.txt (verify AI bot access)
curl -s "https://example.co.il/robots.txt"

# Check sitemap
curl -s "https://example.co.il/sitemap.xml" | head -50
```

**Verify AI bot access in robots.txt:** Googlebot, Bingbot, GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User, ClaudeBot, Claude-SearchBot and Claude-User must all be allowed. The search-index crawlers (`OAI-SearchBot`, `Claude-SearchBot`) are the ones that govern citation eligibility, and they are the ones most often missing. See [references/seo-checklist.md](./references/seo-checklist.md) for the full prioritized audit checklist.

### Step 2: Analyze Hebrew Keyword Morphology

Hebrew is a root-based (shoresh) language where prefixes change meaning:

| Prefix | Hebrew | Meaning | Example |
|--------|--------|---------|---------|
| ha- | ה | the | habayit (the house) |
| ve- | ו | and | vehabayit (and the house) |
| be- | ב | in/at | babayit (in the house) |
| le- | ל | to/for | labayit (to the house) |
| me- | מ | from | mehbayit (from the house) |
| she- | ש | that/which | shebabayit (that in the house) |

For each target keyword:
1. Extract the root (shoresh) using morphological analysis
2. Generate all prefix combinations users might search
3. Include construct state (smikhut) forms: "beit kafe" vs "habait shel hakafe"
4. Account for male/female and singular/plural forms
5. Run `scripts/analyze_keywords.py --keywords "nadlan,dira,bayit"` for full variant analysis

Use **WebSearch** to research target keywords:
```
WebSearch: "{keyword} keyword difficulty site:ahrefs.com OR site:semrush.com"
WebSearch: "{keyword} search volume 2026"
```

### Step 3: Configure .co.il Domain SEO

| Setting | Value | Notes |
|---------|-------|-------|
| TLD priority | .co.il | Preferred for Israeli businesses |
| Server location | Israel or nearby CDN | Improves local ranking |
| Google Search Console | google.co.il property | Register separately from .com |
| Sitemap | Include hreflang annotations | Required for bilingual sites |

1. Register .co.il domain with an ISOC-IL accredited registrar
2. Set up Google Search Console for the .co.il property
3. Configure DNS with Israeli/nearby CDN endpoints (Cloudflare TLV)
4. Verify RTL layout loads correctly
5. Submit XML sitemap with hreflang annotations

See [references/hebrew-seo.md](./references/hebrew-seo.md) for domain strategy and local citation directories.

### Step 4: Implement hreflang Tags

```html
<link rel="alternate" hreflang="he-IL" href="https://example.co.il/page" />
<link rel="alternate" hreflang="en" href="https://example.co.il/en/page" />
<link rel="alternate" hreflang="x-default" href="https://example.co.il/en/page" />
```

Rules for Israeli sites:
1. Always use `he-IL` (not just `he`) for Israeli Hebrew content
2. Set `x-default` to the English version for international visitors
3. Every page must link bidirectionally to its counterpart in all languages
4. Use consistent absolute URLs across all hreflang declarations

### Step 5: Apply GEO Optimization (AI Search Engines)

**GEO = Generative Engine Optimization.** AI search engines don't rank pages, they **cite sources**. Being cited is the new "ranking #1".

Apply the **9 Princeton GEO Methods** (see [references/geo-research.md](./references/geo-research.md)):

Ordered by the paper's own Table 1, strongest first. A per-method percentage table circulates widely online (usually as "Cite Sources +40%"); it does not match the paper, which reports Quotation Addition as the strongest method and gives 40% as a headline ceiling for GEO overall, not a figure for any one method.

| Method | Effect vs no optimization | How to Apply |
|--------|--------------------------|--------------|
| **Quotation Addition** | Strongest | Add expert quotes with attribution |
| **Statistics Addition** | Very strong | Include specific numbers and data points |
| **Fluency Optimization** | Strong | Improve readability and flow |
| **Cite Sources** | Strong | Add authoritative citations and references |
| **Technical Terms** | Moderate | Include domain-specific terminology |
| **Easy-to-understand** | Moderate | Simplify complex concepts |
| **Authoritative Tone** | Modest | Use confident, expert language |
| **Unique Words** | Negligible | The paper groups this with the non-performing methods |
| ~~Keyword Stuffing~~ | **Below baseline** | **AVOID: scores worse than doing nothing** |

The paper's headline: the best methods improve on the baseline by 41% on Position-Adjusted Word Count and 28% on Subjective Impression.

**Best combination:** Fluency Optimization + Statistics Addition, which the paper reports as the strongest pairing.

**Content structure for AI extraction:**
- Use "answer-first" format (direct answer at top of each section)
- Clear H1 > H2 > H3 hierarchy
- Bullet points, numbered lists, tables for comparison data
- Short paragraphs (2-3 sentences max)
- FAQ format for common questions

**FAQPage Schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is [topic]?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "According to [source], [answer with statistics]."
    }
  }]
}
```

### Step 6: Optimize for Each AI Platform

Each AI search engine has unique ranking factors. Snapshot for 2026:

| Platform | Primary Index | Key Factor | Critical Requirement |
|----------|--------------|------------|---------------------|
| ChatGPT (search) | Own crawler (`OAI-SearchBot`) + Bing fallback | Domain authority + content-answer fit | Allow `OAI-SearchBot` separately from `GPTBot` (training); keep content genuinely current |
| Perplexity | Own crawler (`PerplexityBot`) + Google fallback | Semantic relevance | FAQ Schema, structured data, PDF/markdown sources |
| Google AI Overview | Google index | E-E-A-T + Knowledge Graph | Available to all users in Israel and in Hebrew; structured data and clear answer paragraphs help |
| Google AI Mode | Google index | E-E-A-T + sub-question coverage | A distinct surface from AI Overviews. Hebrew and Israel are both on Google's AI Mode availability list. Uses "query fan-out", so cover the related sub-questions on the page |
| Gemini (Google) | Google index + real-time web | E-E-A-T + recency | Same as Google Search |
| Copilot (Microsoft) | Bing index | Bing rank + MS ecosystem signals | Bing Webmaster Tools verified, LinkedIn/GitHub presence |
| Claude (with web search) | Anthropic's own `Claude-SearchBot` index; a third-party search backend is also involved | Factual density + citations | Allow `Claude-SearchBot`, clean source URLs |

**On Claude's search backend:** it is widely reported that Brave supplies Claude's web search, based on Brave appearing on Anthropic's published subprocessor list and a `BraveSearchParams` parameter in the web-search tool definition. Anthropic has never officially named a provider, so do not state it as fact to a client. What IS officially documented is `Claude-SearchBot`, so optimize against that rather than against a specific third-party index.

**On Google AI Overviews vs AI Mode:** these are two different surfaces. Google's own guidance says "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary", and ordinary indexable, helpful content is the entry ticket. Both may use a "query fan-out" technique, issuing multiple related searches behind one user query, which is the concrete reason to answer adjacent sub-questions on the same page rather than only the headline one.

**Bot table (2026):**
- `GPTBot`, OpenAI training crawler. Block if you do not want training; allow if you want broader OpenAI presence.
- `OAI-SearchBot`, OpenAI's separate crawler for ChatGPT search results. Allow this even if you block `GPTBot`, otherwise ChatGPT search will not cite you.
- `ChatGPT-User`, fired when a user invokes browsing during a chat. Allow.
- `OAI-AdsBot`, OpenAI's crawler that validates the safety of pages submitted as ads on ChatGPT. Only relevant if you advertise there.
- `PerplexityBot`, the search-index crawler. Allow. It respects robots.txt.
- `Perplexity-User`, the on-demand fetch fired when a user asks a question. Allow. Note Perplexity documents that "Since a user requested the fetch, this fetcher generally ignores robots.txt rules", so disallowing it reduces your odds of being *indexed*, not of being fetched when someone pastes your URL.
- `ClaudeBot`, Anthropic's training crawler. Allow if you want your content usable for training.
- `Claude-SearchBot`, Anthropic's search-index crawler. **Allow this one even if you block `ClaudeBot`**, because it is what makes you eligible to be cited in Claude's search results. Same training-vs-search split as OpenAI's `GPTBot` / `OAI-SearchBot`.
- `Claude-User`, fired when a Claude user asks a question that needs a page. Allow.
- `anthropic-ai` and `Claude-Web` are older names that still circulate in robots.txt examples but appear nowhere in Anthropic's current documentation. Harmless to leave in; not worth adding.
- `Google-Extended`, opt-out token for Gemini/Bard training (does NOT affect Google Search ranking or AI Overview citations).
- `CCBot`, Common Crawl, used by many model trainers downstream.
- `Applebot-Extended`, Apple Intelligence training opt-out.
- `MistralAI-User`, circulated as the on-demand fetcher for Le Chat. We could not find it in Mistral's published docs, so verify before relying on it. Leaving it allowed in robots.txt costs nothing.
- `Meta-ExternalAgent`, Meta's web crawler for Meta AI products. Block via robots.txt if you want to opt out.

**llms.txt status (2026): optional, and NOT a ranking or citation signal.** Do not sell it to a client as one. Google's Search Relations team has said Search does not use llms.txt and has no plans to, and Google's AI-features documentation never mentions it while stating that no additional files or markup are needed for AI Overviews or AI Mode. No AI engine has announced reading it as a ranking input. Ship it if you want cheap protocol-layer registration on the chance the convention wins later, the same shape of bet Schema.org was a decade ago, but ship it AFTER the fundamentals and never instead of them. Place a short `/llms.txt` index per the llmstxt.org spec. A longer companion, commonly named llms-full.txt, is a tooling convention and is not part of that spec. Google Cloud's Open Knowledge Format (OKF, currently v0.2, a directory of Markdown files with YAML frontmatter) is a related emerging convention with the same caveat: nothing crawls the open web for it yet.

**Universal requirements:** allow the search-time bots (`OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `Claude-SearchBot`, `Claude-User`) in robots.txt, keep content server-rendered and indexable, implement Schema markup (Article, Organization with sameAs, FAQPage), include statistics and citations, and keep content genuinely current. llms.txt is explicitly NOT on this list.

See [references/platform-algorithms.md](./references/platform-algorithms.md) for detailed per-platform optimization checklists.

### Step 7: Apply EEAT Principles

Google's E-E-A-T framework (Experience, Expertise, Authoritativeness, Trustworthiness) affects both traditional SEO and AI answer selection.

**Israeli-specific EEAT signals:**
- **Experience:** Include real examples from the Israeli market, case studies with Israeli businesses
- **Expertise:** Author credentials, Hebrew domain expertise, references to Israeli regulations
- **Authoritativeness:** Backlinks from .co.il domains, mentions in Israeli publications (Globes, TheMarker, Calcalist)
- **Trustworthiness:** HTTPS, clear Hebrew authorship, contact info with +972 numbers, privacy policy in Hebrew

For YMYL (Your Money or Your Life) content in Hebrew (medical, financial, legal), ensure content is reviewed by certified Israeli professionals and includes appropriate disclaimers.

See [references/eeat-principles.md](./references/eeat-principles.md) for implementation details.

### Step 8: Build Hebrew Schema.org Structured Data

Create JSON-LD markup optimized for Israeli businesses:

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name / Shem HaEsek",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rehov Example 42",
    "addressLocality": "Tel Aviv-Yafo",
    "addressRegion": "Tel Aviv District",
    "postalCode": "6100000",
    "addressCountry": "IL"
  },
  "telephone": "+972-3-XXX-XXXX",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Sunday","Monday","Tuesday","Wednesday","Thursday"],
      "opens": "09:00",
      "closes": "18:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Friday",
      "opens": "09:00",
      "closes": "14:00"
    }
  ]
}
```

**Israeli-specific considerations:**
1. **Shabbat hours:** Friday closes early (14:00), Saturday closed
2. **Kosher certification:** Use `additionalProperty` with certifying body (Rabbanut, Badatz)
3. **Phone format:** Always use `+972` international prefix
4. **Currency:** Set `priceCurrency` to `ILS`

**GEO-enhanced schemas:** Add `SpeakableSpecification` for voice search and AI extraction:
```json
{
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": ["h1", ".summary", ".faq-answer"]
  }
}
```

See [references/schema-templates.md](./references/schema-templates.md) for complete JSON-LD templates (FAQ, Article, Product, HowTo, Organization, combined @graph patterns).

### Step 9: Configure AI Bot Access and llms.txt

Set up `robots.txt` to allow all major search-time and traditional bots:

```
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# OpenAI: separate bots for training vs search
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

# Perplexity
User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

# Anthropic: three separate bots (training / search index / user fetch)
User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

# Common Crawl (used by many trainers)
User-agent: CCBot
Allow: /

# Mistral (Le Chat web search)
User-agent: MistralAI-User
Allow: /

# Meta AI external agent (opt-out by setting Disallow if you don't want Meta AI presence)
User-agent: Meta-ExternalAgent
Allow: /

Sitemap: https://example.co.il/sitemap.xml
```

**Decisions to make:**
- Allowing search-time crawlers (`OAI-SearchBot`, `Perplexity-User`, `ChatGPT-User`) increases chances of being cited in AI responses.
- Blocking `Google-Extended` opts out of Gemini training without affecting Google Search ranking or AI Overview citations.
- Blocking `GPTBot` opts out of OpenAI model training but keeps you eligible for ChatGPT search if `OAI-SearchBot` and `ChatGPT-User` remain allowed.
- The same split applies at Anthropic: blocking `ClaudeBot` opts out of training while `Claude-SearchBot` keeps you eligible for citation in Claude's search results. Blocking `ClaudeBot` alone is NOT an opt-out of Claude entirely, and blocking all three is.
- Review your policy regularly. This landscape evolves rapidly.

**Optionally add `/llms.txt`:** llms.txt (proposed by Jeremy Howard, 2024) is a convention, not a standard, and carries no confirmed ranking or citation effect. Place a short markdown file at `https://example.co.il/llms.txt` summarizing the site's purpose and key URLs if you want to register early. Do NOT let it displace server-rendered HTML, Schema.org, or a correct robots.txt, and do not report it to a client as an AI-visibility win.

### Step 10: Validate and Monitor

**SEO Validation:**
```bash
# Schema validation
open "https://search.google.com/test/rich-results?url={encoded_url}"

# Check Google indexing
open "https://www.google.com/search?q=site:{domain}"

# Check Bing indexing (required for Copilot)
open "https://www.bing.com/search?q=site:{domain}"
```

**GEO Monitoring: measure in four layers, in order.** GEO outcomes are delayed (an engine has to re-crawl before your edit can surface) and confounded (your number also moves when the engine or a competitor changes). So separate the fast proxy from the slow outcome instead of reading a raw before/after.

| Layer | Question | Latency | Proxy or outcome |
|-------|----------|---------|------------------|
| 1. Crawler access | Can the bots fetch and parse the page at all? | Instant | Precondition |
| 2. Citability | Given the page, is it extractable and answer-shaped? | Minutes | Proxy |
| 3. Surfacing | Does an engine cite you for a bare query, unprompted? | Days to weeks | Outcome (GEO) |
| 4. Rankings and clicks | Position, impressions, CTR | Weeks to months | Outcome (SEO) |

**Always check layer 1 before concluding anything about content quality.** "Not crawled yet" and "crawled but not chosen" look identical in the answer box and have completely different fixes. Diagnosing a content problem when the real cause is a blocked `Claude-SearchBot` wastes weeks.

1. **Layer 1:** request the page as each bot user agent, confirm a 200 AND that the content is in the raw HTML rather than JS-injected. Evaluate robots.txt per user agent, not in aggregate. Check your own access logs for real bot hits per URL.
2. **Layer 2:** hand a specific URL to an engine and ask the target question. This bypasses crawl lag on live-fetch paths, so it iterates in minutes, but it only proves extractability, not that you will be chosen.
3. **Layer 3:** ask a FIXED panel of queries WITHOUT supplying the URL, and record citations over time against a control page you did not edit. This is the actual GEO outcome.
4. **Layer 4:** Search Console and rank data, snapshotted over time against the same control.

**Google Search Console generative AI reports:** Google launched dedicated Search Generative AI performance reports on 3 June 2026, covering AI Overviews, AI Mode, and generative AI features in Discover. They report **Impressions, Pages, Countries, Devices and Dates only**. There is no click, CTR, position, or query data in this version, and Google is rolling the reports out to a subset of websites rather than everyone, so do not promise a client this data until you have confirmed their property has it. Generative-AI traffic also continues to be counted inside the overall performance report.

Third-party AI-citation trackers (Otterly.ai, Profound, SE Ranking AI Toolkit) automate layer 3. Also watch referral traffic from AI platforms and check citation accuracy by searching your brand in each assistant.

**Hebrew-specific checks:**
1. Verify RTL rendering in all browsers
2. Test hreflang bidirectional linking
3. Confirm local directory listings are consistent (NAP: Name, Address, Phone)
4. Run `scripts/analyze_keywords.py --audit` for keyword coverage

See [references/tools-and-apis.md](./references/tools-and-apis.md) for a full list of free and paid SEO/GEO tools.

## Examples

### Example 1: Hebrew Keyword Research
User says: "I need keywords for an Israeli real estate website"
Actions:
1. Identify root keywords: nadlan (real estate), dira (apartment), bayit (house)
2. Generate morphological variants: hanadlan, benadlan, dirot (plural), batim (plural)
3. Include construct forms: sokhen nadlan (real estate agent), mehirei dirot (apartment prices)
4. Run `scripts/analyze_keywords.py --keywords "nadlan,dira,bayit"` for full variant analysis
5. Map variants to pages with search volume priority
Result: Complete Hebrew keyword map with morphological variants and prefix combinations

### Example 2: Bilingual Site hreflang Setup
User says: "Set up hreflang for my Hebrew/English .co.il site"
Actions:
1. Audit existing pages for language pairs
2. Generate hreflang link tags for HTML head on each page
3. Create XML sitemap with hreflang annotations
4. Verify bidirectional linking between language versions
Result: Complete hreflang implementation with he-IL and en targeting

### Example 3: GEO Optimization for Israeli SaaS
User says: "Optimize my Israeli SaaS landing page for AI search engines"
Actions:
1. Audit current AI visibility (search brand name in ChatGPT, Perplexity, Claude)
2. Apply Princeton GEO methods: add statistics with sources, expert quotes, authoritative citations
3. Implement FAQPage schema with bilingual Q&A pairs
4. Add SpeakableSpecification to key content sections
5. Verify all AI bots are allowed in robots.txt
6. Structure content in answer-first format with clear H2/H3 hierarchy
Result: Landing page optimized for both Google.co.il and AI search engine citations

### Example 4: Israeli Restaurant Schema with GEO
User says: "Create structured data for my kosher restaurant in Jerusalem"
Actions:
1. Build LocalBusiness/Restaurant JSON-LD with Israeli address format
2. Add Shabbat-aware opening hours (Friday early close, Saturday closed)
3. Include kosher certification with Rabbanut details
4. Add FAQPage schema for common questions (menu, reservations, kashrut level)
5. Add SpeakableSpecification for voice assistant queries
6. Include Hebrew menu schema with NIS pricing
Result: Complete JSON-LD markup optimized for Google Rich Results and AI citations

### Example 5: Full SEO + GEO Audit
User says: "Audit my Israeli e-commerce site for SEO and AI visibility"
Actions:
1. Run `python3 scripts/seo_audit.py "https://example.co.il"` for technical audit
2. Check AI bot access in robots.txt
3. Verify hreflang and Hebrew content quality
4. Audit structured data (FAQPage, Product, BreadcrumbList schemas)
5. Evaluate EEAT signals (author credentials, citations, Hebrew expertise)
6. Test AI visibility by searching brand and product names in ChatGPT, Perplexity, Claude
7. Review Google Search Console AI Overview data
Result: Prioritized SEO + GEO improvement plan for the Israeli market

## Bundled Resources

### Scripts
- `scripts/seo_audit.py` -- Full website SEO audit: meta tags, robots.txt, sitemap, load time, schema markup, AI bot access. No API needed. Run: `python3 scripts/seo_audit.py "https://example.co.il"`
- `scripts/analyze_keywords.py` -- Hebrew keyword morphological analysis: generates prefix variants (ha-, ve-, be-, le-, me-, she-), plural forms, and construct state combinations. Run: `python scripts/analyze_keywords.py --help`
- `scripts/keyword_research.py` -- Keyword research with search volume and difficulty data. Requires DataForSEO API. Run: `python3 scripts/keyword_research.py "seo tools" --limit 20`
- `scripts/serp_analysis.py` -- Analyze top Google results for a keyword. Requires DataForSEO API. Run: `python3 scripts/serp_analysis.py "best seo tools"`
- `scripts/backlinks.py` -- Backlink profile analysis. Requires DataForSEO API. Run: `python3 scripts/backlinks.py "example.com"`
- `scripts/domain_overview.py` -- Domain metrics: traffic, keywords, rankings. Requires DataForSEO API. Run: `python3 scripts/domain_overview.py "example.com"`
- `scripts/autocomplete_ideas.py` -- Google autocomplete keyword suggestions. Requires DataForSEO API.
- `scripts/related_keywords.py` -- Related keyword discovery. Requires DataForSEO API.
- `scripts/competitor_gap.py` -- Competitor keyword gap analysis. Requires DataForSEO API.

### References
- `references/hebrew-seo.md` -- Hebrew SEO best practices: .co.il domain strategy, RTL optimization, Israeli business directories, Google.co.il ranking factors. Consult when implementing or auditing Hebrew SEO.
- `references/geo-research.md` -- Princeton GEO research (9 optimization methods with examples, best combinations, domain-specific recommendations). Consult when optimizing content for AI search engine citations.
- `references/platform-algorithms.md` -- Detailed ranking factors for each AI platform (ChatGPT, Perplexity, Google AI Overview, Copilot, Claude) and traditional Google SEO. Consult when optimizing for a specific search platform.
- `references/schema-templates.md` -- Ready-to-use JSON-LD templates: FAQPage, WebPage, Article, SoftwareApplication, Organization, Product, HowTo, BreadcrumbList, LocalBusiness, SpeakableSpecification, combined @graph patterns. Consult when implementing structured data.
- `references/seo-checklist.md` -- Complete prioritized SEO/GEO audit checklist (P0/P1/P2 priorities) covering technical SEO, on-page SEO, schema markup, GEO optimization, off-page SEO, and monitoring. Consult when running a full site audit.
- `references/tools-and-apis.md` -- Curated list of free and paid SEO/GEO tools, APIs, browser extensions, and command-line utilities. Consult when recommending tools or setting up automation.
- `references/eeat-principles.md` -- Google's EEAT framework (Experience, Expertise, Authoritativeness, Trustworthiness) with implementation patterns and YMYL considerations. Consult when evaluating or improving content quality.
- `references/aeo-considerations.md` -- Answer Engine Optimization (AEO) guide: how AI selects answers, content structure for AI, Google AI Overviews, AI crawler management, measuring AEO success. Consult when optimizing content for AI answer selection.

## Gotchas

- Hebrew morphology creates keyword variants that agents miss. The word "nadlan" (real estate) has prefixes like "hanadlan," "benadlan," "lenadlan" that are separate search queries. Agents may optimize for a single form and miss the majority of search traffic.
- Israeli business hours in schema.org must reflect the Sunday-Thursday work week with Friday early close. Agents default to Monday-Friday schedules.
- The hreflang tag for Israeli Hebrew must be `he-IL`, not just `he`. Agents often omit the country code, which affects Google's geo-targeting for google.co.il.
- Israeli phone numbers in structured data must use the `+972` prefix. Agents may format numbers in local 0X-XXX-XXXX format, which fails schema validation.
- GEO (Generative Engine Optimization) is a rapidly evolving field. AI platform ranking factors (which bots to allow, content freshness windows, citation formats) change frequently. Agents may recommend outdated GEO strategies from even 6 months ago. Google lists AI Overviews as available to all users in Israel and in Hebrew, but it does not appear on every query; treat AI Overview citation as an aspirational signal rather than a guaranteed lever.
- AI Overview de-prioritizes content with stuffed H1/H2 keywords. Sites that rank well in classic Google can lose AI Overview citations to lower-traffic competitors that have a cleaner answer-first paragraph. The fix is structural (rewrite intro for direct-answer format), not more keywords.
- Hebrew-language LLMs cite Hebrew content unevenly. Pure-Hebrew SaaS landing pages get cited less by ChatGPT/Claude than equivalent EN+HE pages. Maintain an English alternate URL with the same content for the AI surface, plus the Hebrew URL with proper hreflang for Google.co.il ranking.


## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Google Search Central | https://developers.google.com/search | Ranking factors, structured data, Core Web Vitals |
| Google Search Status Dashboard | https://status.search.google.com | Active core updates, AI Overview rollout status |
| Schema.org | https://schema.org | JSON-LD markup for LocalBusiness, FAQ, Article |
| Google Keyword Planner | https://ads.google.com/intl/en/home/tools/keyword-planner/ | Hebrew search volumes, keyword ideas |
| Academy of the Hebrew Language | https://hebrew-academy.org.il | Correct Hebrew terminology, spelling rules |
| Princeton GEO paper (Aggarwal et al., 2023) | https://arxiv.org/abs/2311.09735 | GEO methods for AI search engines |
| OpenAI bot docs | https://developers.openai.com/api/docs/bots | `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `OAI-AdsBot` behavior |
| Anthropic crawler docs | https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler | `ClaudeBot`, `Claude-SearchBot`, `Claude-User` and how to block each |
| Perplexity crawler info | https://docs.perplexity.ai/docs/resources/perplexity-crawlers | `PerplexityBot`, `Perplexity-User`, and which one ignores robots.txt |
| Google AI features guidance | https://developers.google.com/search/docs/appearance/ai-features | What is and is not required for AI Overviews and AI Mode |
| Search Console generative AI reports | https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports | Which metrics the AI reports actually expose |
| llms.txt proposal | https://llmstxt.org | Convention for AI-readable site index |
| Bing Webmaster Tools AI Performance | https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview | AI Performance reporting shows when Copilot cites you |
| Brave Search | https://brave.com/search/ | Independent index Claude relies on |

## Troubleshooting

### Error: "hreflang mismatch detected"
Cause: hreflang tags are not bidirectional (page A links to B but B does not link back to A)
Solution: Ensure every hreflang declaration is reciprocal. Both the Hebrew and English versions must reference each other.

### Error: "RTL rendering issues"
Cause: Missing dir="rtl" attribute or CSS conflicts with LTR defaults
Solution: Set dir="rtl" on the html element for Hebrew pages. Use CSS logical properties (margin-inline-start instead of margin-left).

### Error: "Schema validation failed"
Cause: JSON-LD markup contains errors or missing required properties
Solution: Test with Google Rich Results Test. Common Israeli issues: wrong phone format (must use +972), missing addressCountry: IL, or ILS currency code.

### Error: "Keywords not ranking on google.co.il"
Cause: Content may be machine-translated or missing morphological keyword variants
Solution: Ensure Hebrew content includes natural prefix combinations. Use `scripts/analyze_keywords.py` to identify missing variants.

### Error: "Not appearing in AI search results"
Cause: diagnose in order, because these look identical from the outside and have different fixes. (1) the search-time bot cannot fetch the page at all; (2) it fetched, but the content is JS-injected and not in the raw HTML; (3) it parsed fine but the content is not answer-shaped enough to be chosen.
Solution: Check (1) FIRST by requesting the page as each bot user agent and confirming a 200 with the text present in the raw HTML. Confirm robots.txt allows `OAI-SearchBot`, `PerplexityBot`, and `Claude-SearchBot` specifically. Allowing only `GPTBot` and `ClaudeBot` covers training crawlers and leaves you ineligible for search citations on both platforms, which is the most common version of this bug. Only after access is green, apply GEO methods (quotes, statistics, citations) and restructure to answer-first.

### Error: "AI citing competitors instead of my site"
Cause: Competitor content has higher factual density, better structure, or more authoritative citations
Solution: Apply the Princeton GEO methods in the order the paper found effective: expert quotes with attribution first, then specific statistics with sources, then fluency and citations. Use answer-first format and FAQPage schema. Build topical authority through content clusters.
