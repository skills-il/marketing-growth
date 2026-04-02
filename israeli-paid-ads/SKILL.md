---
name: israeli-paid-ads
description: Create and optimize paid advertising campaigns for the Israeli market across Google Ads, Meta (Facebook/Instagram), and local platforms. Use when user asks about Israeli PPC, Hebrew ad copy, Israeli audience targeting, or ad budget optimization. Covers Hebrew keyword research, Israeli Consumer Protection Law ad regulations, local bidding strategies, and audience segmentation.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---

# Israeli Paid Ads

## Instructions

### Step 1: Choose Platform and Campaign Type

Select the right platform based on business type, audience, and campaign objective. Each platform serves a different role in the Israeli digital ad ecosystem.

| Platform | Best For | Israeli Audience | Avg CPM (NIS) | Ad Formats |
|----------|----------|------------------|---------------|------------|
| Google Ads (Search) | High-intent traffic, lead gen | ~95% search market share in Israel | N/A (CPC model) | Text ads, responsive search ads |
| Google Ads (Display) | Brand awareness, retargeting | Google Display Network reach in IL | 5-15 | Banner, responsive display |
| Meta (Facebook) | B2C, community, local business | ~7.6M Israeli users | 15-40 | Image, video, carousel, collection |
| Instagram | Lifestyle, fashion, food, travel | ~4.5M Israeli users | 20-50 | Stories, reels, feed, shopping |
| LinkedIn | B2B, SaaS, enterprise, recruiting | ~3M Israeli professionals | 40-120 | Sponsored content, InMail, lead gen |
| TikTok | Gen Z, viral content, brand awareness | Growing Israeli user base (18-34) | 10-30 | In-feed video, branded effects |

**Campaign type selection guide:**

- **Lead generation**: Google Search Ads (high intent) or Meta Lead Ads (lower cost per lead, lower intent)
- **E-commerce sales**: Google Shopping + Meta Dynamic Product Ads (DPA)
- **App installs**: Meta App Install campaigns or Google App campaigns (UAC)
- **Brand awareness**: YouTube pre-roll, Meta reach campaigns, TikTok
- **Local business**: Google Local campaigns, Meta radius targeting around the business
- **B2B**: LinkedIn Sponsored Content + Google Search for branded/non-branded terms

### Step 2: Hebrew Keyword Research

Hebrew is a morphologically rich language with root-based word formation. A single root (shoresh) produces dozens of inflections, and keyword tools may not group them automatically. Thorough keyword research requires covering all variants.

**Hebrew morphology considerations:**

| Pattern | Example Root | Inflections to Target |
|---------|-------------|----------------------|
| Verb conjugations | ל.מ.ד (learn) | לומד, לומדת, לומדים, ללמוד, למד, ילמד |
| Noun forms | ב.ט.ח (insure) | ביטוח, ביטוחים, מבוטח, מבוטחת |
| Construct state (smichut) | | ביטוח רכב, ביטוח בריאות, ביטוח חיים |
| With/without definite article | | ביטוח vs הביטוח |
| Colloquial spelling | | אינטרנט vs אינטרנת |

**Keyword research process:**

1. **Seed keywords**: Start with 5-10 core terms in Hebrew. Include both formal and colloquial forms. Many Israelis search in English for tech terms (e.g., "CRM" not "ניהול קשרי לקוחות").
2. **Expand with Google Keyword Planner**: Set location to Israel, language to Hebrew. Export suggestions and group by intent (informational, commercial, transactional).
3. **Check English variants**: Israeli users frequently search in English or transliterated Hebrew (e.g., "ramzor" for רמזור). Add these as separate ad groups.
4. **Negative keywords in Hebrew**: Build a negative keyword list early. Common Hebrew negatives: "חינם" (free), "מה זה" (what is), "השוואה" (comparison, if not relevant).
5. **Competitor analysis**: Search your main keywords on google.co.il and note which competitors are bidding. Check their ad copy for messaging angles you can differentiate from.

**Tools for Hebrew keyword research:**

- Google Keyword Planner (set region: Israel)
- Google Trends (compare Hebrew vs English search volume for the same concept)
- Google Search Console (existing site query data)
- Ahrefs/Semrush (limited Hebrew support, but useful for competitor gap analysis)

### Step 3: Write Hebrew Ad Copy

Hebrew ad copy requires attention to character limits, RTL formatting, register, and cultural norms. Israeli consumers respond well to direct, informal communication with clear pricing.

**Google Ads character limits (apply equally to Hebrew):**

| Element | Character Limit | Hebrew Tip |
|---------|----------------|------------|
| Headline 1-15 | 30 chars each | Hebrew words are shorter on average, giving more room |
| Description 1-4 | 90 chars each | Use informal register, include NIS pricing |
| Display URL path | 15 chars each | Use Hebrew slugs: /ביטוח-רכב |
| Sitelink title | 25 chars | Short Hebrew CTAs: "קבלו הצעה", "צרו קשר" |
| Callout | 25 chars | "משלוח חינם", "אחריות שנתיים" |

**Hebrew ad copy best practices:**

1. **Use informal register (guf sheni)**: Address the reader as "אתה/את" not "אתם". Israeli ads use casual, direct language. Example: "מחפש ביטוח רכב? קבל הצעת מחיר תוך דקה" (not "המעוניינים בביטוח רכב מוזמנים...").
2. **Include prices with VAT**: Israeli law requires all advertised prices to include 18% VAT. Always show the final price in NIS. Example: "החל מ-99 ש\"ח לחודש (כולל מע\"מ)".
3. **Add local trust signals**: "חברה ישראלית", "שירות בעברית", "משלוח בכל הארץ", phone number with Israeli prefix (0X-XXXXXXX or *number).
4. **Use phone extensions**: Israelis prefer calling businesses directly. Add call extensions with local numbers. Click-to-call performs well on mobile.
5. **RTL preview**: Always preview ads in the Google Ads interface to verify Hebrew text renders correctly. Pay attention to mixed Hebrew/English strings (e.g., brand names, numbers) which may reorder in RTL context.

**Meta (Facebook/Instagram) ad copy:**

- Primary text: 125 chars visible before "See more" (Hebrew counts the same)
- Headline: 27 chars visible in feed (40 max)
- Use emojis strategically (they work well in Israeli Facebook ads)
- Include a clear CTA in Hebrew: "הזמינו עכשיו", "קבלו הנחה", "הצטרפו אלינו"

### Step 4: Israeli Audience Targeting

Israeli audience targeting requires understanding the country's unique geographic, demographic, and behavioral patterns.

**Geographic targeting:**

| Region | Population Share | Ad Spend Share | Notes |
|--------|-----------------|---------------|-------|
| Gush Dan (Tel Aviv metro) | ~40% | ~40-45% | Highest competition, highest CPCs |
| Haifa and North | ~20% | ~15% | Lower CPCs, more Hebrew-dominant |
| Jerusalem | ~12% | ~10% | Mixed Hebrew/Arabic, unique demographics |
| Be'er Sheva and South | ~15% | ~10% | Lower competition, lower CPCs |
| Judea and Samaria | ~5% | ~5% | Requires careful geo-targeting |

**Demographic targeting notes:**

- **Military service gap**: Israelis serve in the IDF from age 18-21 (men) or 18-20 (women). Purchasing power and consumer behavior differ significantly from other countries in this age range. Adjust age targeting accordingly: the "young professional" segment starts at 22-23 in Israel, not 18.
- **Shabbat scheduling**: Most Israeli consumers are inactive Friday afternoon (14:00) through Saturday evening (20:00). Pause or reduce bids during these hours to avoid wasted spend. Exception: secular audiences in Tel Aviv may still be active.
- **Holiday calendar**: Israeli holidays (Rosh Hashana, Yom Kippur, Sukkot, Pesach) follow the Hebrew calendar and shift dates yearly. Pause campaigns on Yom Kippur. Adjust budgets before holidays (pre-holiday shopping spikes are common).
- **Mobile-first**: Over 70% of Israeli web traffic is mobile. Design ads and landing pages for mobile first. Use vertical video formats for Meta and TikTok.

**Behavioral targeting on Meta:**

- Interest-based: Target Hebrew speakers, Israeli TV shows, local brands, Israeli news outlets
- Lookalike audiences: Build from Israeli customer lists (minimum 100 users from Israel)
- Custom audiences: Upload customer phone lists (Israeli format: 05X-XXXXXXX)

### Step 5: Ad Regulations (Chok Haganat HaTzarchan)

Israeli advertising is regulated primarily by the Consumer Protection Law (חוק הגנת הצרכן, 1981) and its amendments. Non-compliance can result in fines and criminal penalties. See `references/israeli-ad-regulations.md` for the full regulatory reference.

**Mandatory requirements:**

| Requirement | Details | Penalty |
|-------------|---------|---------|
| VAT-inclusive pricing | All advertised prices must include 18% VAT | Fine + ad takedown |
| Sponsored content labeling | Must display "פרסומת" or "תוכן ממומן" | Fine per violation |
| Accurate claims | No misleading statements about product/service | Criminal penalties possible |
| Comparative advertising | Allowed only if claims are verifiable and accurate | Lawsuit + fine |

**Category-specific restrictions:**

| Category | Requirement |
|----------|-------------|
| Financial services | Must include risk disclaimers ("השקעה כרוכה בסיכון") |
| Health/Medical | Cannot promise cures, must include disclaimers |
| Alcohol | No targeting of minors, must include health warnings |
| Gambling/Lottery | Requires license from Israeli authority |
| Food | Nutrition and health claims must be verified |
| Real estate | Must specify if prices exclude VAT for new construction |

**Influencer marketing rules:**

Israeli law requires influencers to clearly disclose paid partnerships. Use #פרסומת or #תוכן_ממומן in Hebrew posts. The disclosure must be visible without clicking "more" or scrolling.

**Landing page compliance:**

- Landing page prices must match ad prices (both VAT-inclusive)
- "Terms and conditions" links must be in Hebrew
- Return/cancellation policy must be accessible (14-day cancellation right under Israeli law)
- Privacy policy required for any data collection

### Step 6: Budget and Bidding

**Israeli CPC benchmarks by vertical (2025-2026 benchmarks, verify current rates):**

| Vertical | CPC Range (NIS) | Avg CPC (NIS) | Competition Level |
|----------|----------------|---------------|-------------------|
| Legal | 15-40 | 25 | Very High |
| Finance | 10-35 | 20 | Very High |
| Insurance | 10-30 | 18 | High |
| Real Estate | 8-25 | 15 | High |
| SaaS/Tech | 5-20 | 12 | Medium-High |
| Health | 5-18 | 10 | Medium |
| Travel | 3-15 | 8 | Medium |
| Education | 3-12 | 7 | Medium |
| E-commerce | 2-8 | 4 | Low-Medium |
| Food | 2-6 | 3 | Low |

**Budget planning with the bundled calculator:**

Use the bundled `scripts/cpc_calculator.py` to estimate campaign costs:

```bash
# Show all vertical benchmarks
python scripts/cpc_calculator.py --benchmarks

# Estimate campaign for e-commerce with 5,000 NIS budget
python scripts/cpc_calculator.py --vertical ecommerce --budget 5000

# Custom CPC estimate
python scripts/cpc_calculator.py --vertical legal --budget 10000 --cpc 30
```

The calculator automatically accounts for 18% VAT when computing effective budget and estimates conversions at multiple conversion rates (1%, 2%, 3%, 5%).

**Bidding strategy progression:**

| Stage | Strategy | When to Use |
|-------|----------|-------------|
| Launch (Week 1-2) | Manual CPC | Gathering data, fewer than 15 conversions |
| Learning (Week 3-4) | Enhanced CPC | 15-30 conversions, letting Google adjust |
| Optimization (Month 2+) | Target CPA | 30+ conversions, stable conversion rate |
| Scale (Month 3+) | Target ROAS | Sufficient revenue data, e-commerce focused |
| Max performance | Maximize Conversions | High budget, broad targeting, trust the algorithm |

**VAT impact on ROAS:**

All ROAS calculations in Israel must account for 18% VAT on ad spend. Example:

- Ad spend: 1,000 NIS (your invoice from Google/Meta)
- True cost including VAT: 1,180 NIS
- Revenue generated: 5,000 NIS
- Naive ROAS: 5,000 / 1,000 = 5.0x (incorrect)
- True ROAS: 5,000 / 1,180 = 4.24x (correct for Israeli reporting)

**Monthly budget minimums (recommended):**

| Platform | Minimum Monthly (NIS) | Recommended Monthly (NIS) |
|----------|----------------------|--------------------------|
| Google Search | 1,500 | 5,000-15,000 |
| Google Display | 1,000 | 3,000-8,000 |
| Meta (Facebook) | 1,000 | 3,000-10,000 |
| LinkedIn | 3,000 | 8,000-20,000 |
| TikTok | 1,500 | 4,000-10,000 |

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

### Example 3: Calculate Campaign Budget
User says: "How much should I spend on Google Ads for my Israeli law firm?"
Actions:
1. Run `python scripts/cpc_calculator.py --vertical legal --budget 10000` to estimate clicks and conversions
2. Legal vertical CPC range: 15-40 NIS (avg 25 NIS), so 10,000 NIS budget yields ~340 clicks after VAT
3. At 3% conversion rate: ~10 leads per month at ~1,000 NIS per lead
4. Recommend starting with 8,000-12,000 NIS/month, scaling based on CPA targets
5. Set up Manual CPC bidding initially, move to Target CPA after accumulating 30+ conversions
Result: Data-driven budget recommendation with conversion estimates

## Bundled Resources

### Scripts
- `scripts/cpc_calculator.py` -- Calculates CPC benchmarks and budget estimates for Israeli ad campaigns. Supports all major verticals with min/avg/max CPC data. Automatically accounts for 18% VAT. Run: `python scripts/cpc_calculator.py --help`

### References
- `references/israeli-ad-regulations.md` -- Israeli advertising regulations including Consumer Protection Law requirements, digital advertising rules, restricted categories, Shabbat scheduling best practices, and audience targeting tips. Consult when verifying ad compliance or planning campaign schedules.

## Gotchas

- Israeli ad prices must include VAT (18%) by law under Chok Haganat HaTzarchan (Consumer Protection Law). Agents may generate ad copy with pre-VAT prices, which violates Israeli advertising regulations.
- ROAS calculations must account for 18% VAT on ad spend. If you spend 1,000 NIS on ads, the true cost is 1,180 NIS. Agents often calculate ROAS without this adjustment.
- The Gush Dan metropolitan area (Tel Aviv area) accounts for approximately 40% of Israeli digital ad spend. Agents may set nationwide targeting when the business only serves a specific region, wasting budget.
- Israeli ad scheduling must avoid Shabbat (Friday afternoon through Saturday evening). Agents may run campaigns 24/7 and burn budget during zero-engagement hours.
- Hebrew ad headlines have a 30-character limit in Google Ads, but Hebrew words are often shorter than English equivalents. Agents may not take advantage of the extra room available in Hebrew headlines.
- Hebrew keyword research must account for morphological variants. A single root can produce dozens of word forms. Agents may target only one inflection and miss significant search volume from other forms.
- Mixed Hebrew/English text in ads can reorder unexpectedly in RTL rendering. Always preview ads in the platform's ad preview tool before publishing.

## Troubleshooting

### Error: "Hebrew ad text truncated"
Cause: Hebrew characters may have different display widths than Latin characters in certain fonts.
Solution: Test ad preview in Hebrew using the platform's built-in preview tool. Google Ads headline limit is 30 characters, and Hebrew words are often shorter than English equivalents, so you likely have room to expand. Check for mixed Hebrew/English strings that may cause unexpected RTL reordering.

### Error: "VAT not accounted for in ROAS calculation"
Cause: Israeli ads charge 18% VAT which affects true cost and distorts ROAS if not included.
Solution: Always calculate ROAS including VAT. If ad spend is 1,000 NIS, true cost is 1,180 NIS. Adjust ROAS targets accordingly. Use the formula: True ROAS = Revenue / (Ad Spend * 1.18).

### Error: "Low click-through rate on Hebrew ads"
Cause: Ad copy may be too formal or translated literally from English, which does not resonate with Israeli audiences.
Solution: Rewrite ads in natural conversational Hebrew. Use informal register (guf sheni: "אתה/את"), include NIS pricing with VAT, and add local trust signals like "חברה ישראלית" or a local phone number. Test 3-5 headline variations.

### Error: "Campaign spending but no conversions"
Cause: Common in the first 2 weeks of a new campaign, or due to targeting/landing page issues.
Solution: Check that the landing page is in Hebrew, loads fast on mobile, and has a clear CTA. Verify conversion tracking fires correctly. Review search terms report for irrelevant queries and add negative keywords. If targeting Gush Dan only, ensure radius is not too narrow. Allow 2-4 weeks of data before making major changes.
