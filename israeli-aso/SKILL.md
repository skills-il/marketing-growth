---
name: israeli-aso
description: >-
  Optimize mobile app listings for Israeli users on Apple App Store and Google
  Play with Hebrew metadata, keywords, and screenshots. Use when user asks
  about Israeli app store optimization, Hebrew app listing, Hebrew keywords
  for app store, or localizing app metadata for Israel. Covers Hebrew keyword
  research, RTL screenshot design, and category-specific benchmarks.
license: MIT
compatibility: >-
  Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
metadata:
  author: skills-il
  version: 1.0.0
  category: marketing-growth
  tags:
    he:
      - אופטימיזציה-לחנות
      - אפליקציות
      - ASO
      - גוגל-פליי
      - אפל-סטור
      - מובייל
    en:
      - app-store-optimization
      - apps
      - aso
      - google-play
      - apple-store
      - mobile
  display_name:
    he: "ASO ישראלי"
    en: "Israeli ASO"
  display_description:
    he: >-
      אופטימיזציה של אפליקציות לחנויות האפליקציות עם מטאדאטה בעברית, מחקר
      מילות מפתח, עיצוב צילומי מסך RTL ומדדי קטגוריות ישראליות
    en: >-
      Optimize mobile app listings for Israeli users on Apple App Store and
      Google Play with Hebrew metadata, keywords, and screenshots
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
    - antigravity
---

# Israeli ASO

## Instructions

### Israeli Mobile Market
Israel has ~8.5M smartphone users (~85% penetration). iOS ~30%, Android ~70%. Hebrew localization is critical for market share. Key categories: fintech, transportation (Moovit, Gett), food delivery (Wolt, 10bis).

### Hebrew App Title and Subtitle
30 characters max. Include primary Hebrew keyword. Patterns: [Brand] - [Hebrew Descriptor], [Hebrew Name] [Category].

### Hebrew Keyword Research
Apple: 100 character keyword field. Separate with commas, no spaces. Include morphological variants and bilingual terms (transliterations like דליברי for delivery).

### RTL Screenshot Design
Text overlays must be RTL-aligned. Reading flow starts from RIGHT screenshot. Recommended fonts: Heebo, Rubik, Assistant. Include NIS prices.

### Hebrew App Description
Write in informal Hebrew. Include social proof: "מומלצת על ידי גלובס/כלכליסט". Address Israeli concerns: privacy, no hidden fees.

### Ratings and Reviews
Israeli users leave more negative reviews. Respond in Hebrew within 24-48 hours. Request ratings after positive in-app moments.

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
- `scripts/aso_keyword_analyzer.py` -- Analyzes Hebrew keyword density and suggests ASO improvements. Run: `python scripts/aso_keyword_analyzer.py --help`

### References
- `references/israeli-app-market.md` -- Israeli app market statistics, popular app categories, pricing benchmarks in NIS, and Hebrew keyword research data. Consult when researching Israeli app market or planning ASO strategy.

## Troubleshooting

### Error: "Hebrew keywords not ranking"
Cause: Hebrew keyword variations (with/without vav, different ktiv) not covered
Solution: Include both ktiv maleh and common misspellings. Hebrew users search with varied spelling -- add all common variants to keyword field.

### Error: "Screenshots show LTR interface"
Cause: App screenshots not localized for RTL
Solution: Create separate Hebrew screenshots showing the RTL version. Israeli users expect RTL interfaces -- LTR screenshots reduce conversion.
