# Hebrew SEO Best Practices

## .co.il Domain Strategy

### Domain Registration
- Register through ISOC-IL accredited registrars
- .co.il is the standard for Israeli commercial entities
- .org.il for non-profits, .ac.il for academic institutions
- Registration rules (who may register which .il sub-domain) are set by ISOC-IL; check its current rules rather than assuming

### Country Signals
- A country-code domain such as .co.il is a strong signal that the site targets Israel. It is a geotargeting signal, not a ranking boost.
- For a country-code domain Google lists server location as irrelevant, so do not move hosting to Israel for SEO.
- Subfolders (example.co.il/en/) work well for a bilingual site; mark the versions with hreflang.

## RTL Optimization Checklist

### HTML Configuration
- Set `dir="rtl"` on the `<html>` element for Hebrew pages
- Set `lang="he"` on the `<html>` element
- Use CSS logical properties: `margin-inline-start` instead of `margin-left`
- Test with both Hebrew-only and mixed Hebrew/English content

### Typography
- Use system fonts that support Hebrew: Arial, David, Tahoma
- Web fonts: Open Sans Hebrew, Heebo, Assistant, Rubik (Google Fonts)
- Hebrew glyphs read small at Latin sizes; test readability on mobile (a typography choice, not a ranking factor)

### Layout Considerations
- Navigation flows right-to-left
- Breadcrumbs: Home > Category > Page (RTL arrow direction)
- Form labels align to the right
- Number inputs remain LTR within RTL context
- Tables: header alignment matches text direction

## Israeli Business Directories for Local Citations

### Primary Directories
| Directory | URL | Priority | Notes |
|-----------|-----|----------|-------|
| Google Business Profile | business.google.com | Critical | Hebrew description essential |
| Zap | zap.co.il | High | Price comparison + business listings |
| duns.co.il | duns.co.il | High | D&B Israel business directory |
| b144.co.il | b144.co.il | High | Bezeq yellow pages digital |
| Waze | waze.com/business | Medium | Navigation + local discovery |
| 2all | 2all.co.il | Medium | Israeli business directory |

### Citation Consistency (NAP)
- Name: Use the exact registered Hebrew business name
- Address: Use consistent Hebrew transliteration
- Phone: include the +972 country code (Google recommends country and area code in structured data)
- Ensure identical NAP across all directory listings

## What Helps on Google in Israel

Google does not publish a separate google.co.il algorithm. The items below are practice for the Israeli market; where Google documents something, it says so.

### Content Signals
- Write natively in Hebrew; machine-translated pages tend to miss the forms people actually type (practice)
- Hebrew morphological variety in content (include prefix forms naturally)
- Bilingual content strategy: Hebrew primary, English for international reach
- Local expertise signals: references to Israeli regulations, locations, culture

### Technical Signals
- Page speed on phones: measure Core Web Vitals in PageSpeed Insights
- Core Web Vitals: LCP, INP, CLS thresholds apply equally (INP replaced FID)
- Mobile-first indexing: Google uses the mobile version of a site's content for indexing and ranking
- HTTPS on every page (a Google page-experience expectation, not an ISOC-IL rule)

### Local Signals
- Google Business Profile optimization with Hebrew content
- Local backlinks from .co.il domains
- Mentions in Israeli news sites and publications
- Reviews in Hebrew on Google Maps

### Internal Linking
- Internal links with descriptive Hebrew anchor text
- No Google documentation lists dwell time or bounce rate as ranking signals; do not promise a client a ranking effect from them

## Hebrew Keyword Research Tips

### Morphological Considerations
- Hebrew words take prefixes: people search בית, הבית, בבית, לבית. After ב/כ/ל the article ה is not written. Check which forms actually appear with `analyze_keywords.py --gsc-queries`
- Acronyms appear with and without gershayim (נדל"ן, נדל״ן, נדלן), and spelling varies between ktiv male and ktiv haser (תוכנית / תכנית)
- Plural forms differ by gender: -im (masculine), -ot (feminine)
- Construct state (smikhut) creates compound terms: "beit sefer" (school, literally house of book)
- Acronyms are common: tanakh, rambam, mashav

### Search Behavior Patterns
- Many Israelis search in Hebrew with occasional English technical terms
- Brand names often searched in English even by Hebrew speakers
- Check competition for specific Hebrew queries in a keyword tool (Keyword Planner, or `related_keywords.py` for a 0-100 difficulty score); Search Console shows demand and position, not competition

### Tool Recommendations
- Google Keyword Planner with location set to Israel
- Google Trends filtered to Israel
- Google Search Console Performance report filtered to country Israel (Search Console has no google.co.il property; properties are your own domains)
- Ahrefs/SEMrush with .co.il domain focus
