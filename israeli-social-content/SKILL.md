---
name: israeli-social-content
description: Create social media content optimized for Israeli audiences across Facebook, Instagram, TikTok, and LinkedIn. Use when user asks about Israeli social media strategy, Hebrew social posts, posting schedules for Israel, Hebrew hashtags, or Israeli Facebook group marketing. Covers platform-specific best practices, Israeli cultural references, and Hebrew copywriting for social. Do NOT use for paid ad campaigns, influencer outreach, or SEO content writing.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---

# Israeli Social Content

## Instructions

### Step 1: Identify the Platform Mix

Choose platforms based on audience and goals. Israeli platform landscape (early 2026 data):

| Platform | Users (IL) | Primary Age | Best For |
|----------|-----------|-------------|----------|
| Facebook | ~7.6M | 25-55 | Community, groups, local discovery |
| Instagram | ~5M | 18-35 | Visual brands, Reels, lifestyle |
| TikTok | ~4.5M (18+) | 16-30 | Viral reach, younger audiences |
| LinkedIn | ~3.1M | 25-55 | B2B, tech, hiring |

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

### Step 3: Apply Platform-Specific Strategy

**Facebook:** Groups are the primary channel. Post types that perform: personal stories, hot takes, advice requests, polls. Page-only strategies underperform. Identify and join relevant groups (city, professional, interest-based).

**Instagram:** Reels dominate organic reach. Hebrew captions with line breaks. Carousel posts for educational content. Stories for daily engagement (polls, Q&A, behind-the-scenes). Use Hebrew text overlays on visuals.

**TikTok:** Hebrew audio performs significantly better than English audio for Israeli audiences. Ideal length: 15-60 seconds. Trends move fast, localize global trends with Israeli context. Duets and Stitches drive engagement.

**LinkedIn:** Israeli tech ecosystem content performs exceptionally. Mix: industry insights (40%), company culture (30%), product (20%), hiring (10%). Hebrew posts get higher engagement from Israeli audience but English extends global reach.

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

- Facebook remains the #1 social platform in Israel with ~7.6M users, unlike the US where it skews older. Agents may deprioritize Facebook in favor of Instagram or TikTok based on US trends.
- Israeli social media engagement drops dramatically from Friday afternoon through Saturday evening (Shabbat). Agents may schedule posts during this period and see near-zero engagement.
- Hebrew social copy must use spoken Hebrew (ivrit meduberet), not formal written Hebrew. Agents often produce overly formal Hebrew that feels robotic to Israeli audiences.
- Hebrew hashtags must not contain underscores or spaces. The correct format is #סטארטאפישראלי not #סטארטאפ_ישראלי. Agents may apply English hashtag formatting conventions.
- Israeli audiences respond strongly to personal stories and "dugri" (blunt, honest) content. Corporate-polished messaging that works in the US consistently underperforms in Israeli social media.

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
