---
name: israeli-content-marketing
description: Plan and execute content marketing strategies for the Israeli market including Hebrew SEO content, Hebrew AEO for AI search, tech media outreach to Geektime and Calcalist, and B2B content. Use when user asks about Israeli content strategy, Hebrew blog posts, Israeli tech PR, or Hebrew B2B content. Covers Israeli tech media landscape, Hebrew content SEO, Hebrew keyword research, and bilingual content strategies. Do NOT use for paid ad campaigns, social-media community management, or technical SEO audits.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---

# Israeli Content Marketing

## Instructions

### Israeli Media Landscape
Key outlets: Geektime (tech blog), Calcalist Tech (business+tech), The Marker (business), Globes (business), Ynet Tech (general), CTech (English). Mobile-first consumption (>70%). Facebook groups are major content discovery channel.

### Hebrew SEO Content Strategy
Use Google Keyword Planner with Israel location. Check Google Trends Israel. URL slugs: transliterated Hebrew or English (avoid encoded Hebrew). Structure: H2 every 200-300 words, short paragraphs (2-3 sentences).

### Hebrew Keyword Research
Hebrew keyword research is not English keyword research translated. The language behaves differently:

- **Root-based morphology.** Hebrew words are built from 3-4 letter roots. A single root generates many surface forms (verb conjugations, noun patterns, gendered and plural forms). Research the root family, not just one inflection, and cover the high-volume forms users actually type.
- **Attached prefixes.** The letters ב, ל, ה, ש, ו, מ, כ attach directly to the next word (בתל-אביב, לשיווק, השיווק). The same concept appears with and without a prefix. Account for both; do not treat "שיווק" and "השיווק" as unrelated.
- **Ktiv male vs ktiv haser.** Hebrew has two spelling conventions (full vs defective spelling), so the same word has variant spellings (for example מנהל vs מנהל with an extra yud). Users search both. Include the common variants.
- **No capitalization.** Hebrew has no upper/lower case, so brand names and proper nouns are not visually distinct. This removes one disambiguation signal; rely on context words instead.
- **Nikud stripping.** Almost nobody types vowel points (nikud). Strip nikud from keyword lists and target the unpointed forms.
- **Final-letter (sofit) normalization.** The letters כ/ך, מ/ם, נ/ן, פ/ף, צ/ץ are the same letter in final vs non-final position. Normalize sofit forms when comparing or deduplicating keyword variants.

### AEO / AI Search Optimization in Hebrew
AI Overviews and LLM-based answer engines are the biggest 2026 shift in content marketing, and Hebrew content is underrepresented in their training and citation pools, which is an opportunity. Optimize Hebrew content to be cited, not just ranked:

- **Question to answer-block structure.** Lead a section with the literal question a user would ask in Hebrew, then answer it in the first 2-3 sentences directly below, before any preamble. AI engines extract these self-contained answer blocks.
- **Tables and schema markup.** Put comparisons, prices, and specs in real HTML tables, and add structured data (FAQPage, Article, Product, HowTo where it fits). Structured, machine-readable content is far easier for an AI engine to lift and attribute.
- **Earned-media distribution.** AI engines cite earned media (news coverage, third-party guides, reputable directories) far more often than brand-owned sites. Pair every content piece with an earned-media play, do not rely on the brand blog alone.
- **The Hebrew underrepresentation opportunity.** Because high-quality Hebrew content on many topics is thin, a well-structured Hebrew answer block can become the cited source for a whole topic. Target specific Hebrew questions that currently have weak answers.

### Content Types for Israeli Market
B2B: Case studies with Israeli clients (very high effectiveness), data-driven reports, Hebrew webinars, how-to guides. B2C: Buying guides with NIS pricing, Hebrew reviews, seasonal content tied to Jewish holidays.

### Israeli Content Calendar
Plan publishing around the Israeli rhythm, not the Gregorian/US one. The bundled `scripts/content_planner.py` encodes specific holiday dates, but the planning logic is:

- **The Tishrei cluster (September-October slowdown).** Rosh Hashana, Yom Kippur, and Sukkot fall in close succession, and the whole stretch is low-engagement. Israelis plan around "acharei hachagim" (after the holidays) as a unit; treat it as a content lull followed by a sharp November rebound.
- **Pesach (spring).** A week-long slowdown (the chol hamoed week), not a single day. Engagement drops; many people are off.
- **August summer boom or slowdown.** School is out and many take vacation, so B2B engagement dips, but B2C and consumer content can spike. Plan content type by audience.
- **Election cycles.** Israeli elections are frequent and unpredictable; campaign periods make commercial content underperform and political topics sensitive. Check whether an election overlaps your calendar.
- **Hebrew-calendar dates shift every Gregorian year.** Never hardcode a holiday date. Pull the current year's dates from a Hebrew-calendar source.
- **Yom Kippur and Yom HaZikaron:** absolute no-commercial-content days.

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
- `scripts/content_planner.py` -- Generates content calendars accounting for Israeli holidays and business cycles. Run: `python scripts/content_planner.py --month 9 --year 2026` or `python scripts/content_planner.py --help`. Note: the holiday table is hardcoded per year (2025 and 2026 included); verify the dates and extend the table for future years before relying on it.

### References
- `references/israeli-media-landscape.md` -- Israeli media outlets, tech publications, content distribution channels, and audience demographics. Consult when planning content distribution or media outreach.

## Recommended MCP Servers

The `hebcal` MCP server (Hebrew calendar dates and holidays) is tangentially useful for the content-calendar workflow: since Hebrew-calendar holidays shift every Gregorian year, an agent can use it to pull accurate current-year holiday dates instead of relying on the script's hardcoded table. It is optional, not required. No core MCP server is essential to this skill, since Hebrew content writing, keyword research, and AEO structuring are reasoning tasks the agent performs directly.

## Gotchas

- Israeli content consumption is heavily mobile-first (over 70%). Agents may produce desktop-optimized content with long paragraphs that perform poorly on mobile screens.
- Facebook groups remain the dominant content discovery channel in Israel, unlike the US where search and social feeds dominate. Agents may deprioritize Facebook group strategy.
- Hebrew URL slugs should be transliterated or in English, not URL-encoded Hebrew characters. Agents may generate encoded Hebrew URLs that are unreadable and hurt SEO.
- Israeli work week runs Sunday-Thursday, not Monday-Friday. Content publishing schedules must be adjusted accordingly. Friday afternoon through Saturday is very low engagement.
- Hebrew content must be written natively, not translated from English. Machine-translated Hebrew sounds unnatural and Israeli audiences will disengage immediately.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Geektime | https://www.geektime.co.il | Israeli tech news, guest post opportunities |
| Calcalist | https://www.calcalist.co.il | Israeli business and tech coverage |
| Globes | https://www.globes.co.il | Israeli financial daily |
| TheMarker | https://www.themarker.com | Business newspaper (Haaretz group) |
| Google Search Central | https://developers.google.com/search/docs | Hebrew SEO, hreflang, structured data |
| Academy of the Hebrew Language | https://hebrew-academy.org.il | Authoritative Hebrew spelling and terminology |

## Troubleshooting

### Error: "Content not ranking for Hebrew keywords"
Cause: Hebrew SEO requires different optimization than English
Solution: Use exact Hebrew phrases (not transliterations), include common misspellings, and ensure proper hreflang tags for he-IL locale.

### Error: "Low engagement on Israeli social platforms"
Cause: Content timing or format mismatch with Israeli audience habits
Solution: Post Sunday-Thursday (Israeli work week), peak times 8-9am and 12-1pm. Israeli audiences prefer informal tone and local references over corporate language.
