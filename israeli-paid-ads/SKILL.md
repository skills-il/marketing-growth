---
name: israeli-paid-ads
description: >-
  Create and optimize paid advertising campaigns for the Israeli market across
  Google Ads, Meta (Facebook/Instagram), and local platforms. Use when user asks
  about Israeli PPC, Hebrew ad copy, Israeli audience targeting, or ad budget
  optimization. Covers Hebrew keyword research, Israeli Consumer Protection Law
  ad regulations, local bidding strategies, and audience segmentation.
license: MIT
compatibility: >-
  Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
metadata:
  author: skills-il
  version: 1.0.1
  category: marketing-growth
  tags:
    he:
      - פרסום-ממומן
      - גוגל-אדס
      - מטא
      - PPC
      - קידום-ממומן
      - שיווק-דיגיטלי
    en:
      - paid-ads
      - google-ads
      - meta
      - ppc
      - paid-promotion
      - digital-marketing
  display_name:
    he: "פרסום ממומן ישראלי"
    en: "Israeli Paid Ads"
  display_description:
    he: >-
      יצירת קמפיינים ממומנים בגוגל ומטא לשוק הישראלי עם קופי בעברית, מחקר
      מילות מפתח, ציות לחוק הגנת הצרכן ואסטרטגיות הצעת מחיר
    en: >-
      Create and optimize paid advertising campaigns for the Israeli market
      across Google Ads, Meta (Facebook/Instagram), and local platforms. Use
      when user asks about Israeli PPC, Hebrew ad copy, Israeli audience
      targeting, or ad budget optimization. Covers Hebrew keyword research,
      Israeli Consumer Protection Law ad regulations, local bidding strategies,
      and audience segmentation.
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
    - antigravity
---

# Israeli Paid Ads

## Instructions

### Choose Platform and Campaign Type
Google Ads (Search) for high-intent traffic, Meta (Facebook) for B2C with ~6.5M Israeli users, Instagram for lifestyle, LinkedIn for B2B, TikTok for Gen Z.

### Hebrew Keyword Research
Hebrew is morphologically rich; target all inflections of root words. Use Google Keyword Planner with Israel location. Check both Hebrew and English variants.

### Write Hebrew Ad Copy
Headlines: up to 30 characters. Use informal register. Price transparency and local trust signals work well. Include phone number extensions.

### Israeli Audience Targeting
Gush Dan (~40% of ad spend), mobile-first (>70%), avoid Shabbat hours. Military service shifts age demographics.

### Ad Regulations (Chok Haganat HaTzarchan)
Prices must include VAT (18%). Sponsored content must be labeled. Health and financial claims have stricter requirements.

### Budget and Bidding
Israeli CPC benchmarks by vertical: Legal 15-40 NIS, Insurance 10-30 NIS, Ecommerce 2-8 NIS. Start with Manual CPC, switch to Target CPA after 30+ conversions.

## Examples

### Example 1: Set Up Hebrew Google Ads Campaign
User says: "Create a Google Ads campaign targeting Israeli customers"
Actions:
1. Set campaign location to Israel, language Hebrew + English
2. Write Hebrew ad copy (30 chars headline, 90 chars description)
3. Set budget in NIS, expect CPC of 2-8 NIS (varies by industry)
4. Add Hebrew negative keywords to avoid wasted spend
5. Set up conversion tracking with NIS values (include 18% VAT in ROAS)
Result: Hebrew Google Ads campaign with Israeli market targeting

### Example 2: Launch Facebook Ads for Israeli Audience
User says: "Create Facebook ad campaigns for our Israeli restaurant chain"
Actions:
1. Target: Israel, age 25-54, Hebrew speakers, food interests
2. Create Hebrew ad copy with local references and NIS pricing
3. Use carousel format with Hebrew RTL text overlays
4. Set daily budget in NIS, expect CPM of 15-40 NIS
5. Schedule ads for Israeli peak hours (Sunday-Thursday evenings)
Result: Localized Facebook campaign targeting Israeli food audience

## Bundled Resources

### Scripts
- `scripts/cpc_calculator.py` -- Calculates CPC benchmarks and budget estimates for Israeli ad campaigns. Run: `python scripts/cpc_calculator.py --help`

### References
- `references/israeli-ad-benchmarks.md` -- Israeli digital advertising benchmarks by industry, platform CPCs in NIS, VAT implications, and regulatory requirements. Consult when planning ad budgets or setting performance targets.

## Gotchas

- Israeli ad prices must include VAT (18%) by law under Chok Haganat HaTzarchan (Consumer Protection Law). Agents may generate ad copy with pre-VAT prices, which violates Israeli advertising regulations.
- ROAS calculations must account for 18% VAT on ad spend. If you spend 1,000 NIS on ads, the true cost is 1,180 NIS. Agents often calculate ROAS without this adjustment.
- The Gush Dan metropolitan area (Tel Aviv area) accounts for approximately 40% of Israeli digital ad spend. Agents may set nationwide targeting when the business only serves a specific region, wasting budget.
- Israeli ad scheduling must avoid Shabbat (Friday afternoon through Saturday evening). Agents may run campaigns 24/7 and burn budget during zero-engagement hours.
- Hebrew ad headlines have a 30-character limit in Google Ads, but Hebrew words are often shorter than English equivalents. Agents may not take advantage of the extra room available in Hebrew headlines.

## Troubleshooting

### Error: "Hebrew ad text truncated"
Cause: Hebrew characters may have different display widths than Latin
Solution: Test ad preview in Hebrew. Google Ads headline limit is 30 characters -- Hebrew words are often shorter. Use the ad preview tool to verify display.

### Error: "VAT not accounted for in ROAS calculation"
Cause: Israeli ads charge 18% VAT which affects true cost
Solution: Always calculate ROAS including VAT. If ad spend is 1,000 NIS, true cost is 1,180 NIS. Set ROAS targets accordingly.
