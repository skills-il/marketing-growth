---
name: israeli-aso
description: Optimize mobile app listings for Israeli users on Apple App Store and Google Play with Hebrew metadata, keywords, and screenshots. Use when user asks about Israeli app store optimization, Hebrew app listing, Hebrew keywords for app store, or localizing app metadata for Israel. Covers Hebrew keyword research, RTL screenshot design, and category-specific benchmarks.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex, Antigravity, Gemini CLI.
---


# Israeli ASO

## Legal notice

This skill is guidance on App Store and Google Play listing policy and on writing Hebrew store
metadata. It is not legal advice. Store policies change without notice and are enforced by Apple
and Google at their discretion, so verify every rule against the official page linked in Reference
Links before you rely on it. Claims you make in a listing shown to Israeli consumers are also
subject to Israeli consumer-protection law, including the rules on misleading advertising; you, as
the app's publisher, remain responsible for them. If a claim in your listing is material to a
purchase decision, have it reviewed by a qualified professional rather than relying on this skill.

## Instructions

### Workflow
Run these in order. Steps 1 and 6 are the ones agents most often skip.

1. **Collect inputs:** the app's category, its English listing, whether it ships on iPad, and whether an Israeli price is displayed anywhere in the creative.
2. **Decide the localization scope** (see "Who actually sees the Hebrew listing" below). Hebrew alone is not the whole Israeli audience.
3. **Build the Hebrew term list** (see "Sourcing Hebrew keyword candidates").
4. **Budget the Apple keyword field** with `scripts/keyword_analyzer.py`, then assign terms to fields per store: Apple name / subtitle / keyword field; Play title / short description / full description.
5. **Write the Hebrew copy**, then spec the assets per device class (see "Required assets" and "Screenshot sizes").
6. **Clear the pre-publication gates** (see "Pre-publication gates"). Metadata alone does not make a listing submittable.
7. **Measure and iterate** (see "Where the data lives" and "A/B Testing").

### Sourcing Hebrew keyword candidates
Every example below starts from a Hebrew term list, and producing that list is the actual first task. Without a paid ASO tool, use:
- **Store search autocomplete in the IL storefront** with the device language set to Hebrew. Type a category root (משלוח, תקציב) and read the completions; they are the stores' own view of real queries.
- **Competitors' Hebrew names and subtitles**, which are visible on their product pages and are already keyword-optimized.
- **Your own in-app search logs and support tickets**, which show the words users actually type for your features.
- **Israeli press and category wording** (Globes, Calcalist, Ynet) for the term a general audience would recognize.

Do this by hand or with normal browsing. Do not script the stores, scrape them, or work around rate limiting or bot detection; it violates their terms and gets accounts closed.

### Who actually sees the Hebrew listing
A localized listing is served by the **user's language preference, not by their country**. Google states plainly that a user sees the translated version if their language preference matches a language you added. Apple's per-localization metadata behaves the same way, with a fallback to the primary language when nothing matches.

The consequence is the most commonly missed decision in Israeli ASO: a large share of Israeli users run their phone in English, and they will never see your Hebrew listing. They see the default one. So the Hebrew localization is an addition to the default listing, never a replacement for it, and if Israel is your main market the default/English listing needs optimizing for Israeli readers too. Shipping Hebrew-only leaves the listing most of your Israeli traffic sees untouched.

### Israeli Mobile Market
Israel had 10.4 million active cellular mobile connections at the end of 2025, equal to 109% of the population (GSMA Intelligence, via DataReportal), and 8.72 million internet users at 91.3% penetration (Kepios, October 2025). Do not quote the 8.72M/91.3% pair as a smartphone-user count, it measures internet users. Mobile OS split is Android 67.56% / iOS 32.44% (StatCounter, July 2026). Hebrew localization is critical for market share. Key categories: fintech, transportation (Moovit, Gett), food delivery (Wolt, 10bis).

### Hebrew App Title and Subtitle
30 characters max. Include primary Hebrew keyword. Patterns: [Brand] - [Hebrew Descriptor], [Hebrew Name] [Category].

### Hebrew Keyword Research
Apple: 100 character keyword field, terms separated by commas with no spaces between terms. Include bilingual terms (transliterations like דליברי for delivery).

Apple documents four rules here, and three of them are routinely got backwards:
- **Multi-word phrases ARE allowed.** Apple's own example is `Property,House,Real Estate`: spaces separate words *within* a phrase, commas separate terms. Do not strip every space on the belief that only single words are permitted.
- **Do not repeat any word already in the app name, subtitle, or primary category.** Those are indexed already, so a repeat spends budget for nothing. On a Hebrew listing this is easy to miss, because the Hebrew title and the Hebrew keyword field are usually written at different times.
- **Do not add plurals of words you already included.** Apple treats them as duplicates ("climbs" and "climb"). This is documented for English; Apple does not publish how its stemmer treats Hebrew, where משלוח and משלוחים are entirely different strings. Do not assume either way, spend budget on ktiv maleh/chaser spelling variants first (those really are different strings) and treat a Hebrew plural as a hypothesis to test, not a free win.
- **Skip generic terms** too broad for your category ("app", "game"), **filler words** ("the", "to"), and **special characters** unless they are part of your brand.

Promotional text (170 characters, editable without a new build) does not affect search ranking, so do not spend keywords there.

### Where Each Platform Pulls Keywords From
The two stores index different fields, so the same Hebrew metadata is not interchangeable:

- **Apple App Store**: the text-relevance inputs Apple documents are the app name, the subtitle, the keyword field, and the **primary category**. The description is not among them, so keywords placed only in the description do nothing for Apple search. Note that Apple states the inputs rather than publishing an exhaustive index, so treat this as "the description is not a documented ranking input", not as a guarantee it is never read.
- **The Apple keyword field is per-localization.** The Hebrew (`he`) localization gets its own separate 100-character keyword field, independent of the English field. Hebrew keywords do not compete with English ones for character budget, and English keywords do not rank you for Hebrew searches. Fill the Hebrew field with Hebrew terms only.
- **Google Play** has no keyword field. It indexes the title, the short description, and the full 4,000-character description. On Play, keyword research feeds directly into how you write the Hebrew description, and repetition density in the description matters.

### RTL Screenshot Design
Text overlays must be RTL-aligned. Reading flow starts from RIGHT screenshot. Recommended fonts: Heebo, Rubik, Assistant. Include NIS prices.

Screenshot sizes (verify against Apple's screenshot specifications page in Reference Links before export):
- **Apple, iPhone 6.9" display class:** upload one to 10 screenshots. The class accepts 1320 x 2868, 1290 x 2796, or 1260 x 2736 px portrait (the last is the iPhone Air). There is no longer a separate 6.7" class, so do not budget a second export for 1290 x 2796, it belongs to this class. The 6.5" class is required only if you do NOT provide 6.9" screenshots; provide 6.9" and Apple scales down.
- **Apple, iPad 13":** 2064 x 2752 or 2048 x 2732 px portrait. Required if the app runs on iPad.
- **Google Play, publication minimum:** at least TWO screenshots across device types, minimum dimension 320 px, maximum 3840 px, and the long side may not exceed twice the short side. Up to 8 screenshots per device type.
- **Google Play, tablet and Chromebook:** a different spec from phone, minimum 4 screenshots between 1,080 and 7,680 px, 16:9 landscape or 9:16 portrait. Do not carry the phone numbers across.
- **Google Play, promotion-eligibility bar (a different, higher bar):** to be eligible for Play's recommendation formats an app needs at least FOUR screenshots at 1080 px or better, 9:16 portrait (1080 x 1920) or 16:9 landscape (1920 x 1080). Treat 1080 x 1920 as the target, not as the publication minimum.
- **Google Play feature graphic (required to publish, and often forgotten):** 1024 x 500 px, JPEG or 24-bit PNG with NO alpha channel. A Hebrew listing has no feature graphic until you upload one, and the listing cannot go live without it. It also carries Hebrew overlay text, so it needs the same RTL treatment as the screenshots.

### Required assets (a listing does not publish without these)
Both stores block publication on assets that a metadata-only workflow forgets. Note the alpha-channel rule **inverts between Play's icon and everything else**, which is the single most common export error:

| Asset | Store | Spec |
|---|---|---|
| App icon | Google Play | 512 x 512 px, **32-bit PNG WITH alpha**, max 1024 KB. Required to publish. |
| Feature graphic | Google Play | 1024 x 500 px, JPEG or 24-bit PNG, **no alpha**. Required to publish. |
| Screenshots | Google Play | JPEG or 24-bit PNG, **no alpha**. See sizes below. |
| App icon | Apple | 1024 x 1024 px, **no alpha or transparency**. |
| Screenshots | Apple | .jpg / .jpeg / .png, **no alpha or transparency**. |

The Play feature graphic usually carries Hebrew overlay text, so it needs the same RTL treatment as the screenshots. It is routinely left in English on an otherwise fully localized listing.

### Pre-publication gates
Metadata does not make a listing submittable. Before a Hebrew listing can go live:
- **Apple:** App Privacy details must be completed in App Store Connect; Apple states this is required to submit new apps and app updates. A Privacy Policy URL is required for iOS apps.
- **Google Play:** the App content page requires a privacy policy, the content rating questionnaire, and a target-audience and content declaration, plus declarations for ads and any sensitive permissions.

These are per-app, not per-localization, but they gate the release that carries your Hebrew listing.

### Editability: what you can fix this week and what waits for a release
App Store Connect distinguishes properties that can be edited at any time from those that ship with an app version. Promotional text (170 characters) is editable without submitting a new build; the app name, subtitle, keyword field, description and screenshots are version properties. Check the "Required, localizable, and editable properties" reference before you plan a fix, because it decides whether a wrong Hebrew keyword field is a same-day correction or waits for your next submission. Treat the 100-character Hebrew keyword field accordingly: it is the field you are least able to correct in a hurry.

### Where the data lives
This skill tells you to test rather than assume several times. The evidence lives in **App Store Connect App Analytics**, filtered to the App Store Search source, and in the **Play Console store-listing acquisition reports**. If you cannot see those numbers, the honest answer is that the hypothesis is untested, not that it is true.

### Hebrew App Description
Write in informal Hebrew. Include social proof: "מומלצת על ידי גלובס/כלכליסט". Address Israeli concerns: privacy, no hidden fees.

### Ratings and Reviews
Israeli reviewers have a reputation for bluntness. Treat that as practitioner folklore rather than a measured fact, but the operational consequence holds regardless: a single unanswered 1-star review reads as a red flag to the next Israeli browsing the listing, because ratings and reviews are a documented App Store ranking input alongside downloads. Respond in Hebrew within 24-48 hours. Trigger the rating prompt after a clear in-app win (a completed order, a saved document), never mid-task.

### A/B Testing and Conversion Optimization
Keywords and screenshots drive visibility; native store experiments prove what actually converts. Use the free built-in tools rather than guessing:
- **Apple Product Page Optimization (PPO):** test up to 3 treatments against the original for 90 days or until you stop it (icon, screenshots, app previews). PPO is iOS/iPadOS only and cannot be run on a custom product page. Each treatment can be localized to selected languages, which is how you run a Hebrew-only test. Budget for the arithmetic: Israel-only traffic split across treatments may not reach significance inside the 90-day cap, and Apple notes results take longer depending on the localizations selected. If the volume is not there, prefer a sequential change with before/after measurement over an underpowered test. Pair it with **Custom Product Pages** (up to 70 per app) to show different Hebrew screenshots or messaging to different ad campaigns; custom pages now also surface in organic search.
- **Google Play store-listing A/B tests** (Play Console: Grow users > Store presence > Store listings, "Experiment" column; the help article is now titled "Run A/B tests on your store listing"). Two types, and the difference decides whether you can test Hebrew text at all:
  - a **default graphics experiment** tests the icon, feature graphic, and screenshots in the listing's default language, and **cannot test text**;
  - a **localized experiment** tests icon, feature graphic, screenshots and/or descriptions, in up to five languages.
  To test Hebrew copy you must run a LOCALIZED experiment on the Hebrew listing. You may run one default graphics experiment or up to five localized experiments at a time, with up to 2 variants against the current listing. ("Global experiments" is the retired name for default graphics experiments.)

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
- `scripts/keyword_analyzer.py` -- De-dupes your Hebrew base keywords, builds the comma-no-space Apple keyword field, and reports the 100-character budget (it warns on overflow instead of truncating). Feed it your terms (single words or multi-word phrases, both are permitted) plus your own ktiv maleh/chaser spelling variants. It reminds you that Apple treats plurals of included words as duplicates, so do not pad the list with plurals by reflex. It does NOT validate your terms: it will not detect an attached-prefix form (המשלוח), a word you already used in the title, or a plural, so those judgement calls stay with you. `--prefixes` only prints prefix forms so you can see what they would cost. Run: `python scripts/keyword_analyzer.py --keywords "דליברי,משלוחים,אוכל"` or `python scripts/keyword_analyzer.py --help`

### References
- `references/israeli-app-market.md` -- Israeli mobile market figures with sources, the top app categories and who operates in them, per-store field limits and asset specs, Hebrew keyword seed terms by category with the ktiv/prefix budget rules, and how ILS pricing display works. Consult in step 3 of the workflow when building the Hebrew term list, and in step 5 when specing assets.

## Recommended MCP Servers

No MCP server applies to this skill. Hebrew keyword research, RTL screenshot planning, and metadata writing are reasoning tasks the agent performs directly with the bundled script and reference file. There is no App Store Connect or Google Play API in the skills-il MCP directory that this workflow depends on.

## Gotchas

- Hebrew has two spelling conventions (ktiv maleh and ktiv chaser) that produce different search terms. Agents may optimize for only one spelling, missing users who search the other way.
- The Apple keyword field is 100 characters, with commas separating terms and no space AFTER a comma. Agents waste budget on spaces after commas. They also over-correct: spaces are legitimate INSIDE a multi-word phrase (Apple's own example is `Property,House,Real Estate`), so stripping every space breaks phrases the field supports.
- Israeli app store screenshots must flow right-to-left. The first screenshot users see is the rightmost one. Agents may arrange screenshots in LTR reading order.
- NIS pricing must appear on screenshots and descriptions. Agents may default to USD pricing, which reduces trust with Israeli users.
- Israeli Android market share (67.56%) is roughly double iOS (32.44%, StatCounter July 2026). Agents trained on US data may over-index on App Store optimization and under-invest in Google Play.
- Google Play bans text suggesting store performance, ranking, awards, testimonials, or price and promotion, naming "Best", "#1", "Top", "New", "Free", "Discount", "Sale" and "Million Downloads" on its preview-assets guidance, plus calls to action ("Download now", "Install now"), emojis and ALL-CAPS unless part of the brand name. The ban is NOT limited to the title: it also covers the short description, the full description, the screenshots and the feature graphic. Hebrew equivalents count, so "האפליקציה הכי טובה", "חדש", "חינם" and "הורידו עכשיו" are all exposed, including when they sit as overlay text baked into a Hebrew screenshot. Agents typically sanitize the title and leave the screenshots untouched.
- Agents may reach for Apple's App Store "app tags" as an Israeli discovery lever. They are not one: tags are currently displayed only in the United States storefront and are derived from en_US metadata, so they do nothing for a Hebrew IL listing. Spend the effort on the Hebrew keyword field instead.
- Play screenshots and graphic assets take alt text, which is read by assistive technology. Hebrew alt text is routinely left empty or left in English when a listing is localized.

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
Cause: likeliest cause is that ktiv maleh and ktiv chaser produce different strings and only one is in the field. Not confirmed as the cause in any individual case, because neither store publishes how it stems Hebrew.
Solution: Add the alternate ktiv spelling first, it is the variant most likely to be a genuinely separate string. Do not try to add "all common variants": at 100 characters you cannot, and Apple counts plurals of words you already included as duplicates. Verified NOT to be the cause: a space after a comma (wasteful, but it does not stop indexing) and a missing English keyword (the Hebrew field is independent). Confirm against App Store Connect App Analytics search terms before adding more spellings.

### Error: "Screenshots show LTR interface"
Cause: App screenshots not localized for RTL
Solution: Create separate Hebrew screenshots showing the RTL version. Israeli users expect RTL interfaces -- LTR screenshots reduce conversion.
