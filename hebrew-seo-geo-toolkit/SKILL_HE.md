# ערכת כלים לקידום אתרים ו-GEO בעברית

## הוראות

### שלב 1: ביקורת אתר (SEO + GEO)

הריצו ביקורת מקיפה המכסה הן SEO מסורתי והן מוכנות לחיפוש AI.

**ביקורת SEO מהירה (חינם, ללא API):**
```bash
python3 scripts/seo_audit.py "https://example.co.il"
```

**בדיקות ידניות:**
```bash
# בדיקת מטא תגיות וסימון Schema
curl -sL "https://example.co.il" | grep -E "<title>|<meta name=\"description\"|<meta property=\"og:|application/ld\+json" | head -20

# בדיקת robots.txt (אימות גישת בוטים של AI)
curl -s "https://example.co.il/robots.txt"

# בדיקת מפת אתר
curl -s "https://example.co.il/sitemap.xml" | head -50
```

**אמתו גישת בוטים של AI ב-robots.txt:** Googlebot, Bingbot, PerplexityBot, ChatGPT-User, ClaudeBot, anthropic-ai, GPTBot חייבים כולם להיות מורשים. ראו [references/seo-checklist.md](./references/seo-checklist.md) לרשימת ביקורת מלאה מתועדפת.

### שלב 2: ניתוח מורפולוגיה של מילות מפתח בעברית

עברית היא שפה שורשית שבה תחיליות משנות משמעות:

| תחילית | עברית | משמעות | דוגמה |
|---------|--------|---------|---------|
| ה- | ha- | ה' הידיעה | הבית (the house) |
| ו- | ve- | וו החיבור | והבית (and the house) |
| ב- | be- | ב' השימוש | בבית (in the house) |
| ל- | le- | ל' היעד | לבית (to the house) |
| מ- | me- | מ' המקור | מהבית (from the house) |
| ש- | she- | ש' הזיקה | שבבית (that in the house) |

לכל מילת מפתח מטרה:
1. חלצו את השורש באמצעות ניתוח מורפולוגי
2. צרו את כל צירופי התחיליות שמשתמשים עשויים לחפש
3. כללו צורות סמיכות: "בית קפה" לעומת "הבית של הקפה"
4. התחשבו בצורות זכר/נקבה ויחיד/רבים
5. הריצו `scripts/analyze_keywords.py --keywords "nadlan,dira,bayit"` לניתוח גרסאות מלא

השתמשו ב-**WebSearch** לחקר מילות מפתח:
```
WebSearch: "{keyword} keyword difficulty site:ahrefs.com OR site:semrush.com"
WebSearch: "{keyword} search volume 2026"
```

### שלב 3: הגדרת SEO לדומיין .co.il

| הגדרה | ערך | הערות |
|--------|------|--------|
| עדיפות TLD | co.il. | מועדף לעסקים ישראליים |
| מיקום שרת | ישראל או CDN קרוב | משפר דירוג מקומי |
| Google Search Console | נכס google.co.il | רישום נפרד מ-.com |
| מפת אתר | כלול הערות hreflang | נדרש לאתרים דו-לשוניים |

1. רשמו דומיין .co.il אצל רשם מוסמך של ISOC-IL
2. הגדירו Google Search Console לנכס ה-.co.il
3. הגדירו DNS עם נקודות קצה CDN ישראליות/קרובות (Cloudflare TLV)
4. ודאו שפריסת RTL נטענת כראוי
5. שלחו מפת אתר XML עם הערות hreflang

ראו [references/hebrew-seo.md](./references/hebrew-seo.md) לאסטרטגיית דומיין ומדריכי ציטוטים מקומיים.

### שלב 4: הטמעת תגי hreflang

```html
<link rel="alternate" hreflang="he-IL" href="https://example.co.il/page" />
<link rel="alternate" hreflang="en" href="https://example.co.il/en/page" />
<link rel="alternate" hreflang="x-default" href="https://example.co.il/en/page" />
```

כללים לאתרים ישראליים:
1. השתמשו תמיד ב-`he-IL` (לא רק `he`) לתוכן עברי ישראלי
2. הגדירו `x-default` לגרסה האנגלית למבקרים בינלאומיים
3. כל דף חייב לקשר דו-כיוונית למקבילו בכל השפות
4. השתמשו בכתובות URL מוחלטות ועקביות בכל הצהרות ה-hreflang

### שלב 5: יישום אופטימיזציית GEO (מנועי חיפוש AI)

**GEO = אופטימיזציית מנועים גנרטיביים.** מנועי חיפוש AI לא מדרגים דפים, הם **מצטטים מקורות**. להיות מצוטט זה ה"דירוג מספר 1" החדש.

יישמו את **9 שיטות GEO של פרינסטון** (ראו [references/geo-research.md](./references/geo-research.md)):

| שיטה | שיפור נראות | כיצד ליישם |
|-------|-------------|------------|
| **ציטוט מקורות** | +40% | הוסיפו ציטוטים והפניות סמכותיים |
| **הוספת סטטיסטיקות** | +37% | כללו מספרים ונתונים ספציפיים |
| **הוספת ציטוטים** | +30% | הוסיפו ציטוטי מומחים עם ייחוס |
| **טון סמכותי** | +25% | השתמשו בשפה בטוחה ומומחית |
| **נגיש להבנה** | +20% | פשטו מושגים מורכבים |
| **מונחים מקצועיים** | +18% | כללו טרמינולוגיה תחומית |
| **מילים ייחודיות** | +15% | הגדילו גיוון אוצר מילים |
| **אופטימיזציית שטף** | +15-30% | שפרו קריאות וזרימה |
| ~~דחיסת מילות מפתח~~ | **-10%** | **הימנעו: פוגע בנראות AI** |

**שילוב מיטבי:** שטף + סטטיסטיקות = שיפור מרבי

**מבנה תוכן לחילוץ AI:**
- השתמשו בפורמט "תשובה קודם" (תשובה ישירה בראש כל סעיף)
- היררכיה ברורה של H1 > H2 > H3
- נקודות תבליט, רשימות ממוספרות, טבלאות להשוואה
- פסקאות קצרות (2-3 משפטים מקסימום)
- פורמט שאלות ותשובות לשאלות נפוצות

**FAQPage Schema (+40% נראות AI):**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "מהו [נושא]?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "לפי [מקור], [תשובה עם סטטיסטיקות]."
    }
  }]
}
```

### שלב 6: אופטימיזציה לכל פלטפורמת AI

לכל מנוע חיפוש AI יש גורמי דירוג ייחודיים. הבדלים מרכזיים:

| פלטפורמה | אינדקס ראשי | גורם מפתח | דרישה קריטית |
|----------|-------------|-----------|-------------|
| ChatGPT | אינטרנט (מבוסס Bing) | סמכות דומיין | התאמת תוכן-תשובה, רעננות 30 יום |
| Perplexity | עצמי + Google | רלוונטיות סמנטית | FAQ Schema, מסמכי PDF |
| Google AI Overview | Google | E-E-A-T | Knowledge Graph, נתונים מובנים |
| Copilot | Bing | אינדקס Bing | אקוסיסטם Microsoft (LinkedIn, GitHub) |
| Claude | Brave | צפיפות עובדתית | אינדוקס Brave Search |

**דרישות אוניברסליות:** אפשרו את כל בוטי ה-AI ב-robots.txt, הטמיעו Schema (FAQPage, Article), כללו סטטיסטיקות וציטוטים, עדכנו תוכן תוך 30 יום.

ראו [references/platform-algorithms.md](./references/platform-algorithms.md) לרשימות בדיקה מפורטות לכל פלטפורמה.

### שלב 7: יישום עקרונות EEAT

מסגרת E-E-A-T של Google (ניסיון, מומחיות, סמכותיות, אמינות) משפיעה הן על SEO מסורתי והן על בחירת תשובות AI.

**אותות EEAT ספציפיים לישראל:**
- **ניסיון:** כללו דוגמאות אמיתיות מהשוק הישראלי, מקרי בוחן עם עסקים ישראליים
- **מומחיות:** אישורי מחבר, מומחיות בתחום עברי, הפניות לרגולציה ישראלית
- **סמכותיות:** קישורים נכנסים מדומיינים .co.il, אזכורים בפרסומים ישראליים (גלובס, דה מרקר, כלכליסט)
- **אמינות:** HTTPS, ייחוס ברור בעברית, פרטי קשר עם מספרי 972+, מדיניות פרטיות בעברית

לתוכן YMYL (כסף או חיים) בעברית (רפואי, פיננסי, משפטי), ודאו שהתוכן נבדק על ידי מומחים ישראליים מוסמכים וכולל הצהרות ויתור מתאימות.

ראו [references/eeat-principles.md](./references/eeat-principles.md) לפרטי הטמעה.

### שלב 8: בניית נתונים מובנים של Schema.org בעברית

צרו סימון JSON-LD מותאם לעסקים ישראליים:

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "שם העסק",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "רחוב דוגמה 42",
    "addressLocality": "תל אביב-יפו",
    "addressRegion": "מחוז תל אביב",
    "postalCode": "6100000",
    "addressCountry": "IL"
  },
  "telephone": "+972-3-XXX-XXXX",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Sunday","Monday","Tuesday","Wednesday","Thursday"],
      "opens": "09:00",
      "closes": "18:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Friday",
      "opens": "09:00",
      "closes": "14:00"
    }
  ]
}
```

**שיקולים ספציפיים לישראל:**
1. **שעות שבת:** יום שישי נסגר מוקדם (14:00), שבת סגור
2. **תעודת כשרות:** השתמשו ב-`additionalProperty` עם הגוף המכשיר (רבנות, בד"ץ)
3. **פורמט טלפון:** תמיד קידומת בינלאומית `972+`
4. **מטבע:** הגדירו `priceCurrency` ל-`ILS`

**סכמות משופרות ל-GEO:** הוסיפו `SpeakableSpecification` לחיפוש קולי וחילוץ AI:
```json
{
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": ["h1", ".summary", ".faq-answer"]
  }
}
```

ראו [references/schema-templates.md](./references/schema-templates.md) לתבניות JSON-LD מלאות (FAQ, Article, Product, HowTo, Organization, דפוסי @graph משולבים).

### שלב 9: הגדרת גישת בוטים של AI

הגדירו `robots.txt` לאפשר את כל בוטי החיפוש וה-AI העיקריים:

```
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

Sitemap: https://example.co.il/sitemap.xml
```

**החלטות שצריך לקבל:**
- אפשור סורקי AI מגדיל סיכויים לציטוט בתגובות AI
- חסימת `Google-Extended` מונעת שימוש לאימון AI תוך שמירה על אינדוקס Google Search
- בדקו את המדיניות שלכם באופן קבוע כי תחום זה מתפתח במהירות

### שלב 10: אימות וניטור

**אימות SEO:**
```bash
# אימות Schema
open "https://search.google.com/test/rich-results?url={encoded_url}"

# בדיקת אינדוקס Google
open "https://www.google.com/search?q=site:{domain}"

# בדיקת אינדוקס Bing (נדרש ל-Copilot)
open "https://www.bing.com/search?q=site:{domain}"
```

**ניטור GEO:**
- עקבו אחר ציטוטי AI באמצעות כלים כמו Otterly.ai, Profound, או SE Ranking AI Toolkit
- נטרו תעבורת הפניות מפלטפורמות AI (Perplexity, ChatGPT)
- חפשו את המותג שלכם בעוזרי AI לבדיקת דיוק ציטוטים
- עקבו אחר נתוני AI Overview ב-Google Search Console

**בדיקות ספציפיות לעברית:**
1. ודאו תצוגת RTL תקינה בכל הדפדפנים
2. בדקו קישור hreflang דו-כיווני
3. אשרו שרישומי ספריות מקומיות עקביים (NAP: שם, כתובת, טלפון)
4. הריצו `scripts/analyze_keywords.py --audit` לבדיקת כיסוי מילות מפתח

ראו [references/tools-and-apis.md](./references/tools-and-apis.md) לרשימה מלאה של כלי SEO/GEO חינמיים ובתשלום.

## דוגמאות

### דוגמה 1: מחקר מילות מפתח בעברית
המשתמש אומר: "אני צריך מילות מפתח לאתר נדל"ן ישראלי"
פעולות:
1. זיהוי מילות מפתח שורשיות: נדל"ן, דירה, בית
2. יצירת גרסאות מורפולוגיות: הנדל"ן, בנדל"ן, דירות (רבים), בתים (רבים)
3. הכללת צורות סמיכות: סוכן נדל"ן, מחירי דירות
4. הרצת `scripts/analyze_keywords.py --keywords "נדלן,דירה,בית"` לניתוח גרסאות מלא
5. מיפוי גרסאות לדפים לפי עדיפות נפח חיפוש
תוצאה: מפת מילות מפתח מלאה בעברית עם גרסאות מורפולוגיות וצירופי תחיליות

### דוגמה 2: הגדרת hreflang לאתר דו-לשוני
המשתמש אומר: "הגדר hreflang לאתר ה-.co.il שלי בעברית ואנגלית"
פעולות:
1. ביקורת דפים קיימים לזוגות שפה
2. יצירת תגי hreflang link עבור ה-head של HTML בכל דף
3. יצירת מפת אתר XML עם הערות hreflang
4. אימות קישור דו-כיווני בין גרסאות שפה
תוצאה: הטמעת hreflang מלאה עם טירגוט he-IL ו-en

### דוגמה 3: אופטימיזציית GEO ל-SaaS ישראלי
המשתמש אומר: "מטב את דף הנחיתה של ה-SaaS הישראלי שלי למנועי חיפוש AI"
פעולות:
1. ביקורת נראות AI נוכחית (חפשו את שם המותג ב-ChatGPT, Perplexity, Claude)
2. יישום שיטות GEO של פרינסטון: הוספת סטטיסטיקות עם מקורות, ציטוטי מומחים, הפניות סמכותיות
3. הטמעת FAQPage schema עם זוגות שאלות-תשובות דו-לשוניים
4. הוספת SpeakableSpecification לסעיפי תוכן מרכזיים
5. אימות שכל בוטי ה-AI מורשים ב-robots.txt
6. מבנה תוכן בפורמט תשובה-קודם עם היררכיית H2/H3 ברורה
תוצאה: דף נחיתה ממוטב הן ל-Google.co.il והן לציטוטים במנועי חיפוש AI

### דוגמה 4: Schema למסעדה ישראלית עם GEO
המשתמש אומר: "צור נתונים מובנים למסעדה הכשרה שלי בירושלים"
פעולות:
1. בניית JSON-LD של LocalBusiness/Restaurant עם פורמט כתובת ישראלי
2. הוספת שעות פתיחה מותאמות שבת (סגירה מוקדמת ביום שישי, שבת סגור)
3. הכללת תעודת כשרות עם פרטי רבנות
4. הוספת FAQPage schema לשאלות נפוצות (תפריט, הזמנות, רמת כשרות)
5. הוספת SpeakableSpecification לשאילתות עוזרים קוליים
6. הכללת Schema תפריט בעברית עם תמחור בש"ח
תוצאה: סימון JSON-LD מלא ממוטב ל-Google Rich Results ולציטוטי AI

### דוגמה 5: ביקורת SEO + GEO מלאה
המשתמש אומר: "בצע ביקורת לאתר המסחר האלקטרוני הישראלי שלי ל-SEO ונראות AI"
פעולות:
1. הרצת `python3 scripts/seo_audit.py "https://example.co.il"` לביקורת טכנית
2. בדיקת גישת בוטי AI ב-robots.txt
3. אימות hreflang ואיכות תוכן עברי
4. ביקורת נתונים מובנים (FAQPage, Product, BreadcrumbList schemas)
5. הערכת אותות EEAT (אישורי מחבר, ציטוטים, מומחיות עברית)
6. בדיקת נראות AI על ידי חיפוש שם מותג ומוצרים ב-ChatGPT, Perplexity, Claude
7. סקירת נתוני AI Overview ב-Google Search Console
תוצאה: תוכנית שיפור SEO + GEO מתועדפת לשוק הישראלי

## משאבים מצורפים

### סקריפטים
- `scripts/seo_audit.py` -- ביקורת SEO מלאה לאתר: מטא תגיות, robots.txt, מפת אתר, זמן טעינה, סימון Schema, גישת בוטי AI. ללא צורך ב-API. הרצה: `python3 scripts/seo_audit.py "https://example.co.il"`
- `scripts/analyze_keywords.py` -- ניתוח מורפולוגי של מילות מפתח בעברית: מייצר גרסאות תחיליות (ה-, ו-, ב-, ל-, מ-, ש-), צורות רבים, וצירופי סמיכות. הרצה: `python scripts/analyze_keywords.py --help`
- `scripts/keyword_research.py` -- מחקר מילות מפתח עם נתוני נפח חיפוש וקושי. דורש DataForSEO API. הרצה: `python3 scripts/keyword_research.py "seo tools" --limit 20`
- `scripts/serp_analysis.py` -- ניתוח תוצאות Google מובילות למילת מפתח. דורש DataForSEO API. הרצה: `python3 scripts/serp_analysis.py "best seo tools"`
- `scripts/backlinks.py` -- ניתוח פרופיל קישורים נכנסים. דורש DataForSEO API. הרצה: `python3 scripts/backlinks.py "example.com"`
- `scripts/domain_overview.py` -- מדדי דומיין: תעבורה, מילות מפתח, דירוגים. דורש DataForSEO API. הרצה: `python3 scripts/domain_overview.py "example.com"`
- `scripts/autocomplete_ideas.py` -- הצעות השלמה אוטומטית של Google. דורש DataForSEO API.
- `scripts/related_keywords.py` -- גילוי מילות מפתח קשורות. דורש DataForSEO API.
- `scripts/competitor_gap.py` -- ניתוח פערי מילות מפתח מול מתחרים. דורש DataForSEO API.

### חומרי עזר
- `references/hebrew-seo.md` -- שיטות עבודה מומלצות ל-SEO בעברית: אסטרטגיית דומיין .co.il, אופטימיזציית RTL, ספריות עסקיות ישראליות, גורמי דירוג Google.co.il. היעזרו בעת הטמעה או ביקורת של SEO בעברית.
- `references/geo-research.md` -- מחקר GEO של פרינסטון (9 שיטות אופטימיזציה עם דוגמאות, שילובים מיטביים, המלצות לפי תחום). היעזרו בעת אופטימיזציה לציטוטים במנועי חיפוש AI.
- `references/platform-algorithms.md` -- גורמי דירוג מפורטים לכל פלטפורמת AI (ChatGPT, Perplexity, Google AI Overview, Copilot, Claude) ו-SEO מסורתי של Google. היעזרו בעת אופטימיזציה לפלטפורמת חיפוש ספציפית.
- `references/schema-templates.md` -- תבניות JSON-LD מוכנות לשימוש: FAQPage, WebPage, Article, SoftwareApplication, Organization, Product, HowTo, BreadcrumbList, LocalBusiness, SpeakableSpecification, דפוסי @graph משולבים. היעזרו בעת הטמעת נתונים מובנים.
- `references/seo-checklist.md` -- רשימת ביקורת SEO/GEO מלאה מתועדפת (P0/P1/P2) המכסה SEO טכני, SEO on-page, סימון Schema, אופטימיזציית GEO, SEO off-page, וניטור. היעזרו בעת הרצת ביקורת אתר מלאה.
- `references/tools-and-apis.md` -- רשימה אצורה של כלי SEO/GEO חינמיים ובתשלום, APIs, הרחבות דפדפן, וכלי שורת פקודה. היעזרו בעת המלצה על כלים או הגדרת אוטומציה.
- `references/eeat-principles.md` -- מסגרת EEAT של Google (ניסיון, מומחיות, סמכותיות, אמינות) עם דפוסי הטמעה ושיקולי YMYL. היעזרו בעת הערכה או שיפור איכות תוכן.
- `references/aeo-considerations.md` -- מדריך אופטימיזציית מנועי תשובות (AEO): כיצד AI בוחר תשובות, מבנה תוכן ל-AI, Google AI Overviews, ניהול סורקי AI, מדידת הצלחת AEO. היעזרו בעת אופטימיזציה של תוכן לבחירת תשובות AI.

## מלכודות נפוצות

- המורפולוגיה העברית יוצרת וריאנטים של מילות מפתח שסוכנים מפספסים. למילה "נדל"ן" יש תחיליות כמו "הנדל"ן", "בנדל"ן", "לנדל"ן" שהן שאילתות חיפוש נפרדות. סוכנים עלולים לייעל לצורה אחת ולפספס את רוב תנועת החיפוש.
- שעות הפעילות העסקיות ב-schema.org חייבות לשקף שבוע עבודה ראשון-חמישי עם סגירה מוקדמת ביום שישי. סוכנים מגדירים כברירת מחדל לוח זמנים של שני-שישי.
- תג hreflang לעברית ישראלית חייב להיות `he-IL`, לא רק `he`. סוכנים לעתים קרובות משמיטים את קוד המדינה, מה שפוגע בטירגוט הגיאוגרפי של Google ל-google.co.il.
- מספרי טלפון ישראליים ב-structured data חייבים להשתמש בקידומת `972+`. סוכנים עלולים לעצב מספרים בפורמט מקומי 0X-XXX-XXXX, שנכשל באימות Schema.
- GEO (אופטימיזציה למנועים גנרטיביים) הוא תחום שמתפתח במהירות. גורמי הדירוג של פלטפורמות AI משתנים תדיר. סוכנים עלולים להמליץ על אסטרטגיות GEO מיושנות אפילו מלפני חצי שנה.

## פתרון בעיות

### שגיאה: "hreflang mismatch detected"
סיבה: תגי hreflang אינם דו-כיווניים (דף A מקשר ל-B אבל B לא מקשר חזרה ל-A)
פתרון: ודאו שכל הצהרת hreflang היא הדדית. גם הגרסה העברית וגם האנגלית חייבות להפנות אחת לשנייה.

### שגיאה: "RTL rendering issues"
סיבה: חסר מאפיין dir="rtl" או קונפליקטים ב-CSS עם ברירות מחדל של LTR
פתרון: הגדירו dir="rtl" על אלמנט ה-html בדפים עבריים. השתמשו ב-CSS logical properties (margin-inline-start במקום margin-left).

### שגיאה: "Schema validation failed"
סיבה: סימון JSON-LD מכיל שגיאות או חסרים מאפיינים נדרשים
פתרון: בדקו עם Google Rich Results Test. בעיות ישראליות נפוצות: פורמט טלפון שגוי (חובה להשתמש ב-972+), חסר addressCountry: IL, או קוד מטבע ILS.

### שגיאה: "Keywords not ranking on google.co.il"
סיבה: תוכן עשוי להיות מתורגם מכונה או חסרות גרסאות מורפולוגיות של מילות מפתח
פתרון: ודאו שתוכן עברי כולל צירופי תחיליות טבעיים. השתמשו ב-`scripts/analyze_keywords.py` לזיהוי גרסאות חסרות.

### שגיאה: "לא מופיע בתוצאות חיפוש AI"
סיבה: בוטי AI עשויים להיות חסומים, לתוכן חסרים אותות ראויים לציטוט, או שהאתר לא מאונדקס בפלטפורמות הנדרשות
פתרון: בדקו ש-robots.txt מאפשר GPTBot, PerplexityBot, ClaudeBot. יישמו שיטות GEO (ציטוטים, סטטיסטיקות, טון סמכותי). אמתו אינדוקס Bing (ל-Copilot) ואינדוקס Brave (ל-Claude). ודאו שהתוכן עודכן תוך 30 יום.

### שגיאה: "AI מצטט מתחרים במקום את האתר שלי"
סיבה: לתוכן המתחרה צפיפות עובדתית גבוהה יותר, מבנה טוב יותר, או ציטוטים סמכותיים יותר
פתרון: יישמו שיטות GEO של פרינסטון: הוסיפו סטטיסטיקות ספציפיות עם מקורות (+37%), ציטוטים סמכותיים (+40%), ציטוטי מומחים (+30%). השתמשו בפורמט תשובה-קודם ו-FAQPage schema. בנו סמכות נושאית דרך אשכולות תוכן.
