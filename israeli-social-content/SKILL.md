---
name: israeli-social-content
description: Create social media content optimized for Israeli audiences across Facebook, Instagram, TikTok, and LinkedIn. Use when user asks about Israeli social media strategy, Hebrew social posts, posting schedules for Israel, Hebrew hashtags, or Israeli Facebook group marketing. Covers platform-specific best practices, Israeli cultural references, and Hebrew copywriting for social. Do NOT use for paid ad campaigns, influencer outreach, or SEO content writing.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---

# Israeli Social Content

## Instructions

### Step 1: Identify the Platform Mix

Choose platforms based on audience and goals. Israeli platform landscape (DataReportal Digital 2026, figures for late 2025):

| Platform | Users (IL) | Primary Age | Best For |
|----------|-----------|-------------|----------|
| Facebook | ~5.05M ad reach (~7.6M all-ages, NapoleonCat) | 25-55 | Community, groups, local discovery |
| Instagram | ~5M | 18-35 | Visual brands, Reels, lifestyle |
| TikTok | ~4.49M (18+) | 16-30 | Viral reach, younger audiences |
| LinkedIn | ~3.1M | 25-55 | B2B, tech, hiring |

Methodology notes: the Facebook, Instagram, and TikTok figures are DataReportal Digital 2026 ad-reach numbers (TikTok's is the 18+ figure), so some under-18 users are excluded and true totals are higher. The ~7.6M Facebook figure is NapoleonCat's all-ages count (a different methodology), shown for context. LinkedIn counts registered members, not monthly active users. For raw scale, YouTube is actually Israel's largest platform (~7M); Facebook (~5.05M) and Instagram (~5M) are roughly tied. Treat all as directional and re-verify against the current DataReportal Israel report before quoting a number to a client.

Decision criteria:
- B2C local business (restaurant, salon, shop) -> Facebook groups + Instagram
- B2B / tech startup -> LinkedIn + Facebook professional groups
- Targeting under-30 audience -> TikTok + Instagram Reels
- Community building -> Facebook groups (still the #1 discovery channel in Israel)

### Step 2: Write Hebrew Social Copy

Write in spoken Hebrew (ivrit meduberet), not formal written Hebrew. Key rules:

1. **Hook first.** The first line determines whether users stop scrolling. Lead with a bold claim, question, or personal story.
2. **Use contractions naturally.** Write "אני לא" not "אינני". Write "יש לי" not "ברשותי".
3. **Paragraph breaks for mobile.** 70%+ of Israeli social traffic is mobile. One idea per paragraph, blank lines between.
4. **Dugri tone wins.** Israeli audiences respond to direct, honest, personal content. Corporate-polished copy underperforms consistently.
5. **Bilingual when relevant.** Tech and business terms stay in English (SaaS, ROI, B2B). Do not transliterate.

### Step 2b: Disclose AI-Generated Content (2026)

If you use AI to generate or substantially alter visuals or audio (images, video, voiceover), both Meta (Facebook/Instagram/Threads) and TikTok require disclosure in 2026, and both auto-detect and label realistic AI media via C2PA Content Credentials whether or not you self-disclose:

1. **Toggle the platform's "AI-generated" / "Made with AI" label** when you publish AI visuals or audio, especially anything photorealistic.
2. Expect an automatic "AI Info" label if your file carries C2PA provenance metadata (most AI image and video tools now embed it).
3. Repeated non-disclosure of realistic AI content can get posts demoted, ads rejected, or the account restricted.
4. Lightly stylized graphics, text overlays, and obvious illustrations generally do not need a label; realistic depictions of people, voices, or events do. Verify the current Meta and TikTok policies before a campaign.

### Step 3: Apply Platform-Specific Strategy

**Facebook:** Groups are the primary channel. Post types that perform: personal stories, hot takes, advice requests, polls. Page-only strategies underperform. Identify and join relevant groups (city, professional, interest-based).

**Instagram:** Reels still lead organic reach, but in 2026 the dominant ranking signals are watch time and "sends" (DM shares per reach), with likes downgraded, so make content worth sending to a friend. Carousels now edge out Reels on engagement rate, use them for educational, save-worthy content. Hebrew captions with line breaks. Stories for daily engagement (polls, Q&A, behind-the-scenes). Use Hebrew text overlays on visuals.

**TikTok:** Hebrew audio performs significantly better than English audio for Israeli audiences. The algorithm rewards retention, not raw length: roughly 21-34 seconds works for entertainment and 60-90 seconds for informative or search-driven content, so match length to intent rather than always cutting to 15-60 seconds. Trends move fast, localize global trends with Israeli context. Duets and Stitches drive engagement.

**LinkedIn:** Israeli tech ecosystem content performs exceptionally. Mix: industry insights (40%), company culture (30%), product (20%), hiring (10%). Hebrew posts get higher engagement from Israeli audience but English extends global reach.

### Step 3b: Format Specs for Vertical Video and Overlays

Current specs for Reels and TikTok (verify against the platform docs in Reference Links before a production handoff):

- **Reels and TikTok video:** 1080 x 1920 px, 9:16 aspect ratio, MP4 (H.264). This fills a phone screen edge to edge.
- **Hebrew text overlays:** keep them inside the central safe zone. The bottom ~20% of the frame is covered by the caption, audio credit, and interaction buttons, and the top ~10% by the platform UI, so do not place Hebrew copy there. Center Hebrew text horizontally so RTL alignment does not collide with the right-side action rail.
- **TikTok caption:** the field allows up to 4,000 characters (it includes hashtags and mentions), but only roughly the first 80-100 characters show before truncation, so front-load the Hebrew hook.
- **Instagram caption:** up to 2,200 characters. Instagram allows up to 30 hashtags but recommends a small targeted set (3-5 is the practical sweet spot, see Step 4).

### Step 3c: RTL Caption Formatting (Hebrew, English, Emoji, Hashtags)

This is the most common Israel-specific technical failure. A caption that mixes Hebrew, English words, emoji, and Latin-script hashtags often flips reading direction mid-line, and punctuation (a period, comma, or `!`) lands on the wrong side of the line.

The failure mode: the first strong-directional character in a line decides the base direction. If a Hebrew caption opens with an English word, a digit, an emoji, or a `#hashtag`, the line renders left-to-right and the Hebrew looks broken. Trailing punctuation after a Hebrew clause can jump to the left edge.

The fix:
- Start every Hebrew line with a Hebrew letter. Never lead a line with an English word, a number, an emoji, or a hashtag.
- Put Latin-script hashtags and mentions on their own lines at the end of the caption, not inline inside Hebrew sentences.
- For an unavoidable inline English term or number inside a Hebrew sentence, wrap it with directional marks: a Right-to-Left Mark (RLM, U+200F) before and after the foreign run keeps the surrounding Hebrew base direction. A Left-to-Right Mark (LRM, U+200E) does the inverse inside English text.
- Keep punctuation tight against the Hebrew word it belongs to; if it still jumps, add an RLM right after the punctuation.
- Test the caption in the actual app composer (not just a desktop editor) before publishing, on both iOS and Android.

### Step 4: Build Hashtag Strategy

Hebrew hashtag rules:
- No underscores: #סטארטאפישראלי (correct) not #סטארטאפ_ישראלי (wrong)
- No spaces (Hebrew words concatenate naturally)
- Mix 2-3 popular tags + 2-3 niche tags per post
- Popular: #ישראל #תלאביב #שיווקדיגיטלי #הייטקישראלי #סטארטאפ #עסקיםקטנים

### Step 5: Schedule Around Israeli Calendar

- **Work week:** Sunday-Thursday. Sunday morning is the highest-engagement window (start of week).
- **Peak times:** 8-9 AM, 12-1 PM, 7-9 PM (Israel time, UTC+2/+3)
- **Shabbat:** No posting Friday afternoon through Saturday evening. Engagement drops to near-zero.
- **Holidays to avoid commercial content:** Yom Kippur (total blackout), Yom HaZikaron (memorial day)
- **Holidays to leverage:** Rosh Hashana (greetings), Hanukkah (promotions), Purim (fun content), Yom Ha'atzmaut (national pride)

Calendar dynamics to plan around:
- **Hebrew-calendar dates shift every Gregorian year.** Do not hardcode a fixed date for any Jewish holiday. Pull the current year's dates from a Hebrew-calendar source (for example Hebcal) when you build a schedule.
- **Sukkot and Pesach are week-long low-engagement windows,** not single days. Many Israelis take the whole week off (chol hamoed). Treat the full span as reduced reach, and plan a content push for "after the chagim" instead.
- **The Tishrei cluster** (Rosh Hashana, Yom Kippur, Sukkot, usually September-October) is a multi-week slowdown. "Acharei hachagim" (after the holidays) is a real planning unit Israelis use.
- **August** is a summer slowdown (school break, vacations).
- **Election days** are national holidays in Israel and engagement patterns shift; commercial content underperforms and political content is sensitive. Check whether an election or campaign period overlaps your calendar.

## Examples

### Example 1: Create Hebrew LinkedIn Content Strategy
User says: "Plan LinkedIn content for our Israeli B2B startup"
Actions:
1. Profile: Hebrew + English bilingual company page
2. Content mix: 40% industry insights, 30% company culture, 20% product, 10% hiring
3. Posting schedule: Sunday-Thursday, 8-9am Israel time
4. Hebrew hashtags: #הייטק #סטארטאפ #טכנולוגיה + English tech hashtags
5. Engage with Israeli tech community (Startup Nation Central, IVC)
Result: LinkedIn content strategy tailored for Israeli B2B audience

### Example 2: Build Hebrew Instagram Campaign
User says: "Create Instagram content for our Tel Aviv restaurant"
Actions:
1. Visual style: bright, Mediterranean aesthetic, Hebrew text overlays
2. Content: food photos with Hebrew captions, behind-the-scenes reels
3. Stories: daily specials with NIS pricing, polls in Hebrew
4. Hashtags: #תלאביב #אוכל #מסעדות + neighborhood-specific tags
5. Post timing: lunch (11am-1pm) and dinner (6pm-8pm) Israeli time
Result: Instagram content plan for Israeli food business

### Example 3: Launch TikTok Presence for Israeli Brand
User says: "We want to start TikTok for our Israeli fashion brand"
Actions:
1. Content style: behind-the-scenes, styling tips, Hebrew voiceover
2. Format: 15-30 second Reels, trending sounds with Hebrew text overlays
3. Posting: 3-5 videos/week, peak times 12pm, 5pm, 9pm
4. Hashtags: #אופנהישראלית #סטייל #תלאביב + trending global tags
5. Engagement: respond to comments in Hebrew, use Duets with local creators
Result: TikTok launch plan optimized for Israeli fashion audience

## Bundled Resources

### Scripts
- `scripts/posting_scheduler.py` -- Generates optimal posting schedules based on Israeli timezone and audience patterns. Run: `python scripts/posting_scheduler.py --platform facebook` or `python scripts/posting_scheduler.py --all`

### References
- `references/israeli-social-platforms.md` -- Israeli social media platform demographics, usage statistics, popular Israeli hashtags, and cultural content norms. Consult when planning social media strategy for Israeli audiences.

## Gotchas

- Facebook is still central in Israel, and its groups are the #1 community/discovery channel, unlike the US where it skews older. On raw scale it is now roughly tied with Instagram (~5M ad reach each, behind YouTube), so the case for Facebook is the groups, not headline user count. Agents may wrongly deprioritize Facebook groups based on US trends.
- Israeli social media engagement drops dramatically from Friday afternoon through Saturday evening (Shabbat). Agents may schedule posts during this period and see near-zero engagement.
- Hebrew social copy must use spoken Hebrew (ivrit meduberet), not formal written Hebrew. Agents often produce overly formal Hebrew that feels robotic to Israeli audiences.
- Hebrew hashtags must not contain underscores or spaces. The correct format is #סטארטאפישראלי not #סטארטאפ_ישראלי. Agents may apply English hashtag formatting conventions.
- Israeli audiences respond strongly to personal stories and "dugri" (blunt, honest) content. Corporate-polished messaging that works in the US consistently underperforms in Israeli social media.
- Mixed Hebrew/English/emoji/hashtag captions flip reading direction and misplace punctuation. The first strong-directional character in a line sets its base direction, so a Hebrew line that starts with a hashtag, emoji, or English word renders left-to-right and looks broken. Always lead Hebrew lines with a Hebrew letter.
- TikTok's US operations moved to a majority-American joint venture (Oracle, Silver Lake, MGX) that closed January 2026. Any TikTok policy, data-handling, or feature claim should be re-verified against current TikTok documentation rather than assumed from older sources.
- A clickable external link in the caption costs organic reach. Meta applies a reach reduction to Instagram caption links (around 15%) and Facebook suppresses external-link feed posts, and TikTok keeps users on-platform too. Put the link in the first comment or send people to the bio/profile, and use teaser content that earns a profile visit. Nuance: Instagram's head confirmed the phrase "link in bio" in a caption does NOT hurt reach (that is a myth), it is the clickable URL in the caption that gets the reach penalty, so writing "link in bio" is fine.

## Recommended MCP Servers

No MCP server applies to this skill. Social content creation, scheduling, and Hebrew copywriting are reasoning and writing tasks that the agent performs directly with the bundled script and references. There is no Israeli social-platform API in the skills-il MCP directory that this workflow depends on.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Meta Business Help Center | https://www.facebook.com/business/help | Facebook and Instagram page/group rules, content policies |
| Instagram for Creators | https://creators.instagram.com | Reels specs, caption and hashtag guidance |
| Instagram Help Center | https://help.instagram.com | Account, posting, and feature documentation |
| TikTok for Business | https://ads.tiktok.com/business/en | TikTok content formats, video specs, business features |
| LinkedIn Business Solutions | https://business.linkedin.com | Organic content best practices for LinkedIn |
| DataReportal Digital 2026 Israel | https://datareportal.com/reports/digital-2026-israel | Current Israeli social platform user counts and methodology |

## Troubleshooting

### Error: "Hebrew hashtags not trending"
Cause: Hebrew hashtags have different discovery patterns than English
Solution: Mix Hebrew and English hashtags. Use Hebrew for local reach (#תלאביב) and English for broader tech/business reach (#StartupNation). Monitor trending hashtags on each platform.

### Error: "Post engagement drops on Fridays/Saturdays"
Cause: Shabbat significantly reduces Israeli social media activity
Solution: Avoid posting Friday afternoon through Saturday evening. Schedule important content for Sunday morning (start of Israeli work week) for maximum reach.

### Error: "LinkedIn posts not getting traction in Israel"
Cause: Generic English-only content does not resonate with Israeli professionals
Solution: Write in Hebrew for local engagement. Lead with personal experience, not corporate announcements. Israeli LinkedIn favors storytelling over formal business updates. Post Sunday-Wednesday mornings for best reach.
