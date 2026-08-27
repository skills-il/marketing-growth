---
name: israeli-content-marketing
description: Plan and execute content marketing strategies for the Israeli market including Hebrew SEO content, Hebrew AEO for AI search, tech media outreach to Geektime and Calcalist, and B2B content. Use when user asks about Israeli content strategy, Hebrew blog posts, Israeli tech PR, or Hebrew B2B content. Covers Israeli tech media landscape, Hebrew content SEO, Hebrew keyword research, and bilingual content strategies. Do NOT use for paid ad campaigns, social-media community management, or technical SEO audits.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---

# Israeli Content Marketing

## Instructions

### Israeli Media Landscape
Key outlets: Geektime (tech blog), Calcalist Tech (business+tech), The Marker (business), Globes (business), ynet Digital (general consumer tech, the section is `ynet.co.il/digital`, there is no `/tech` section), CTech (English). **NoCamels has ceased operations**: its About page states it was active from 2011 to 2024 and that operations are paused, and its last post is from October 2024. Do not pitch it. Israeli web traffic splits 53.62% mobile / 44.91% desktop (StatCounter, July 2026), so write for mobile FIRST but do not assume desktop is a rounding error, nearly half the audience is on it. Facebook groups are a major content discovery channel.

### Hebrew SEO Content Strategy
Use Google Keyword Planner with Israel location. Check Google Trends Israel. URL slugs: transliterated Hebrew or English (avoid encoded Hebrew). Structure: break the page with an H2 roughly every 200-300 words and keep paragraphs to 2-3 sentences. These are editorial conventions for scannability, not ranking thresholds published by Google, so treat them as defaults to adapt rather than rules to enforce.

### Hebrew Keyword Research
Hebrew keyword research is not English keyword research translated. The language behaves differently:

- **Root-based morphology.** Hebrew words are built from 3-4 letter roots. A single root generates many surface forms (verb conjugations, noun patterns, gendered and plural forms). Research the root family, not just one inflection, and cover the high-volume forms users actually type.
- **Attached prefixes.** The letters ב, ל, ה, ש, ו, מ, כ attach directly to the next word (בתל-אביב, לשיווק, השיווק). The same concept appears with and without a prefix. Account for both; do not treat "שיווק" and "השיווק" as unrelated.
- **Ktiv male vs ktiv haser.** Hebrew has two spelling conventions (full vs defective spelling), so the same word has variant spellings (for example מנהל vs מנהל with an extra yud). Users search both. Include the common variants.
- **No capitalization.** Hebrew has no upper/lower case, so brand names and proper nouns are not visually distinct. This removes one disambiguation signal; rely on context words instead.
- **Nikud stripping.** Almost nobody types vowel points (nikud). Strip nikud from keyword lists and target the unpointed forms.
- **Final-letter (sofit) normalization.** The letters כ/ך, מ/ם, נ/ן, פ/ף, צ/ץ are the same letter in final vs non-final position. Normalize sofit forms when comparing or deduplicating keyword variants.

### AEO / AI Search Optimization in Hebrew
AI Overviews, Google's AI Mode and other LLM-based answer engines are the biggest 2026 shift in content marketing. Hebrew content appears to be thinner than English on many topics, which plausibly leaves citation room, though treat that as a working assumption rather than a measured fact. Optimize Hebrew content to be cited, not just ranked:

- **Question to answer-block structure.** Lead a section with the literal question a user would ask in Hebrew, then answer it in the first 2-3 sentences directly below, before any preamble. AI engines extract these self-contained answer blocks.
- **Tables and schema markup.** Put comparisons, prices, and specs in real HTML tables, and add structured data (FAQPage, Article, Product, HowTo where it fits). Structured, machine-readable content is far easier for an AI engine to lift and attribute.
- **Earned-media distribution.** AI engines cite earned media (news coverage, third-party guides, reputable directories) far more often than brand-owned sites. Pair every content piece with an earned-media play, do not rely on the brand blog alone.
- **The Hebrew thin-coverage opportunity.** Where high-quality Hebrew content on a topic is thin, a well-structured Hebrew answer block can become the cited source for it. Check the actual Hebrew SERP and AI answers for your target questions before assuming the gap exists.
- **Decide your crawler permissions deliberately.** Whether AI surfaces may use your content is a setting, not a given: Google's `Google-Extended` control governs Gemini and grounded AI use, separately from ordinary Search indexing. See Google's crawler overview and its AI-features guidance. Blocking it and then asking to be cited by AI is a contradiction, so make the choice explicitly and document it.

### Content Types for Israeli Market
B2B: case studies with Israeli clients (the format Israeli B2B marketers reach for most often, though that is practitioner convention rather than measured effectiveness data), data-driven reports, Hebrew webinars, how-to guides. B2C: Buying guides with NIS pricing, Hebrew reviews, seasonal content tied to Jewish holidays.

### Israeli Content Calendar
Plan publishing around the Israeli rhythm, not the Gregorian/US one. The bundled `scripts/content_planner.py` encodes specific holiday dates, but the planning logic is:

- **The Tishrei cluster (September-October slowdown).** Rosh Hashana, Yom Kippur, and Sukkot fall in close succession, and the whole stretch is low-engagement. Israelis plan around "acharei hachagim" (after the holidays) as a unit; treat it as a content lull followed by a sharp November rebound.
- **Pesach (spring).** A week-long slowdown (the chol hamoed week), not a single day. Engagement drops; many people are off.
- **August summer boom or slowdown.** School is out and many take vacation, so B2B engagement dips, but B2C and consumer content can spike. Plan content type by audience.
- **Election cycles.** Israeli elections are frequent and unpredictable; campaign periods make commercial content underperform and political topics sensitive. Check whether an election overlaps your calendar.
- **Hebrew-calendar dates shift every Gregorian year.** Never hardcode a holiday date. Pull the current year's dates from a Hebrew-calendar source.
- **Yom Kippur, Yom HaShoah, and Yom HaZikaron:** absolute no-commercial-content days. Yom HaShoah (Holocaust Remembrance Day, ~a week before Yom HaZikaron) and Yom HaZikaron are siren days where advertising is suspended and venues close, never schedule promotional content on them.

### Israeli Tech PR
Keep pitches brief and direct. WhatsApp follow-ups acceptable. Include quick facts: founding, team size, funding, traction. Hebrew pitches for Hebrew outlets; English for CTech. NoCamels is no longer operating, so for an English-language lane evaluate and verify a current alternative (Globes English, Times of Israel tech, Jerusalem Post tech) before pitching rather than reusing an outlet list from memory.

### Content Distribution
Google SEO, Facebook groups (value-first), LinkedIn (B2B), email newsletter, WhatsApp, Telegram (tech communities).

### Distribution Compliance (do this before the first send, not after)

Two duties bind almost everything this skill produces, and neither is satisfied by a label in a plan.

**The anti-spam rule (חוק הספאם, סעיף 30א to the Communications Law).** It governs email, SMS, automated calls and fax, so it covers the newsletter and any bulk WhatsApp or SMS push.
- **Prior consent is required.** The law prohibits sending an advertisement without obtaining the recipient's consent in advance. Building a list by scraping, buying or importing contacts is not consent.
- **The exposure is per message and needs no proof of harm.** A court may award up to NIS 1,000 **for each advertisement sent**, with no need to show the recipient suffered any damage, and the awards accumulate across messages. Sending in breach is also a criminal offence, with a fine of up to NIS 226,000 (2026).
- Practically: a single Hebrew blast to a few thousand non-consenting addresses is a six-figure exposure, and it is claimable in small-claims court without a lawyer.
- Give every message a working opt-out by the same channel it arrived on, honour it promptly, and keep a record of when and how each recipient consented.

**Disclosure of paid or brand-placed content.** Two instructions in this skill lead straight into it: seeding content into Facebook groups, and placing pieces with outlets. Marketing content that reads as independent editorial or as an ordinary community post must be labelled as what it is (`תוכן שיווקי`, `בחסות`, `בשיתוף`). Undisclosed promotion is a consumer-protection problem, not a style preference. Check the outlet's own commercial-content policy, and note that a paid placement is not a "guest post".

**Building the list is also a privacy question.** An email list is a database of personal data, so Israel's Privacy Protection Law (as amended by Amendment 13, in force August 2025) attaches, including its specific direct-marketing (דיוור ישיר) duties. Do not design a list-building flow without checking those obligations.

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
4. Create social snippets for LinkedIn and X (formerly Twitter)
Result: Publishable Hebrew tech article with social distribution kit

## Bundled Resources

### Scripts
- `scripts/content_planner.py` -- Generates content calendars accounting for Israeli holidays and business cycles. Run: `python scripts/content_planner.py --month 9 --year 2026` or `python scripts/content_planner.py --help`. Note: the holiday table is hardcoded per year (2025, 2026, and 2027 included); verify the dates against hebcal.com and extend the table for future years before relying on it.

### References
- `references/israeli-media-landscape.md` -- Israeli media outlets, tech publications, content distribution channels, and audience demographics. Consult when planning content distribution or media outreach.

## Recommended MCP Servers

The `hebcal` MCP server (Hebrew calendar dates and holidays) is tangentially useful for the content-calendar workflow: since Hebrew-calendar holidays shift every Gregorian year, an agent can use it to pull accurate current-year holiday dates instead of relying on the script's hardcoded table. It is optional, not required. No core MCP server is essential to this skill, since Hebrew content writing, keyword research, and AEO structuring are reasoning tasks the agent performs directly.

## Gotchas

- Israeli web traffic is 53.62% mobile and 44.91% desktop (StatCounter, July 2026), not the "over 70% mobile" figure that circulates. Write mobile-first, with short paragraphs and scannable structure, but do not drop desktop considerations such as table layout and wider media, because nearly half the audience is on desktop. Agents commonly do one of two wrong things here: produce desktop-shaped walls of text, or over-correct and treat desktop as negligible.
- Facebook groups are a far more important content-discovery channel in Israel than a US-shaped playbook assumes, and agents routinely deprioritise them for that reason. Treat their relative weight as a working assumption to test against the account's own referral data rather than a measured ranking; the point is to evaluate the channel, not to assume it wins.
- Hebrew URL slugs should be transliterated or in English, not URL-encoded Hebrew characters. Agents may generate encoded Hebrew URLs that are unreadable and hurt SEO.
- Israeli work week runs Sunday-Thursday, not Monday-Friday. Content publishing schedules must be adjusted accordingly. Friday afternoon through Saturday is very low engagement.
- Hebrew content must be written natively, not translated from English. Machine-translated Hebrew sounds unnatural and Israeli audiences will disengage immediately.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Geektime | https://www.geektime.co.il | Israeli tech news and coverage. Its site offers a commercial "פרסמו אצלנו" route and a general contact route; do not assume an editorial guest-contributor programme, and if a placement is paid it must be labelled as such |
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
Solution: Post Sunday-Thursday (Israeli work week). The bundled planner uses 09:00-10:00, 12:00-13:00 and 19:00-21:00 as its default slots; treat these as starting defaults and replace them with the account's own analytics as soon as you have data, since they are conventions rather than measured benchmarks. Israeli audiences prefer informal tone and local references over corporate language.
