# Israeli Mobile App Market

## Market Overview
- 10.4M active cellular mobile connections at end-2025, 109% of population (GSMA Intelligence via DataReportal Digital 2026 Israel). Connections exceed people because many hold more than one line; this is NOT a smartphone-user count.
- 8.72M internet users, 91.3% penetration (Kepios, October 2025). Do not relabel this figure as smartphone users.
- Android 67.56%, iOS 32.44% (StatCounter, July 2026)

## Top App Categories in Israel
| Category | Key Players | Notes |
|----------|------------|-------|
| Fintech | Bank Hapoalim, Leumi, bit, PayBox | Mobile banking very mature |
| Transport | Moovit, Gett, Yango | Moovit founded in Israel. Yango's apps are now published by post-Yandex Yango Group entities, the brand name is unchanged but the owner is not. |
| Food Delivery | Wolt, 10bis (תן ביס), Cibus Pluxee | Corporate meal cards huge. Cibus rebranded to Cibus Pluxee under Pluxee Israel Ltd; cibus.co.il no longer resolves and the site is now cibus.pluxee.co.il. Do not write "Cibus" alone as the current brand. |
| Shopping | Zap, KSP, iHerb | Price comparison culture |
| News | Ynet, Walla, Haaretz | Hebrew content essential |

## Apple App Store (Israel)
- Keyword field: 100 characters, per-localization (the Hebrew localization has its own separate field)
- Title: 30 characters
- Subtitle: 30 characters
- Documented text-relevance inputs: app name, subtitle, keyword field, primary category. The description is not among them. Apple states inputs rather than publishing an exhaustive index.
- Localization: he (Hebrew), the App Store Connect shortcode. Apple does not publish how far a Hebrew keyword set carries beyond the Israel storefront, so plan the Hebrew field to stand on its own rather than relying on cross-storefront carryover. Do not assert a carryover rule either way, it is undocumented.
- Currency: ILS (₪)

## Google Play (Israel)
- Title: 30 characters. Banned across title, icon, developer name, short description, full description, screenshots and feature graphic: text suggesting store performance/ranking/awards/testimonials or price and promotion ("Best", "#1", "Top", "New", "Free", "Discount", "Sale", "Million Downloads"), calls to action ("Download now"), emoji, and ALL-CAPS unless part of the brand name.
- Short description: 80 characters. Pack the primary Hebrew keyword here.
- Full description: 4,000 characters. Character limits count full-width and half-width characters alike.
- Feature graphic: 1024 x 500 px, JPEG or 24-bit PNG with no alpha. REQUIRED to publish the store listing.
- There is no separate keyword field. Google does not publish which fields it indexes for search, so treat "title + short description + full description are what Play indexes" as practitioner consensus, not as a documented rule; Google states only that unnecessary keywords "will not impact ranking".
- Localization: Google Play Console uses `iw-IL` for Hebrew. `iw` is the legacy ISO 639 alias; `he` / `he-IL` is the modern standard code, but the Console listing still shows and accepts `iw-IL`. Verify the exact code in the current Play Console UI.
- Keywords extracted from the description text

## Screenshot Dimensions
- Apple accepts one to 10 screenshots per localization, .jpg/.jpeg/.png, no alpha channel or transparency.
- iPhone 6.9" display class: 1320 x 2868, 1290 x 2796, or 1260 x 2736 px portrait (1260 x 2736 is iPhone Air). There is no separate 6.7" class any more.
- iPhone 6.5" class: required only if 6.9" screenshots are not provided.
- iPad 13": 2064 x 2752 or 2048 x 2732 px portrait. Required if the app runs on iPad.
- Google Play publication minimum: two screenshots across device types, min dimension 320 px, max 3840 px, long side at most 2x the short side. Up to 8 per device type.
- Google Play promotion-eligibility bar: at least four screenshots at 1080 px+, 9:16 (1080 x 1920) portrait or 16:9 (1920 x 1080) landscape. This is a recommendation-eligibility threshold, not the publication minimum.
- Alt text is supported on Play screenshots and graphic assets; localize it to Hebrew.
- Text overlays: RTL aligned, Heebo/Rubik fonts
- Verify all sizes against Apple's screenshot specifications page before export, since required sizes shift with new device classes

## Hebrew Keyword Seed Terms by Category
Starting points only. Validate every term against IL-storefront search autocomplete with a Hebrew device language before spending budget on it, and check it is not already in your app name, subtitle or primary category.

| Category | Hebrew seed terms | Transliteration / bilingual forms users also type |
|---|---|---|
| Food delivery | משלוחים, משלוח, אוכל, מסעדות, הזמנת אוכל, טייק אווי | דליברי, טייקאווי |
| Fintech / budgeting | תקציב, הוצאות, חיסכון, ניהול כספים, מעקב הוצאות | בנקינג |
| Banking | בנק, עובר ושב, כרטיס אשראי, העברה בנקאית | |
| Transport | תחבורה ציבורית, אוטובוס, רכבת, מוניות, נסיעות | |
| Shopping / price comparison | השוואת מחירים, קניות, מבצעים, חנות | |
| Health | בריאות, קופת חולים, תורים, מרשמים | |
| News | חדשות, עדכונים, כתבות | |

Two Hebrew-specific budget rules, in priority order:
1. **Ktiv maleh vs ktiv chaser first** (משלוח / מישלוח). These are genuinely different strings and are the variant most likely to earn its characters.
2. **Attached stop-word prefixes last, or never** (ה, ו, ב, ל, מ, ש). Forms like המשלוח are not how people search and Apple lists filler words as budget waste.

Plurals sit between the two and are a judgement call: Apple documents that plurals of included words are treated as duplicates, but that is stated for English and Apple does not publish how it stems Hebrew, where משלוח and משלוחים are unrelated strings. Test before spending.

Israeli users routinely mix scripts, typing an English brand name inside an otherwise Hebrew query. Budget for a transliteration only where it is the form users actually type, which autocomplete will show you.

## Pricing Display in Israel
This file does not carry price benchmarks; category pricing moves too fast to freeze in a reference and no reliable public source for Israeli app-price medians was available at last review. What matters for the listing:
- Prices shown to Israeli users are configured for the IL storefront in App Store Connect / Play Console, in ILS (₪).
- A price baked into a screenshot image is a version property on Apple, so a price change needs a new submission to correct. Prefer showing value framing over a specific number in creative.
- Verify current tax treatment on the platform's own pricing and tax pages before printing any price in Hebrew creative.

