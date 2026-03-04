---
name: hebrew-seo-toolkit
description: >-
  Optimize websites for Hebrew SEO on Google.co.il, including keyword research
  with Hebrew morphological analysis, hreflang setup for he-IL, and structured
  data markup. Use when user asks about Hebrew keyword research, Israeli SEO,
  .co.il domain optimization, Hebrew schema.org markup, or asks about "kidum
  atarim", "milot mafteach", "SEO", or Israeli search ranking. Supports Hebrew
  root-based morphology analysis, JSON-LD structured data, and Israeli business
  schema (Shabbat hours, kosher certification). Do NOT use for general
  English-only SEO, paid advertising campaigns, or social media marketing.
license: MIT
compatibility: >-
  Requires network access for keyword analysis. Works with Claude Code, Cursor,
  GitHub Copilot, Windsurf, OpenCode, Codex.
metadata:
  author: skills-il
  version: 1.0.0
  category: marketing-growth
  tags:
    he:
      - קידום-אתרים
      - SEO
      - מילות-מפתח
      - עברית
      - גוגל
      - ישראל
    en:
      - seo
      - keywords
      - hebrew
      - google
      - optimization
      - israel
  display_name:
    he: ערכת כלים לקידום אתרים בעברית
    en: Hebrew SEO Toolkit
  display_description:
    he: >-
      מחקר מילות מפתח בעברית, אופטימיזציה לדומיינים ישראליים, ונתונים מובנים
      לגוגל ישראל
    en: >-
      Hebrew keyword research with morphological analysis, .co.il domain
      optimization, hreflang setup for he-IL, and Israeli business schema
      markup for Google.co.il ranking
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
---

# Hebrew SEO Toolkit

## Instructions

### Step 1: Analyze Hebrew Keyword Morphology
Hebrew is a root-based (shoresh) language where prefixes change meaning. Identify keyword variants:

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
5. Run `scripts/analyze_keywords.py` on the keyword list to get variant counts

### Step 2: Configure .co.il Domain SEO
Israeli domains have specific optimization requirements:

| Setting | Value | Notes |
|---------|-------|-------|
| TLD priority | .co.il | Preferred for Israeli businesses |
| Server location | Israel or nearby CDN | Improves local ranking |
| Google Search Console | google.co.il property | Register separately from .com |
| Sitemap | Include hreflang annotations | Required for bilingual sites |
| robots.txt | Allow Googlebot | Standard configuration |

Configuration checklist:
1. Register the .co.il domain with an ISOC-IL accredited registrar
2. Set up Google Search Console for the .co.il property specifically
3. Configure DNS with Israeli or nearby CDN endpoints
4. Verify the site loads correctly with RTL (right-to-left) layout
5. Submit XML sitemap with hreflang annotations to Google Search Console

### Step 3: Implement hreflang Tags
Set up proper language targeting for Hebrew-Israeli content:

```html
<!-- In HTML head -->
<link rel="alternate" hreflang="he-IL" href="https://example.co.il/page" />
<link rel="alternate" hreflang="en" href="https://example.co.il/en/page" />
<link rel="alternate" hreflang="x-default" href="https://example.co.il/en/page" />
```

For XML sitemap hreflang:
```xml
<url>
  <loc>https://example.co.il/page</loc>
  <xhtml:link rel="alternate" hreflang="he-IL" href="https://example.co.il/page"/>
  <xhtml:link rel="alternate" hreflang="en" href="https://example.co.il/en/page"/>
</url>
```

Rules for Israeli sites:
1. Always use `he-IL` (not just `he`) for Israeli Hebrew content
2. Set `x-default` to the English version for international visitors
3. Every page in one language must link to its counterpart in all other languages
4. hreflang must be bidirectional (Hebrew page links to English, English links to Hebrew)
5. Use consistent absolute URLs across all hreflang declarations

### Step 4: Build Hebrew Schema.org Structured Data
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

Israeli-specific schema considerations:
1. **Shabbat hours:** Friday closes early (typically 14:00), Saturday closed. Use `OpeningHoursSpecification` with no Saturday entry.
2. **Kosher certification:** Use `additionalProperty` with `name: "Kosher Certification"` and the certifying body (Rabbanut, Badatz, etc.)
3. **Phone format:** Always use `+972` international prefix
4. **Address format:** Use Hebrew transliteration for street names; include postal code (mikud)
5. **Currency:** Set `priceCurrency` to `ILS` for all pricing

### Step 5: Optimize for Google.co.il Ranking Factors
Israeli-specific ranking considerations:

| Factor | Priority | Action |
|--------|----------|--------|
| Hebrew content quality | High | Natural Hebrew, not machine-translated |
| RTL layout | High | Proper dir="rtl" on html element |
| Mobile optimization | High | 70%+ Israeli traffic is mobile |
| Page speed | High | Use Israeli CDN nodes (Cloudflare TLV) |
| Local citations | Medium | Zap, duns.co.il, b144.co.il listings |
| Google Business Profile | High | Claim and optimize with Hebrew description |
| SSL certificate | High | Required for all .co.il sites |

Implementation steps:
1. Ensure all Hebrew content is written by native speakers or thoroughly reviewed
2. Set `<html lang="he" dir="rtl">` on all Hebrew pages
3. Optimize Core Web Vitals targeting Israeli mobile networks
4. Create and verify Google Business Profile with Hebrew business description
5. Build local citations on Israeli business directories (Zap, duns.co.il, b144.co.il)
6. Ensure all images have Hebrew alt text

### Step 6: Generate Israeli Business Schema Markup
For businesses requiring specialized Israeli markup:

Shabbat-aware hours example:
```json
{
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Sunday","Monday","Tuesday","Wednesday","Thursday"],
      "opens": "08:00",
      "closes": "20:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Friday",
      "opens": "08:00",
      "closes": "14:00",
      "description": "Erev Shabbat - early closing"
    }
  ]
}
```

Kosher certification markup:
```json
{
  "additionalProperty": [
    {
      "@type": "PropertyValue",
      "name": "Kosher Certification",
      "value": "Rabbanut Yerushalayim"
    },
    {
      "@type": "PropertyValue",
      "name": "Kashrut Level",
      "value": "Mehadrin"
    }
  ]
}
```

### Step 7: Validate and Audit
Run a comprehensive SEO audit:
1. Validate all JSON-LD with Google Rich Results Test
2. Check hreflang implementation with hreflang tag checker tools
3. Verify Hebrew content renders correctly in RTL
4. Test mobile responsiveness on common Israeli devices
5. Run `scripts/analyze_keywords.py --audit` to check keyword coverage
6. Verify Google Search Console shows no hreflang errors
7. Confirm all local directory listings are consistent (NAP: Name, Address, Phone)

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

### Example 3: Israeli Restaurant Schema
User says: "Create structured data for my kosher restaurant in Jerusalem"
Actions:
1. Build LocalBusiness/Restaurant JSON-LD with Israeli address format
2. Add Shabbat-aware opening hours (Friday early close, Saturday closed)
3. Include kosher certification with Rabbanut details
4. Add Hebrew menu schema with NIS pricing
Result: Complete JSON-LD markup ready for Google Rich Results

### Example 4: Google.co.il SEO Audit
User says: "Audit my Israeli e-commerce site for local SEO"
Actions:
1. Check Hebrew content quality and RTL rendering
2. Verify .co.il domain configuration and Google Search Console setup
3. Audit hreflang tags and language targeting
4. Review Google Business Profile and local citations
5. Run keyword analysis for Hebrew product category terms
Result: Prioritized SEO improvement recommendations for the Israeli market

## Bundled Resources

### Scripts
- `scripts/analyze_keywords.py` -- Analyzes Hebrew keywords using morphological rules: generates prefix variants (ha-, ve-, be-, le-, me-, she-), plural forms, and construct state combinations. Run: `python scripts/analyze_keywords.py --help`

### References
- `references/hebrew-seo.md` -- Comprehensive guide to Hebrew SEO best practices including .co.il domain strategy, RTL optimization checklist, Israeli business directories for local citations, and Google.co.il-specific ranking factors. Consult when implementing or auditing Hebrew SEO.

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
