# Israeli Advertising Regulations

## Consumer Protection Law (Chok Haganat HaTzarchan)
- All prices MUST include VAT (18%)
- Sponsored content must be clearly labeled ("פרסומת" or "תוכן ממומן")
- Comparative advertising allowed but must be accurate
- Misleading advertising carries criminal penalties

## Digital Advertising Rules
- Facebook/Instagram: Must comply with Israeli labeling requirements
- Google Ads: Prices in NIS must include VAT
- Influencer marketing: Must disclose sponsored content (#ad #sponsored #פרסומת)

## Restricted Categories
| Category | Restriction |
|----------|------------|
| Alcohol | No ads targeting minors, health warnings |
| Gambling | Requires license, strict targeting |
| Financial | Risk disclaimers required |
| Health/Medical | Cannot promise cures, requires disclaimers |
| Food | Nutrition claims must be verified |

## Shabbat Advertising
- No legal restriction on digital ads during Shabbat
- But most Israeli businesses avoid scheduling during Shabbat hours
- Best practice: Pause campaigns Friday 14:00 - Saturday 20:00
- Yom Kippur: Strongly recommended to pause ALL campaigns

## Israeli Audience Targeting Tips
- Gush Dan: ~40% of digital ad spend
- Traffic split: 53.62% mobile, 44.91% desktop, 1.47% tablet (StatCounter, July 2026). The commonly repeated "over 70% mobile" figure is NOT supported for Israel; nearly half of Israeli web traffic is desktop.
- Peak hours: 9-10 AM, 12-1 PM, 8-10 PM (Sun-Thu)
- Age demographics shift due to military service (18-21)

## Amendment 13 to the Privacy Protection Law (in force August 14, 2025)
Amendment 13 is a structural overhaul of Israel's privacy framework. It directly affects how ad audiences can be built from personal data.

Consent requirements for ad targeting:
- Consent must be informed, freely given, and in most cases explicit, especially for direct marketing.
- Consent must be granular. Bundled or pre-ticked consent is invalid. Consent to marketing must be separable from consent to the core service.
- Uploading customer phone or email lists for Meta Custom Audiences or Google Customer Match requires documented consent for that specific use. A generic "we may contact you" checkbox does not cover it.
- The same applies to using a customer list as a lookalike or Advantage+ seed, and to pixel / Conversions API (CAPI) tracking that builds remarketing audiences.
- Keep records of when and how each contact consented.

Database obligations:
- Large marketing databases (10,000+ records) and sensitive-data databases still carry registration and notification duties.
- Amendment 13 also introduces mandatory privacy protection officers for some organizations, enhanced transparency obligations, and stricter rules for data brokers.

This is a compliance area. Verify the current Privacy Protection Authority (PPA) guidance and have a privacy lawyer review the consent flow before running list-based or remarketing campaigns.

## Source URLs
- Privacy Protection Authority (Amendment 13 guidance): https://www.gov.il/en/departments/the_privacy_protection_authority/govil-landing-page
- Kol Zchut, cancelling a distance transaction: https://www.kolzchut.org.il/he/ביטול_עסקת_מכר_מרחוק (cancellation windows by transaction type; the four-month right for olim, people with disabilities and over-65s). The gov.il consumer-protection unit page previously cited here now 404s, so this is the working reference. Verify any duty stated as "must" against counsel before relying on it commercially.
- Israel Tax Authority (VAT, currently 18%): https://www.gov.il/he/departments/israel_tax_authority/govil-landing-page
- Google Ads policies: https://support.google.com/google-ads/answer/6008942
- Google Ads, About Smart Bidding: https://support.google.com/google-ads/answer/2459326
- Meta Advertising Standards: https://transparency.meta.com/policies/ad-standards/

## CPC planning defaults by vertical

Illustrative planning defaults, NOT measured Israeli benchmark data. There is no published Israeli CPC benchmark dataset; the vertical ranking derives from US benchmark data adjusted for a smaller, less saturated market. Never quote these to a client as Israeli benchmarks. The sourced path is a Google Keyword Planner forecast with location Israel and language Hebrew, then your own search-terms and auction-insights reports after launch. These same values are encoded in `scripts/cpc_calculator.py`.

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

## Israeli publisher and native networks

Beyond the global platforms, Israel has its own ad inventory worth considering, especially for brand reach and native content:

| Platform | Type | Best For |
|----------|------|----------|
| Taboola (Realize) | Native content recommendation | Native ads on Ynet, Walla, Globes, and other major Israeli news sites. Israeli company. PPC model. Advertisers now buy through Taboola's performance platform "Realize" (ads.realizeperformance.com), which replaced the old Taboola Ads UI. |
| Outbrain Direct Response (by Teads) | Native content recommendation | Native ads on Haaretz, TheMarker, Calcalist, Mako, Times of Israel. Israeli-founded. PPC model. Following the Teads combination the performance product is branded **Outbrain Direct Response (ODR), a Teads subsidiary**, and you still buy it in the Outbrain UI at `my.outbrain.com`, NOT inside a Teads buying platform. |
| Yad2 | Classifieds marketplace | Real estate, automotive, second-hand goods, local services; high-intent local audience. |
| Walla, Ynet, Globes (direct) | Publisher display / sponsored content | Direct media buys and branded content on Israel's largest news properties; strong for brand campaigns and PR-adjacent content. |

Taboola (now sold through its Realize platform at `ads.realizeperformance.com`, which `ads.taboola.com` redirects to) and Outbrain Direct Response (part of Teads, still bought at `my.outbrain.com`) both run a pay-per-click model and cover most of the Israeli premium-publisher landscape between them. They remain two separate competitors, the long-rumored Taboola-Outbrain merger never closed, so do not treat them as one company, just expect the newer brand/platform names. Direct buys with a publisher's ad sales team make sense for larger brand budgets or sponsored-content campaigns. All Israeli-platform campaigns are still subject to the VAT-inclusive pricing and labeling rules in Step 5.

## Category-specific advertising restrictions

| Category | Requirement |
|----------|-------------|
| Financial services | Must include risk disclaimers ("השקעה כרוכה בסיכון") |
| Health/Medical | Cannot promise cures, must include disclaimers |
| Alcohol | No targeting of minors, must include health warnings |
| Gambling/Lottery | Requires license from Israeli authority |
| Food | Nutrition and health claims must be verified |
| Real estate | Must specify if prices exclude VAT for new construction |

### בעברית

| קטגוריה | דרישה |
|----------|-------|
| שירותים פיננסיים | חובה לכלול הגבלות סיכון ("השקעה כרוכה בסיכון") |
| בריאות/רפואה | אי אפשר להבטיח ריפוי, חובה לכלול הגבלות |
| אלכוהול | בלי טרגוט קטינים, חובה לכלול אזהרות בריאות |
| הימורים/הגרלות | דורש רישיון מהרשות הישראלית |
| מזון | טענות תזונתיות ובריאותיות חייבות להיות מאומתות |
| נדל"ן | חובה לציין אם מחירים לא כוללים מע"מ לבנייה חדשה |

### כללי שיווק משפיענים (מלא)

החוק הישראלי דורש ממשפיענים לחשוף בבירור שותפויות בתשלום. תשתמשו ב-#פרסומת או #תוכן_ממומן בפוסטים בעברית. החשיפה חייבת להיות גלויה בלי צורך ללחוץ על "עוד" או לגלול.

## Hebrew keyword morphology

| Pattern | Example Root | Inflections to Target |
|---------|-------------|----------------------|
| Verb conjugations | ל.מ.ד (learn) | לומד, לומדת, לומדים, ללמוד, למד, ילמד |
| Noun forms | ב.ט.ח (insure) | ביטוח, ביטוחים, מבוטח, מבוטחת |
| Construct state (smichut) | | ביטוח רכב, ביטוח בריאות, ביטוח חיים |
| With/without definite article | | ביטוח vs הביטוח |
| Colloquial spelling | | אינטרנט vs אינטרנת |

### Tools


- Google Keyword Planner (set region: Israel)
- Google Trends (compare Hebrew vs English search volume for the same concept)
- Google Search Console (existing site query data)
- Ahrefs/Semrush (limited Hebrew support, but useful for competitor gap analysis)

## Amendment 13 consent for ad targeting (full)

Amendment 13 to the Privacy Protection Law came into force on August 14, 2025. It directly affects how you can build ad audiences from personal data:

- Uploading a customer phone or email list for Meta Custom Audiences (or Google Customer Match) requires explicit, informed, freely given consent from those contacts for that use. A generic "we may contact you" checkbox is not enough.
- Consent must be granular. Bundled or pre-ticked consent is invalid. Marketing consent has to be separable from consent to the core service.
- The same applies to using a customer list as a lookalike or Advantage+ seed, and to pixel / Conversions API (CAPI) tracking that builds remarketing audiences.
- Keep documentation of when and how each contact consented. Large marketing databases (10,000+ records) and sensitive-data databases still carry registration and notification duties.
- Treat the consent and incident-reporting duties as live obligations rather than as guidance. Check the PPA's own publications for current enforcement actions and for its opinion on appointing a privacy protection officer (ממונה הגנת פרטיות), which is the document that decides whether the appointment duty reaches you if you run pixel or CAPI remarketing at scale. We could not reach gov.il to confirm the current status of either at the time of writing, so verify before relying on it.
- This is a compliance area, not advertising advice. Verify the current Privacy Protection Authority (PPA) guidance and have a privacy lawyer review your consent flow. See `references/israeli-ad-regulations.md`.
- **Google Consent Mode v2** (the `ad_user_data` and `ad_personalization` parameters added in the November 2023 consent-mode update, enforced for EEA traffic) is a separate, technical obligation: if you target or measure users in the EEA/UK (common for Israeli companies selling to Europe), you must pass consent signals to Google via Consent Mode or you lose conversion measurement and remarketing for that traffic. It complements Amendment 13, it does not replace the documented consent you need for Israeli contacts.

## Monthly budget minimums

Planning defaults, not platform minimums.

| Platform | Minimum Monthly (NIS) | Recommended Monthly (NIS) |
|----------|----------------------|--------------------------|
| Google Search | 1,500 | 5,000-15,000 |
| Google Display | 1,000 | 3,000-8,000 |
| Meta (Facebook) | 1,000 | 3,000-10,000 |
| LinkedIn | 3,000 | 8,000-20,000 |
| TikTok | 1,500 | 4,000-10,000 |

## Gotchas, long form

- Israeli ad prices must include VAT (18%) by law under Chok Haganat HaTzarchan (Consumer Protection Law). Agents may generate ad copy with pre-VAT prices, which violates Israeli advertising regulations.
- Do NOT inflate ROAS by 18% VAT for a VAT-registered business (osek murshe). The VAT on your ad invoice is reclaimable input VAT, so true ROAS uses ex-VAT spend (5,000 / 1,000 = 5.0x, not 5,000 / 1,180). Only an osek patur, who cannot reclaim it, or a cash-flow model adds the 18%. Agents often wrongly divide ad spend by 1.18.
- The Gush Dan metropolitan area (Tel Aviv area) accounts for approximately 40% of Israeli digital ad spend. Agents may set nationwide targeting when the business only serves a specific region, wasting budget.
- Israeli ad scheduling must avoid Shabbat (Friday afternoon through Saturday evening). Agents may run campaigns 24/7 and burn budget during zero-engagement hours.
- Hebrew ad headlines have a 30-character limit in Google Ads, but Hebrew words are often shorter than English equivalents. Agents may not take advantage of the extra room available in Hebrew headlines.
- Hebrew keyword research must account for morphological variants. A single root can produce dozens of word forms. Agents may target only one inflection and miss significant search volume from other forms.
- Mixed Hebrew/English text in ads can reorder unexpectedly in RTL rendering. Always preview ads in the platform's ad preview tool before publishing.
- Uploading customer phone or email lists for Meta Custom Audiences or Google Customer Match without explicit, granular, documented consent violates Amendment 13 to the Privacy Protection Law (in force since August 2025). Agents may suggest list uploads, lookalike seeds, or pixel/CAPI remarketing with no consent caveat.
- Enhanced CPC (ECPC) is no longer a selectable bidding strategy for Search and Display campaigns. Agents trained on older Google Ads material may still recommend it; use Maximize Conversions or Target CPA instead.
- Agents repeat the widely-blogged claim that Meta is phasing out Lookalike Audiences. Lookalikes remain creatable and we could not find a Meta deprecation notice, so do not tell a client they are being removed unless you can point at one. Test a lookalike against broad Advantage+ rather than assuming either one wins.
- Meta blocks custom audiences that imply a health condition or financial status. Agents building lists for Israeli insurance, finance, legal or health advertisers, the highest-CPC verticals here, will hit this.
- Agents quote the CPC table as if it were measured Israeli benchmark data. It is an illustrative planning default derived from US data; pull a Keyword Planner forecast before quoting a number to a client.

## הסכמה לטרגוט לפי תיקון 13 (עברית, מלא)

**הסכמה לטרגוט פרסומי לפי תיקון 13:**

תיקון 13 לחוק הגנת הפרטיות נכנס לתוקף ב-14 באוגוסט 2025. הוא משפיע ישירות על האופן שבו אפשר לבנות קהלי פרסום ממידע אישי:

- העלאת רשימת טלפונים או מיילים של לקוחות ל-Custom Audiences של מטא (או ל-Customer Match של גוגל) דורשת הסכמה מפורשת, מיודעת וחופשית מאותם אנשים לשימוש הזה. תיבת סימון כללית של "אנחנו עשויים ליצור איתך קשר" לא מספיקה.
- ההסכמה חייבת להיות מפורטת (גרנולרית). הסכמה מאוגדת או מסומנת מראש אינה תקפה. הסכמה לשיווק חייבת להיות נפרדת מהסכמה לשירות עצמו.
- אותו דבר חל על שימוש ברשימת לקוחות כ-seed ל-lookalike או ל-Advantage+, ועל מעקב פיקסל / Conversions API (CAPI) שבונה קהלי רימרקטינג.
- תשמרו תיעוד של מתי וכיצד כל איש קשר נתן הסכמה. מאגרי שיווק גדולים (10,000+ רשומות) ומאגרי מידע רגיש עדיין נושאים חובות רישום והודעה.
- תתייחסו לחובות ההסכמה והדיווח על אירועי אבטחה כחובות חיות ולא כהמלצות. תבדקו בפרסומי הרשות להגנת הפרטיות מהן פעולות האכיפה העדכניות ומה גילוי הדעת שלה בנושא מינוי ממונה הגנת פרטיות, שהוא המסמך שקובע אם חובת המינוי חלה עליכם אם אתם מריצים רימרקטינג פיקסל או CAPI בהיקף. לא הצלחנו להגיע ל-gov.il כדי לאמת את הסטטוס העדכני של שניהם בזמן הכתיבה, אז תאמתו לפני שאתם מסתמכים.
- זהו תחום ציות, לא ייעוץ פרסומי. תאמתו את ההנחיות העדכניות של הרשות להגנת הפרטיות ותעבירו את תהליך ההסכמה לבדיקת עורך דין פרטיות. תסתכלו על `references/israeli-ad-regulations.md`.
- **Google Consent Mode v2** (הפרמטרים `ad_user_data` ו-`ad_personalization` שנוספו בעדכון consent mode של נובמבר 2023, נאכף לתנועת EEA) הוא חובה טכנית נפרדת: אם אתם מטרגטים או מודדים משתמשים ב-EEA/בריטניה (נפוץ לחברות ישראליות שמוכרות לאירופה), אתם חייבים להעביר אותות הסכמה לגוגל דרך Consent Mode אחרת תאבדו מדידת המרות ורימרקטינג לתנועה הזו. זה משלים את תיקון 13, לא מחליף את ההסכמה המתועדת שצריך עבור אנשי קשר ישראלים.

## מינימום תקציב חודשי (עברית)

**מינימום תקציב חודשי (המלצה):**

| פלטפורמה | מינימום חודשי (ש"ח) | מומלץ חודשי (ש"ח) |
|-----------|--------------------|--------------------|
| Google Search | 1,500 | 5,000-15,000 |
| Google Display | 1,000 | 3,000-8,000 |
| Meta (פייסבוק) | 1,000 | 3,000-10,000 |
| לינקדאין | 3,000 | 8,000-20,000 |
| טיקטוק | 1,500 | 4,000-10,000 |

## מורפולוגיה של מילות מפתח בעברית

| תבנית | שורש לדוגמה | צורות נטייה לטרגוט |
|--------|------------|-------------------|
| הטיות פועל | ל.מ.ד | לומד, לומדת, לומדים, ללמוד, למד, ילמד |
| צורות שם עצם | ב.ט.ח | ביטוח, ביטוחים, מבוטח, מבוטחת |
| סמיכות | | ביטוח רכב, ביטוח בריאות, ביטוח חיים |
| עם/בלי ה' הידיעה | | ביטוח לעומת הביטוח |
| כתיב דיבורי | | אינטרנט לעומת אינטרנת |

## מלכודות נפוצות, נוסח מלא

- מחירי פרסום בישראל חייבים לכלול מע"מ (18%) לפי חוק הגנת הצרכן. סוכנים לפעמים מייצרים קופי עם מחירים לפני מע"מ, וזה מפר את הרגולציה.
- אל תנפחו ROAS ב-18% מע"מ לעסק רשום למע"מ (עוסק מורשה). המע"מ בחשבונית הפרסום הוא מס תשומות הניתן לקיזוז, אז ROAS אמיתי משתמש בהוצאה ללא מע"מ (5,000 / 1,000 = 5.0x, לא 5,000 / 1,180). רק עוסק פטור, שלא יכול לקזז, או מודל תזרים מזומנים מוסיף את ה-18%. סוכנים לפעמים מחלקים בטעות את הוצאת הפרסום ב-1.18.
- אזור גוש דן (מטרופולין תל אביב) מהווה כ-40% מהוצאות הפרסום הדיגיטלי בישראל. סוכנים נוטים להגדיר טרגוט ארצי כשהעסק משרת רק אזור ספציפי, וזה שורף תקציב.
- תזמון פרסום ישראלי חייב להימנע משבת (שישי אחר הצהריים עד מוצאי שבת). סוכנים נוטים להריץ קמפיינים 24/7 ולשרוף תקציב בשעות בלי מעורבות.
- כותרות מודעות בעברית מוגבלות ל-30 תווים ב-Google Ads, אבל מילים בעברית לרוב קצרות יותר ממקבילות באנגלית. סוכנים לא תמיד מנצלים את המרחב הנוסף הזמין בכותרות בעברית.
- מחקר מילות מפתח בעברית חייב להביא בחשבון וריאנטים מורפולוגיים. שורש אחד יכול לייצר עשרות צורות מילה. סוכנים לפעמים מטרגטים רק צורה אחת ומפספסים נפח חיפוש משמעותי.
- טקסט מעורב עברית/אנגלית במודעות יכול להסתדר מחדש באופן לא צפוי ברינדור RTL. תמיד תבדקו תצוגה מקדימה בכלי של הפלטפורמה לפני שמפרסמים.
- העלאת רשימות טלפון או מיילים של לקוחות ל-Custom Audiences של מטא או ל-Customer Match של גוגל בלי הסכמה מפורשת, מפורטת ומתועדת מפרה את תיקון 13 לחוק הגנת הפרטיות (בתוקף מאוגוסט 2025). סוכנים נוטים להציע העלאות רשימה, seeds ל-lookalike או רימרקטינג פיקסל/CAPI בלי שום הסתייגות לגבי הסכמה.
- Enhanced CPC (ECPC) כבר לא אסטרטגיית הצעת מחיר שאפשר לבחור לקמפייני חיפוש ותצוגה. סוכנים שאומנו על חומר ישן של Google Ads עדיין ממליצים עליו; תשתמשו ב-Maximize Conversions או ב-Target CPA במקום.
- סוכנים חוזרים על הטענה הנפוצה בבלוגים שמטא מוציאה משימוש קהלי Lookalike. ה-lookalikes עדיין ניתנים ליצירה ולא מצאנו הודעת deprecation של מטא, אז אל תגידו ללקוח שהם מוסרים אלא אם אתם יכולים להצביע על אחת. תבדקו lookalike מול Advantage+ רחב במקום להניח מי מנצח.
- מטא חוסמת קהלים מותאמים שמרמזים על מצב רפואי או מצב פיננסי. סוכנים שבונים רשימות למפרסמים ישראלים בביטוח, פיננסים, משפט או בריאות, הענפים עם ה-CPC הגבוה כאן, ייתקלו בזה.
- סוכנים מצטטים את טבלת ה-CPC כאילו היא נתוני ייחוס ישראליים נמדדים. היא ברירת מחדל אילוסטרטיבית לתכנון שנגזרה מנתונים אמריקאיים; תוציאו תחזית מ-Keyword Planner לפני שאתם מצטטים מספר ללקוח.

## פלטפורמות נייטיב ישראליות (מלא)

**רשתות מפרסמים ונייטיב ישראליות:**

מעבר לפלטפורמות הגלובליות, לישראל יש מלאי פרסום משלה ששווה לשקול, במיוחד לחשיפת ברנד ולתוכן נייטיב:

| פלטפורמה | סוג | הכי מתאים ל |
|-----------|------|-------------|
| טאבולה (Realize) | המלצת תוכן נייטיב | מודעות נייטיב ב-ynet, וואלה, גלובס ואתרי חדשות ישראליים נוספים. חברה ישראלית. מודל PPC. מפרסמים קונים היום דרך פלטפורמת הביצועים של טאבולה בשם "Realize" (ads.realizeperformance.com), שהחליפה את ממשק Taboola Ads הישן. |
| Outbrain Direct Response (של Teads) | המלצת תוכן נייטיב | מודעות נייטיב בהארץ, דה מרקר, כלכליסט, מאקו, טיימס אוף ישראל. חברה ישראלית. מודל PPC. אחרי החיבור ל-Teads מוצר הביצועים ממותג **Outbrain Direct Response (ODR), חברה-בת של Teads**, ועדיין קונים אותו בממשק של אאוטבריין בכתובת `my.outbrain.com`, ולא בתוך פלטפורמת רכישה של Teads. |
| יד2 | זירת מודעות | נדל"ן, רכב, יד שנייה, שירותים מקומיים; קהל מקומי בכוונת רכישה גבוהה. |
| וואלה, ynet, גלובס (ישיר) | תצוגה / תוכן ממומן של המפרסם | רכישת מדיה ישירה ותוכן ממותג בנכסי החדשות הגדולים בישראל; חזק לקמפייני ברנד ולתוכן צמוד-יח"צ. |

טאבולה (כיום דרך פלטפורמת Realize בכתובת `ads.realizeperformance.com`, ש-`ads.taboola.com` מפנה אליה) ו-Outbrain Direct Response (חברה-בת של Teads, עדיין נרכש ב-`my.outbrain.com`) שתיהן רצות על מודל תשלום-לקליק ומכסות ביניהן את רוב נוף המפרסמים הפרמיום בישראל. הן נשארות שתי מתחרות נפרדות, המיזוג השמועתי בין טאבולה לאאוטבריין מעולם לא נסגר, אז אל תתייחסו אליהן כחברה אחת, רק צפו לשמות מותג ופלטפורמה חדשים. רכישה ישירה מול צוות מכירות הפרסום של מפרסם הגיונית לתקציבי ברנד גדולים יותר או לקמפייני תוכן ממומן. כל קמפיין בפלטפורמה ישראלית עדיין כפוף לכללי התמחור כולל מע"מ והסימון בשלב 5.
