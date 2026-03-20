---
name: israeli-social-content
description: >-
  Create social media content optimized for Israeli audiences across Facebook,
  Instagram, TikTok, and LinkedIn. Use when user asks about Israeli social media
  strategy, Hebrew social posts, posting schedules for Israel, Hebrew hashtags,
  or Israeli Facebook group marketing. Covers platform-specific best practices,
  Israeli cultural references, and Hebrew copywriting for social.
license: MIT
compatibility: >-
  Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
metadata:
  author: skills-il
  version: 1.0.1
  category: marketing-growth
  tags:
    he:
      - רשתות-חברתיות
      - פייסבוק
      - אינסטגרם
      - טיקטוק
      - תוכן-שיווקי
      - שיווק-דיגיטלי
    en:
      - social-media
      - facebook
      - instagram
      - tiktok
      - marketing-content
      - digital-marketing
  display_name:
    he: "תוכן לרשתות חברתיות ישראליות"
    en: "Israeli Social Content"
  display_description:
    he: >-
      יצירת תוכן לרשתות חברתיות מותאם לקהל הישראלי כולל קופי בעברית,
      האשטגים, לוח זמנים לפרסום וקבוצות פייסבוק
    en: >-
      Create social media content optimized for Israeli audiences across
      Facebook, Instagram, TikTok, and LinkedIn. Use when user asks about
      Israeli social media strategy, Hebrew social posts, posting schedules for
      Israel, Hebrew hashtags, or Israeli Facebook group marketing. Covers
      platform-specific best practices, Israeli cultural references, and Hebrew
      copywriting for social.
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
    - antigravity
---

# Israeli Social Content

## Instructions

### Israeli Social Media Landscape
Facebook (~7.6M users, ages 25-55) remains #1 in Israel. Instagram (~5.3M), TikTok (~4M growing), LinkedIn (~3.1M highest per-capita penetration). Facebook groups are the dominant discovery channel.

### Platform-Specific Strategy
**Facebook:** Groups are king. Post types that work: personal stories, hot takes, advice requests. **Instagram:** Reels dominate reach. Hebrew captions with line breaks. **TikTok:** Hebrew audio performs best. 15-60 seconds ideal. **LinkedIn:** Tech ecosystem content performs exceptionally.

### Hebrew Social Copy
Write in spoken Hebrew (ivrit meduberet). First line is your hook. Use contractions naturally. Paragraph breaks crucial for mobile.

### Israeli Hashtag Strategy
No underscores in Hebrew hashtags. Mix popular and niche. Popular: #ישראל #תלאביב #שיווקדיגיטלי #הייטקישראלי

### Content Calendar
Jewish holidays, national days, weekly rhythm (Sunday = new week, Friday = Shabbat content). Peak posting: Sunday-Thursday 8-9 AM, 12-1 PM, 7-9 PM.

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

## Bundled Resources

### Scripts
- `scripts/social_scheduler.py` -- Generates optimal posting schedules based on Israeli timezone and audience patterns. Run: `python scripts/social_scheduler.py --help`

### References
- `references/israeli-social-landscape.md` -- Israeli social media platform demographics, usage statistics, popular Israeli hashtags, and cultural content norms. Consult when planning social media strategy for Israeli audiences.

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
