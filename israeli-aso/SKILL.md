---
name: israeli-aso
description: Optimize mobile app listings for Israeli users on Apple App Store and Google Play with Hebrew metadata, keywords, and screenshots. Use when user asks about Israeli app store optimization, Hebrew app listing, Hebrew keywords for app store, or localizing app metadata for Israel. Covers Hebrew keyword research, RTL screenshot design, and category-specific benchmarks.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex, Antigravity, Gemini CLI.
---


# Israeli ASO

## Instructions

### Israeli Mobile Market
Israel has ~8.7M smartphone users (~91% penetration). iOS ~33%, Android ~67%. Hebrew localization is critical for market share. Key categories: fintech, transportation (Moovit, Gett), food delivery (Wolt, 10bis).

### Hebrew App Title and Subtitle
30 characters max. Include primary Hebrew keyword. Patterns: [Brand] - [Hebrew Descriptor], [Hebrew Name] [Category].

### Hebrew Keyword Research
Apple: 100 character keyword field. Separate with commas, no spaces. Include morphological variants and bilingual terms (transliterations like דליברי for delivery).

### Where Each Platform Pulls Keywords From
The two stores index different fields, so the same Hebrew metadata is not interchangeable:

- **Apple App Store** indexes the app name, the subtitle, and the dedicated 100-character keyword field. It does NOT index the description, so keywords placed only in the description are wasted on Apple.
- **The Apple keyword field is per-localization.** The Hebrew (`he`) localization gets its own separate 100-character keyword field, independent of the English field. Hebrew keywords do not compete with English ones for character budget, and English keywords do not rank you for Hebrew searches. Fill the Hebrew field with Hebrew terms only.
- **Google Play** has no keyword field. It indexes the title, the short description, and the full 4,000-character description. On Play, keyword research feeds directly into how you write the Hebrew description, and repetition density in the description matters.

### RTL Screenshot Design
Text overlays must be RTL-aligned. Reading flow starts from RIGHT screenshot. Recommended fonts: Heebo, Rubik, Assistant. Include NIS prices.

Screenshot sizes (verify against Apple's screenshot specifications page in Reference Links before export):
- **iPhone 6.9" (primary required size):** 1320 x 2868 px portrait. This is App Store Connect's main required iPhone size as of 2026 (iPhone 16 Pro Max class). If you upload only this size, Apple scales it for smaller devices.
- **iPhone 6.7":** 1290 x 2796 px portrait, still accepted; provide it separately if your app renders differently on those devices.
- **iPad 13":** 2064 x 2752 px portrait.
- **Google Play phone:** 1080 x 1920 px minimum, up to 8 screenshots.

### Hebrew App Description
Write in informal Hebrew. Include social proof: "מומלצת על ידי גלובס/כלכליסט". Address Israeli concerns: privacy, no hidden fees.

### Ratings and Reviews
Israeli users leave more negative reviews than the global average and are blunt in them, so a single unanswered 1-star review reads as a red flag to the next Israeli browsing the listing. Respond in Hebrew within 24-48 hours. Trigger the rating prompt after a clear in-app win (a completed order, a saved document), never mid-task.

### A/B Testing and Conversion Optimization
Keywords and screenshots drive visibility; native store experiments prove what actually converts. Use the free built-in tools rather than guessing:
- **Apple Product Page Optimization (PPO):** test up to 3 treatment variants against the original for up to 90 days (icon, screenshots, app preview video). Pair it with **Custom Product Pages** (up to 70 per app) to show different Hebrew screenshots or messaging to different ad campaigns; custom pages now also surface in organic search.
- **Google Play Store Listing Experiments:** test the icon, screenshots, short description, and full description on a slice of traffic, one variable at a time.

Israeli angle: A/B test the RTL screenshot order (which benefit earns the rightmost/first slot), NIS-vs-USD price display, and Hebrew social-proof variants. Do not assume RTL layout and NIS pricing lift conversion, measure it.

## Examples

### Example 1: Optimize Hebrew App Store Listing
User says: "Optimize my fintech app listing for the Israeli App Store"
Actions:
1. Research Hebrew keywords: "ניהול כספים", "תקציב", "חיסכון"
2. Write title (30 chars max): "מנהל הכספים - תקציב וחיסכון"
3. Write subtitle focusing on key benefit in Hebrew
4. Create keyword field with Hebrew terms (no duplicates from title)
5. Write description with Hebrew social proof and NIS pricing
Result: Optimized Hebrew App Store listing with keyword-rich metadata

### Example 2: Localize Google Play Listing for Israel
User says: "Adapt my English app listing for Israeli users on Google Play"
Actions:
1. Translate and culturally adapt title and description
2. Add Hebrew screenshots with RTL interface
3. Include Israeli payment methods (credit cards, Bit, PayBox)
4. Add local social proof (Israeli user count, local press mentions)
Result: Culturally adapted Google Play listing for Israeli market

## Bundled Resources

### Scripts
- `scripts/keyword_analyzer.py` -- De-dupes your Hebrew base keywords, builds the comma-no-space Apple keyword field, and reports the 100-character budget (it warns on overflow instead of truncating). Apple ranks single base words and auto-combines them, so feed it base words plus your own spelling (ktiv maleh/chaser) and plural variants, not phrases or attached-prefix forms. Run: `python scripts/keyword_analyzer.py --keywords "דליברי,משלוחים,אוכל"` or `python scripts/keyword_analyzer.py --help`

### References
- `references/israeli-app-market.md` -- Israeli app market statistics, popular app categories, pricing benchmarks in NIS, and Hebrew keyword research data. Consult when researching Israeli app market or planning ASO strategy.

## Recommended MCP Servers

No MCP server applies to this skill. Hebrew keyword research, RTL screenshot planning, and metadata writing are reasoning tasks the agent performs directly with the bundled script and reference file. There is no App Store Connect or Google Play API in the skills-il MCP directory that this workflow depends on.

## Gotchas

- Hebrew has two spelling conventions (ktiv maleh and ktiv chaser) that produce different search terms. Agents may optimize for only one spelling, missing users who search the other way.
- Apple App Store keyword field is 100 characters with comma separation and no spaces. Agents often include spaces after commas, wasting precious character budget.
- Israeli app store screenshots must flow right-to-left. The first screenshot users see is the rightmost one. Agents may arrange screenshots in LTR reading order.
- NIS pricing must appear on screenshots and descriptions. Agents may default to USD pricing, which reduces trust with Israeli users.
- Israeli Android market share (~67%) is significantly higher than iOS (~33%). Agents trained on US data may over-index on App Store optimization and under-invest in Google Play.
- Google Play bans promotional words ("best", "#1", "free", "top") and calls to action ("Download now") in the app title, icon, and developer name, plus emojis and ALL-CAPS. A Hebrew title like "האפליקציה הכי טובה" or "הורידו עכשיו" can get the listing rejected. Keep the title descriptive, not promotional.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| App Store Review Guidelines | https://developer.apple.com/app-store/review/guidelines/ | Metadata, screenshot, and localization rules |
| App Store Connect Help | https://developer.apple.com/help/app-store-connect/ | Adding localizations, keywords field limits |
| Google Play Console Help | https://support.google.com/googleplay/android-developer | Store listing optimization, policy rules |
| Google Play Policy Center | https://support.google.com/googleplay/android-developer/topic/9858052 | Developer program policies |
| Apple HIG Right-to-Left | https://developer.apple.com/design/human-interface-guidelines/right-to-left | RTL layout guidelines for screenshots |

## Troubleshooting

### Error: "Hebrew keywords not ranking"
Cause: Hebrew keyword variations (with/without vav, different ktiv) not covered
Solution: Include both ktiv maleh and common misspellings. Hebrew users search with varied spelling -- add all common variants to keyword field.

### Error: "Screenshots show LTR interface"
Cause: App screenshots not localized for RTL
Solution: Create separate Hebrew screenshots showing the RTL version. Israeli users expect RTL interfaces -- LTR screenshots reduce conversion.
