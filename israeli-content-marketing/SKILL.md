---
name: israeli-content-marketing
description: Plan and execute content marketing strategies for the Israeli market including Hebrew SEO content, tech media outreach to Geektime and Calcalist, and B2B content. Use when user asks about Israeli content strategy, Hebrew blog posts, Israeli tech PR, or Hebrew B2B content. Covers Israeli tech media landscape, Hebrew content SEO, and bilingual content strategies.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---

# Israeli Content Marketing

## Instructions

### Israeli Media Landscape
Key outlets: Geektime (tech blog), Calcalist Tech (business+tech), The Marker (business), Globes (business), Ynet Tech (general), CTech (English). Mobile-first consumption (>70%). Facebook groups are major content discovery channel.

### Hebrew SEO Content Strategy
Use Google Keyword Planner with Israel location. Check Google Trends Israel. URL slugs: transliterated Hebrew or English (avoid encoded Hebrew). Structure: H2 every 200-300 words, short paragraphs (2-3 sentences).

### Content Types for Israeli Market
B2B: Case studies with Israeli clients (very high effectiveness), data-driven reports, Hebrew webinars, how-to guides. B2C: Buying guides with NIS pricing, Hebrew reviews, seasonal content tied to Jewish holidays.

### Israeli Tech PR
Keep pitches brief and direct. WhatsApp follow-ups acceptable. Include quick facts: founding, team size, funding, traction. Hebrew pitches for Hebrew outlets; English for CTech, No Camels.

### Content Distribution
Google SEO, Facebook groups (value-first), LinkedIn (B2B), email newsletter (Chok HaSpam compliant), WhatsApp (viral), Telegram (tech communities).

### Repurposing
Blog post -> social snippets -> email summary -> LinkedIn article -> video -> infographic.

## Examples

### Example 1: Create Hebrew Blog Content Calendar
User says: "Plan a 3-month content calendar for our Israeli SaaS blog"
Actions:
1. Identify Hebrew keyword clusters for the industry
2. Map content to Israeli business calendar (avoid holidays, leverage events)
3. Plan weekly cadence: 1 long-form post + 2 social snippets
4. Include Hebrew SEO optimization for each piece
5. Assign distribution channels (LinkedIn IL, Facebook groups, Calcalist)
Result: 12-week Hebrew content calendar with SEO targets and distribution plan

### Example 2: Write Hebrew Thought Leadership Article
User says: "Write an article about AI trends for Israeli tech audience"
Actions:
1. Research trending topics in Israeli tech press (Geektime, Calcalist Tech)
2. Write 1500-word Hebrew article with data and expert quotes
3. Optimize for Hebrew SEO with meta description and headers
4. Create social snippets for LinkedIn and Twitter
Result: Publishable Hebrew tech article with social distribution kit

## Bundled Resources

### Scripts
- `scripts/content_calendar.py` -- Generates content calendars accounting for Israeli holidays and business cycles. Run: `python scripts/content_calendar.py --help`

### References
- `references/israeli-media-landscape.md` -- Israeli media outlets, tech publications, content distribution channels, and audience demographics. Consult when planning content distribution or media outreach.

## Gotchas

- Israeli content consumption is heavily mobile-first (over 70%). Agents may produce desktop-optimized content with long paragraphs that perform poorly on mobile screens.
- Facebook groups remain the dominant content discovery channel in Israel, unlike the US where search and social feeds dominate. Agents may deprioritize Facebook group strategy.
- Hebrew URL slugs should be transliterated or in English, not URL-encoded Hebrew characters. Agents may generate encoded Hebrew URLs that are unreadable and hurt SEO.
- Israeli work week runs Sunday-Thursday, not Monday-Friday. Content publishing schedules must be adjusted accordingly. Friday afternoon through Saturday is very low engagement.
- Hebrew content must be written natively, not translated from English. Machine-translated Hebrew sounds unnatural and Israeli audiences will disengage immediately.

## Troubleshooting

### Error: "Content not ranking for Hebrew keywords"
Cause: Hebrew SEO requires different optimization than English
Solution: Use exact Hebrew phrases (not transliterations), include common misspellings, and ensure proper hreflang tags for he-IL locale.

### Error: "Low engagement on Israeli social platforms"
Cause: Content timing or format mismatch with Israeli audience habits
Solution: Post Sunday-Thursday (Israeli work week), peak times 8-9am and 12-1pm. Israeli audiences prefer informal tone and local references over corporate language.
