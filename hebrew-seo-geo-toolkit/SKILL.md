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

**Verify AI bot access in robots.txt:** Googlebot, Bingbot, PerplexityBot, ChatGPT-User, ClaudeBot, anthropic-ai, GPTBot must all be allowed. See [references/seo-checklist.md](./references/seo-checklist.md) for the full prioritized audit checklist.

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

| Method | Visibility Boost | How to Apply |
|--------|-----------------|--------------|
| **Cite Sources** | +40% | Add authoritative citations and references |
| **Statistics Addition** | +37% | Include specific numbers and data points |
| **Quotation Addition** | +30% | Add expert quotes with attribution |
| **Authoritative Tone** | +25% | Use confident, expert language |
| **Easy-to-understand** | +20% | Simplify complex concepts |
| **Technical Terms** | +18% | Include domain-specific terminology |
| **Unique Words** | +15% | Increase vocabulary diversity |
| **Fluency Optimization** | +15-30% | Improve readability and flow |
| ~~Keyword Stuffing~~ | **-10%** | **AVOID: hurts AI visibility** |

**Best combination:** Fluency + Statistics = Maximum boost

**Content structure for AI extraction:**
- Use "answer-first" format (direct answer at top of each section)
- Clear H1 > H2 > H3 hierarchy
- Bullet points, numbered lists, tables for comparison data
- Short paragraphs (2-3 sentences max)
- FAQ format for common questions

**FAQPage Schema (+40% AI visibility):**
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
| ChatGPT (search) | Own crawler (`OAI-SearchBot`) + Bing fallback | Domain authority + content-answer fit | Allow `OAI-SearchBot` separately from `GPTBot` (training); 30-day freshness |
| Perplexity | Own crawler (`PerplexityBot`) + Google fallback | Semantic relevance | FAQ Schema, structured data, PDF/markdown sources |
| Google AI Overview | Google index | E-E-A-T + Knowledge Graph | Hebrew AI Overview rolled out to google.co.il during 2024-2025; structured data and clear answer paragraphs help |
| Gemini (Google) | Google index + real-time web | E-E-A-T + recency | Same as Google Search; benefits from llms.txt and clean markdown |
| Copilot (Microsoft) | Bing index | Bing rank + MS ecosystem signals | Bing Webmaster Tools verified, LinkedIn/GitHub presence |
| Claude (with web search) | Brave Search index | Factual density + citations | Brave indexing + clean source URLs |

**Bot table (2026):**
- `GPTBot`, OpenAI training crawler. Block if you do not want training; allow if you want broader OpenAI presence.
- `OAI-SearchBot`, OpenAI's separate crawler for ChatGPT search results. Allow this even if you block `GPTBot`, otherwise ChatGPT search will not cite you.
- `ChatGPT-User`, fired when a user invokes browsing during a chat. Allow.
- `PerplexityBot` and `Perplexity-User`, index + on-demand fetch. Allow both.
- `ClaudeBot`, `anthropic-ai`, `Claude-Web`, Anthropic crawlers. Allow.
- `Google-Extended`, opt-out token for Gemini/Bard training (does NOT affect Google Search ranking or AI Overview citations).
- `CCBot`, Common Crawl, used by many model trainers downstream.
- `Applebot-Extended`, Apple Intelligence training opt-out.

**Universal requirements:** allow the search-time bots (`OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `ClaudeBot`) in robots.txt, implement Schema markup (FAQPage, Article, Organization with sameAs), include statistics and citations, update content within 30 days, expose a clean `/llms.txt` and `/llms-full.txt` for AI consumption.

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

# Anthropic
User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Claude-Web
Allow: /

# Common Crawl (used by many trainers)
User-agent: CCBot
Allow: /

Sitemap: https://example.co.il/sitemap.xml
```

**Decisions to make:**
- Allowing search-time crawlers (`OAI-SearchBot`, `Perplexity-User`, `ChatGPT-User`) increases chances of being cited in AI responses.
- Blocking `Google-Extended` opts out of Gemini training without affecting Google Search ranking or AI Overview citations.
- Blocking `GPTBot` opts out of OpenAI model training but keeps you eligible for ChatGPT search if `OAI-SearchBot` and `ChatGPT-User` remain allowed.
- Review your policy regularly. This landscape evolves rapidly.

**Add `/llms.txt` and `/llms-full.txt`:** llms.txt (proposed by Jeremy Howard, 2024) is becoming a de facto AI-readable index. Place a short markdown file at `https://example.co.il/llms.txt` summarizing the site's purpose and key URLs, plus a longer `llms-full.txt` with the full content. AI search crawlers and agents increasingly use these instead of guessing structure from HTML.

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

**GEO Monitoring:**
- Track AI citations using tools like Otterly.ai, Profound, or SE Ranking AI Toolkit
- Monitor referral traffic from AI platforms (Perplexity, ChatGPT)
- Search for your brand in AI assistants to check citation accuracy
- Track Google Search Console AI Overview data

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
- GEO (Generative Engine Optimization) is a rapidly evolving field. AI platform ranking factors (which bots to allow, content freshness windows, citation formats) change frequently. Agents may recommend outdated GEO strategies from even 6 months ago.


## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Google Search Central | https://developers.google.com/search | Ranking factors, structured data, Core Web Vitals |
| Google Search Status Dashboard | https://status.search.google.com | Active core updates, AI Overview rollout status |
| Schema.org | https://schema.org | JSON-LD markup for LocalBusiness, FAQ, Article |
| Google Keyword Planner | https://ads.google.com/home/tools/keyword-planner/ | Hebrew search volumes, keyword ideas |
| Academy of the Hebrew Language | https://hebrew-academy.org.il | Correct Hebrew terminology, spelling rules |
| Princeton GEO paper (Aggarwal et al., 2023) | https://arxiv.org/abs/2311.09735 | GEO methods for AI search engines |
| OpenAI bot docs | https://platform.openai.com/docs/bots | `GPTBot`, `OAI-SearchBot`, `ChatGPT-User` behavior |
| Anthropic crawler docs | https://docs.anthropic.com/en/docs/agents-and-tools/web-crawler | `ClaudeBot`, `anthropic-ai`, `Claude-Web` |
| Perplexity crawler info | https://docs.perplexity.ai/guides/bots | `PerplexityBot`, `Perplexity-User` |
| llms.txt proposal | https://llmstxt.org | Convention for AI-readable site index |
| Bing Webmaster Tools | https://www.bing.com/webmasters | Required for Copilot indexing |
| Brave Search | https://search.brave.com | Index Claude relies on |

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
Cause: AI bots may be blocked, content lacks citation-worthy signals, or site not indexed on required platforms
Solution: Check robots.txt allows GPTBot, PerplexityBot, ClaudeBot. Apply GEO methods (citations, statistics, authoritative tone). Verify Bing indexing (for Copilot) and Brave indexing (for Claude). Ensure content is updated within 30 days.

### Error: "AI citing competitors instead of my site"
Cause: Competitor content has higher factual density, better structure, or more authoritative citations
Solution: Apply Princeton GEO methods: add specific statistics with sources (+37%), authoritative citations (+40%), expert quotes (+30%). Use answer-first format and FAQPage schema. Build topical authority through content clusters.
