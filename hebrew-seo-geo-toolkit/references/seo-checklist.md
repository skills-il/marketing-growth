# SEO/GEO Audit Checklist

Complete checklist for auditing and optimizing websites for both traditional SEO and GEO (AI search visibility).

## Priority Levels

| Level | Meaning | Action |
|-------|---------|--------|
| **P0** | Critical | Must fix immediately - blocks indexing or causes major issues |
| **P1** | Important | Should fix soon - significant impact on rankings |
| **P2** | Recommended | Nice to have - improves visibility and user experience |

---

## Technical SEO

### P0 - Critical

- [ ] **P0** `robots.txt` allows important pages
- [ ] **P0** Site is accessible (no 5xx errors)
- [ ] **P0** HTTPS enabled (valid SSL certificate)
- [ ] **P0** Mobile-responsive design
- [ ] **P0** No critical pages blocked by `noindex` (meta robots or `X-Robots-Tag`)
- [ ] **P0** Search generative AI control in Search Console left on (required for AI Overviews and AI Mode eligibility)
- [ ] **P0** CDN / firewall does not refuse the search-index AI crawlers (check with `seo_audit.py`)
- [ ] **P0** Site is indexed in Google (check: `site:domain.com`)
- [ ] **P0** `robots.txt` allows the SEARCH-INDEX AI bots (`OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`). These govern citation eligibility and are the ones most often missing
- [ ] **P0** Search Console Manual actions and Security issues reports are empty (any entry outranks everything else)
- [ ] **P0** No unintended `nosnippet` or `max-snippet:0` (these limit what Google Search and its AI features can show)

### P1 - Important

- [ ] **P1** `robots.txt` allows the training crawlers you are happy with (`GPTBot`, `ClaudeBot`) and the live fetchers (`ChatGPT-User`, `Claude-User`, `Perplexity-User`)
- [ ] **P1** XML sitemap exists and is submitted
- [ ] **P1** Site is indexed in Bing (for Copilot visibility)
- [ ] **P1** Canonical tags properly implemented
- [ ] **P1** No duplicate content issues
- [ ] **P1** LCP (Largest Contentful Paint) < 2.5s
- [ ] **P1** INP (Interaction to Next Paint) 200 ms or less (INP replaced FID)

### P2 - Recommended

- [ ] **P2** CLS (Cumulative Layout Shift) < 0.1
- [ ] **P2** Images optimized (WebP format, lazy loading)
- [ ] **P2** CSS/JS minified
- [ ] **P2** GZIP/Brotli compression enabled
- [ ] **P2** CDN configured
- [ ] **P2** Pages render and read well on a phone (Google retired its Mobile-Friendly Test; use Lighthouse or PageSpeed Insights)
- [ ] **P2** No mixed content warnings
- [ ] **P2** Secure headers configured

---

## On-Page SEO

### P0 - Critical

- [ ] **P0** Unique `<title>` tag exists (Google truncates by pixel width, so keep the key words first)

### P1 - Important

- [ ] **P1** Title states what the page is about, in the words searchers use
- [ ] **P1** Unique `<meta description>` that summarizes the page (Google publishes no length rule)
- [ ] **P1** A clear main heading that states the page topic
- [ ] **P1** Description is compelling and includes keyword
- [ ] **P1** `<meta name="robots">` correctly set
- [ ] **P1** Logical heading hierarchy (H1 > H2 > H3)
- [ ] **P1** All images have `alt` attributes
- [ ] **P1** Internal links to related content
- [ ] **P1** No broken links (404s)
- [ ] **P1** Anchor text is descriptive

### P2 - Recommended

- [ ] **P2** `og:title` set
- [ ] **P2** `og:description` set
- [ ] **P2** `og:image` set (1200x630px recommended)
- [ ] **P2** `og:url` set (canonical URL)
- [ ] **P2** `og:type` set (website/article)
- [ ] **P2** `twitter:card` set (summary_large_image)
- [ ] **P2** `twitter:title` set
- [ ] **P2** `twitter:description` set
- [ ] **P2** `twitter:image` set
- [ ] **P2** Short, scannable paragraphs (practice, not a Google rule)
- [ ] **P2** Bullet points used for lists
- [ ] **P2** Tables used for comparisons
- [ ] **P2** Alt text includes keywords where natural
- [ ] **P2** Image file names are descriptive

---

## Schema Markup (Structured Data)

### P1 - Important

- [ ] **P1** Organization schema on homepage
- [ ] **P1** LocalBusiness or Product schema where it applies
- [ ] **P1** Article schema on blog posts
- [ ] **P1** Schema passes Google Rich Results Test
- [ ] **P1** No errors in Search Console "Enhancements"

### P2 - Recommended - GEO Enhanced

- [ ] **P2** FAQPage schema only if a consumer other than Google uses it (Google stopped showing FAQ rich results on 7 May 2026)
- [ ] **P2** BreadcrumbList schema for navigation
- [ ] **P2** LocalBusiness `specialOpeningHoursSpecification` for Israeli holidays
- [ ] **P2** datePublished and dateModified included
- [ ] **P2** Author information with credentials
- [ ] **P2** Publisher information with logo
- [ ] **P2** Schema passes Schema.org Validator

---

## GEO Optimization (AI Search)

### P1 - Important - Princeton GEO Methods

- [ ] **P1** Content includes authoritative citations
- [ ] **P1** Statistics and data points included (one of the two strongest GEO methods)
- [ ] **P1** Expert quotes with attribution (the strongest GEO method in the paper)
- [ ] **P1** NO keyword stuffing (below baseline on the paper's word-count metric, and a Google spam-policy violation)
- [ ] **P1** Every statistic and quote has a real, linkable source (never invented)

### P2 - Recommended - GEO Enhancement

- [ ] **P2** Authoritative, confident tone
- [ ] **P2** Content is accessible/easy to understand
- [ ] **P2** Appropriate technical terminology
- [ ] **P2** Diverse vocabulary throughout (least effective of the nine)
- [ ] **P2** High fluency and readability

### Content Structure for AI

- [ ] "Answer-first" format (direct answer at top)
- [ ] Clear, extractable paragraphs
- [ ] FAQ format for common questions
- [ ] Tables for comparison data
- [ ] Lists for step-by-step processes

### AI Bot Access

- [ ] `OAI-SearchBot` allowed in robots.txt (ChatGPT search citations)
- [ ] `Claude-SearchBot` allowed in robots.txt (Claude search citations)
- [ ] `PerplexityBot` allowed in robots.txt (Perplexity indexing)
- [ ] `ChatGPT-User`, `Claude-User`, `Perplexity-User` allowed (live user-triggered fetches)
- [ ] `GPTBot` and `ClaudeBot` decided deliberately (training opt-in or opt-out; blocking these does NOT block search citations)
- [ ] Bingbot allowed in robots.txt (required for Copilot)

---

## Off-Page SEO

### Backlinks

- [ ] Quality backlinks from relevant sites
- [ ] Diverse referring domains
- [ ] No toxic/spammy backlinks
- [ ] Brand mentions (even without links)

### E-E-A-T Signals

- [ ] Author bios with credentials
- [ ] About page with company info
- [ ] Contact information visible
- [ ] Privacy policy and terms
- [ ] Trust badges/certifications if applicable
- [ ] Customer reviews/testimonials

---

## Content Strategy

### Content Audit

- [ ] All pages have unique, valuable content
- [ ] No thin pages that add nothing beyond other pages (Google sets no word count)
- [ ] Content matches search intent
- [ ] Content is genuinely up-to-date (fast-moving topics need more frequent substantive revision; no published engine threshold exists)
- [ ] Content provides unique value vs competitors

### Keyword Strategy

- [ ] Primary keyword identified for each page
- [ ] Secondary keywords mapped
- [ ] Long-tail keywords targeted
- [ ] No keyword cannibalization
- [ ] Keywords match user intent

---

## Monitoring & Analytics

### Setup

- [ ] Google Analytics installed
- [ ] Google Search Console connected
- [ ] Bing Webmaster Tools connected
- [ ] Sitemap submitted to both

### Regular Checks

- [ ] Weekly: Check Search Console for errors
- [ ] Weekly: Review Core Web Vitals (LCP, INP, CLS)
- [ ] Monthly: Analyze organic traffic trends
- [ ] Monthly: Review top performing pages
- [ ] Quarterly: Full SEO audit

---

## Quick Audit Commands

```bash
# Check meta tags
curl -sL "https://example.com" | grep -E "<title>|<meta"

# Check robots.txt
curl -s "https://example.com/robots.txt"

# Check sitemap
curl -s "https://example.com/sitemap.xml" | head -30

# Check page speed (using PageSpeed Insights API)
# Requires API key
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&strategy=mobile"

# Check if indexed in Google
# Manual check: https://www.google.com/search?q=site:example.com

# Validate schema
# Open: https://search.google.com/test/rich-results?url=https://example.com
```

---

## Priority Matrix

| Priority | Task | Impact |
|----------|------|--------|
| **Critical** | Fix crawl errors | Blocks indexing |
| **Critical** | HTTPS enabled | Trust + ranking |
| **High** | Core Web Vitals | UX + ranking |
| **High** | Mobile experience | Google uses the mobile version of a site's content for indexing and ranking |
| **High** | Search-index AI crawlers allowed (robots.txt and CDN) | AI-search citation eligibility |
| **Medium** | Meta descriptions | CTR improvement |
| **Medium** | Internal linking | Authority distribution |
| **Low** | Social meta tags | Share appearance |
