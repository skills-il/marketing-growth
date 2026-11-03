# SEO/GEO Tools and API Reference

Curated list of tools and APIs for SEO and GEO optimization.

---

## Free Tools

### Schema Markup Generators

| Tool | URL | Features |
|------|-----|----------|
| **TechnicalSEO.com** | technicalseo.com/tools/schema-markup-generator | Multiple schema types, validation |
| **Rank Ranger** | rankranger.com/schema-markup-generator | FAQ, Article, Product schemas |
| **Merkle** | technicalseo.com/tools/schema-markup-generator | Comprehensive schema generator |
| **JSON-LD Generator** | jsonld.com | Simple schema builder |

### Validation Tools

| Tool | URL | Purpose |
|------|-----|---------|
| **Google Rich Results Test** | search.google.com/test/rich-results | Test schema markup |
| **Schema.org Validator** | validator.schema.org | Validate any schema |
| **PageSpeed Insights** | pagespeed.web.dev | Core Web Vitals |

### SEO Audit Tools

| Tool | URL | Features |
|------|-----|----------|
| **SEOmator** | seomator.com/free-seo-audit-tool | Comprehensive free audit |
| **Screaming Frog (Free)** | screamingfrog.co.uk | Crawl up to 500 URLs |
| **Google Search Console** | search.google.com/search-console | Official Google data |
| **Bing Webmaster Tools** | bing.com/webmasters | Bing indexing data |

---

## Paid SEO Tools

### Comprehensive Platforms

| Tool | Price | Best For |
|------|-------|----------|
| **Ahrefs** | Paid subscription | Backlink analysis, keyword research |
| **Semrush** | Paid subscription | All-in-one SEO + GEO toolkit |
| **Moz Pro** | Paid subscription | Domain authority, link building |
| **SE Ranking** | Paid subscription | Affordable all-in-one |

### Content Optimization

| Tool | Price | Best For |
|------|-------|----------|
| **Surfer SEO** | Paid subscription | Content optimization for AI |
| **Clearscope** | Paid subscription | Enterprise content optimization |
| **Frase** | Paid subscription | AI content briefs |
| **MarketMuse** | Paid subscription | Content strategy |

---

## GEO / AI Visibility Tools

### AI Search Monitoring

| Tool | Price | Platforms |
|------|-------|-----------|
| **Profound** | Paid subscription | ChatGPT, Perplexity, Claude, Gemini |
| **Otterly.ai** | Free trial | ChatGPT, Perplexity, Google AIO |
| **SE Ranking AI Toolkit** | Included | AI Overviews, ChatGPT |
| **Semrush AI Visibility** | Included | Google AIO, ChatGPT |
| **Peec AI** | Mid-tier | Sentiment + visibility |
| **Scrunch AI** | Varies | Brand tracking, citations |

### AI Visibility Features to Look For

- Citation tracking across AI platforms
- Prompt-level insights
- Source attribution
- Sentiment analysis
- Competitive benchmarking
- Actionable recommendations

---

## APIs for Automation

### Google APIs

| API | Purpose | Docs |
|-----|---------|------|
| **Search Console API** | Indexing status, search data | developers.google.com/webmaster-tools |
| **PageSpeed API** | Core Web Vitals data | developers.google.com/speed/docs/insights/v5/get-started |
| **Indexing API** | Request indexing | developers.google.com/search/apis/indexing-api |
| **Custom Search API** | Programmatic search | developers.google.com/custom-search |

### SEO Data APIs

| API | Purpose | Pricing |
|-----|---------|---------|
| **DataForSEO** | Comprehensive SEO data | Pay-as-you-go, $50 minimum top-up, $1 trial credit |
| **Moz API** | DA, PA, link data | Included with Moz |
| **Ahrefs API** | Backlinks, keywords | Included with Ahrefs |
| **SE Ranking API** | Rankings, audits | Included with SE Ranking |
| **SEO Review Tools API** | Various SEO checks | Free tier available |

### Schema/Metadata APIs

| API | Purpose | Pricing |
|-----|---------|---------|
| **Apify Metadata Extractor** | Extract meta, sitemap, robots | Paid subscription |
| **Firecrawl** | Website crawling for SEO | Pay-per-use |

---

## Browser Extensions

### SEO Analysis

| Extension | Browser | Features |
|-----------|---------|----------|
| **SEOquake** | Chrome/Firefox | Quick SEO metrics |
| **MozBar** | Chrome | DA, PA, link data |
| **Ahrefs SEO Toolbar** | Chrome | Backlinks, keywords |
| **Detailed SEO Extension** | Chrome | Technical SEO checks |

### Schema Testing

| Extension | Browser | Features |
|-----------|---------|----------|
| **Structured Data Testing Tool** | Chrome | View page schema |
| **Schema Builder** | Chrome | Generate schema |

---

## Command Line Tools

### curl Commands for SEO Checks

```bash
# Check meta tags
curl -sL "https://example.com" | grep -E "<title>|<meta"

# Check robots.txt
curl -s "https://example.com/robots.txt"

# Check sitemap
curl -s "https://example.com/sitemap.xml"

# Check HTTP headers
curl -I "https://example.com"

# Check redirect chain
curl -sIL "https://example.com" | grep -E "HTTP|Location"

# Check page size
curl -sL "https://example.com" | wc -c

# Check load time
curl -o /dev/null -s -w "Total: %{time_total}s\n" "https://example.com"
```

### Using Google APIs via curl

```bash
# PageSpeed Insights (no API key needed for basic)
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com"

# With API key (more requests allowed)
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&key=YOUR_API_KEY"
```

---

## Robots.txt Template for AI Bots

```
# Search Engines
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# AI bots: search-index crawlers first, these govern citation eligibility
User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

# Live, user-triggered fetchers
User-agent: ChatGPT-User
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Perplexity-User
Allow: /

# Training crawlers, decide deliberately
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Applebot-Extended
Allow: /

# Sitemap
Sitemap: https://example.com/sitemap.xml
```

---

## Scripts

Ready-to-use Python scripts in the `scripts/` folder. List prices change; check each vendor's pricing page before quoting one to a client.

### Free scripts

```bash
# Single-page SEO + GEO audit ending in a P0/P1/P2 fix list
python3 scripts/seo_audit.py "https://example.co.il"
python3 scripts/seo_audit.py "https://example.co.il" --json

# Hebrew prefix and spelling variants, and coverage against a Search Console Queries export
python3 scripts/analyze_keywords.py --keywords 'נדל"ן,דירה להשכרה'
python3 scripts/analyze_keywords.py --keywords 'נדל"ן' --gsc-queries Queries.csv
```

If `seo_audit.py` exits 2 with a TLS error, the local Python lacks current root certificates: run its "Install Certificates" step or set `SSL_CERT_FILE` to a current CA bundle.

### DataForSEO scripts (paid)

Set credentials as environment variables, never as arguments. Use the API password from the DataForSEO dashboard (it differs from the account password):

```bash
export DATAFORSEO_LOGIN=your_api_login
export DATAFORSEO_PASSWORD=your_api_password
export DATAFORSEO_SANDBOX=1   # optional: free sandbox, dummy data, real response shape
```

Every script defaults to Israel (`--location 2376`) and Hebrew (`--language he`). The Labs scripts (`related_keywords.py`, `competitor_gap.py`, `domain_overview.py`) refuse English for Israel, because DataForSEO Labs holds only Hebrew and Arabic data for Israel. Google Ads endpoints allow 12 requests per minute per account.

```bash
python3 scripts/keyword_research.py 'נדל"ן,דירה להשכרה' --limit 20   # Google Ads volume + paid-search competition
python3 scripts/related_keywords.py 'ביטוח רכב' --depth 1 --limit 50   # Labs: volume + organic difficulty 0-100
python3 scripts/autocomplete_ideas.py 'הנהלת חשבונות'                   # Google autocomplete
python3 scripts/serp_analysis.py 'רואה חשבון בתל אביב' --depth 10        # top organic results (billed per 10)
python3 scripts/competitor_gap.py my-site.co.il competitor.co.il       # keywords the competitor ranks for and you do not
python3 scripts/domain_overview.py example.co.il                        # organic keyword count and estimated traffic
python3 scripts/backlinks.py example.co.il --limit 20                   # backlinks, rank on a 0-1000 scale
```

---

## Workflow Integration

### Automation Ideas

1. **Recurring audit** - run `seo_audit.py --json` on key pages after each deploy and diff the findings
2. **Schema monitoring** - validate structured data after deploys with the Rich Results Test
3. **AI visibility tracking** - run a fixed query panel by hand, or with Otterly.ai or Profound
4. **Content freshness** - flag pages whose dateModified is old relative to their topic
5. **Competitor monitoring** - re-run `competitor_gap.py` monthly

---

## Resources

### Learning

| Resource | URL | Type |
|----------|-----|------|
| **Google SEO Guide** | developers.google.com/search/docs | Official |
| **Moz Beginner's Guide** | moz.com/beginners-guide-to-seo | Tutorial |
| **Backlinko** | backlinko.com/hub/seo | Advanced |
| **Search Engine Journal** | searchenginejournal.com | News |

### GEO Research

| Resource | URL | Type |
|----------|-----|------|
| **Princeton GEO Paper** | arxiv.org/abs/2311.09735 | Research |
| **GEO Guide (SingleGrain)** | singlegrain.com/geo | Guide |
| **AI Search Optimization (Semrush)** | semrush.com/blog/ai-search-optimization | Tutorial |

### Communities

| Community | Platform | Focus |
|-----------|----------|-------|
| **r/SEO** | Reddit | General SEO |
| **r/bigseo** | Reddit | Advanced SEO |
| **r/TechSEO** | Reddit | Technical SEO |
| **SEO Twitter** | Twitter | News, tips |
