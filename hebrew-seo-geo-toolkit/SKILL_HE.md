# ערכת כלים לקידום אתרים ו-GEO בעברית

## הוראות

### שלב 1: ביקורת אתר (SEO + GEO)

תריצו ביקורת מקיפה שמכסה גם SEO מסורתי וגם מוכנות לחיפוש AI.

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

**תאמתו גישת בוטי AI ב-robots.txt:** חייבים להיות מורשים Googlebot, Bingbot, GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User, ClaudeBot, Claude-SearchBot ו-Claude-User. תסתכלו על [references/seo-checklist.md](./references/seo-checklist.md) לרשימת ביקורת מלאה מתועדפת.

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
1. תחלצו את השורש בעזרת ניתוח מורפולוגי
2. תייצרו את כל צירופי התחיליות שמשתמשים יכולים לחפש
3. תכניסו צורות סמיכות: "בית קפה" לעומת "הבית של הקפה"
4. תשימו לב לצורות זכר/נקבה ויחיד/רבים
5. תריצו `scripts/analyze_keywords.py --keywords "nadlan,dira,bayit"` לניתוח גרסאות מלא

תשתמשו ב-**WebSearch** למחקר מילות מפתח:
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

1. תרשמו דומיין .co.il אצל רשם מוסמך של ISOC-IL
2. תגדירו Google Search Console לנכס ה-.co.il
3. תגדירו DNS עם נקודות קצה CDN ישראליות/קרובות (Cloudflare TLV)
4. תוודאו שפריסת RTL נטענת כמו שצריך
5. תשלחו מפת אתר XML עם הערות hreflang

תסתכלו על [references/hebrew-seo.md](./references/hebrew-seo.md) לאסטרטגיית דומיין ומדריכי ציטוטים מקומיים.

### שלב 4: הטמעת תגי hreflang

```html
<link rel="alternate" hreflang="he-IL" href="https://example.co.il/page" />
<link rel="alternate" hreflang="en" href="https://example.co.il/en/page" />
<link rel="alternate" hreflang="x-default" href="https://example.co.il/en/page" />
```

כללים לאתרים ישראליים:
1. תשתמשו תמיד ב-`he-IL` (לא רק `he`) לתוכן עברי ישראלי
2. תגדירו `x-default` לגרסה האנגלית למבקרים בינלאומיים
3. כל דף חייב לקשר דו-כיוונית למקבילו בכל השפות
4. תשתמשו בכתובות URL מוחלטות ועקביות בכל הצהרות ה-hreflang

### שלב 5: יישום אופטימיזציית GEO (מנועי חיפוש AI)

**GEO = אופטימיזציית מנועים גנרטיביים.** מנועי חיפוש AI לא מדרגים דפים, הם **מצטטים מקורות**. להיות מצוטט זה ה"דירוג מספר 1" החדש.

תיישמו את **9 שיטות GEO של פרינסטון** (תסתכלו על [references/geo-research.md](./references/geo-research.md)):

מסודר לפי טבלה 1 במאמר עצמו, מהחזק לחלש. באינטרנט מסתובבת טבלת אחוזים לכל שיטה (בדרך כלל "ציטוט מקורות 40%+"), אבל היא לא תואמת את המאמר: המאמר מדווח שהוספת ציטוטים היא השיטה החזקה ביותר, ו-40% הוא תקרה כללית ל-GEO ולא נתון של שיטה בודדת.

| שיטה | עוצמת ההשפעה | כיצד ליישם |
|-------|---------------|------------|
| **הוספת ציטוטים** | החזקה ביותר | הוסיפו ציטוטי מומחים עם ייחוס |
| **הוספת סטטיסטיקות** | חזקה מאוד | כללו מספרים ונתונים ספציפיים |
| **אופטימיזציית שטף** | חזקה | שפרו קריאות וזרימה |
| **ציטוט מקורות** | חזקה | הוסיפו ציטוטים והפניות סמכותיים |
| **מונחים מקצועיים** | בינונית | כללו טרמינולוגיה תחומית |
| **נגיש להבנה** | בינונית | פשטו מושגים מורכבים |
| **טון סמכותי** | מתונה | השתמשו בשפה בטוחה ומומחית |
| **מילים ייחודיות** | זניחה | המאמר משייך אותה לשיטות שלא עובדות |
| ~~דחיסת מילות מפתח~~ | **מתחת לבסיס** | **הימנעו: התוצאה גרועה מלא לעשות כלום** |

הנתון המרכזי במאמר: השיטות הטובות ביותר משפרות על הבסיס ב-41% במדד Position-Adjusted Word Count וב-28% במדד Subjective Impression.

**שילוב מיטבי:** אופטימיזציית שטף יחד עם הוספת סטטיסטיקות, שהמאמר מדווח עליו כצמד החזק ביותר.

**מבנה תוכן לחילוץ AI:**
- תשתמשו בפורמט "תשובה קודם" (תשובה ישירה בראש כל סעיף)
- היררכיה ברורה של H1 > H2 > H3
- נקודות תבליט, רשימות ממוספרות, טבלאות להשוואה
- פסקאות קצרות (2-3 משפטים מקסימום)
- פורמט שאלות ותשובות לשאלות נפוצות

**FAQPage Schema:**
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

לכל מנוע חיפוש AI יש גורמי דירוג ייחודיים. תמונת מצב 2026:

| פלטפורמה | אינדקס ראשי | גורם מפתח | דרישה קריטית |
|----------|-------------|-----------|-------------|
| ChatGPT (חיפוש) | סורק עצמי (`OAI-SearchBot`) + Bing כגיבוי | סמכות דומיין + התאמת תוכן-תשובה | חייבים לאשר את `OAI-SearchBot` בנפרד מ-`GPTBot` (אימון); לשמור על תוכן עדכני באמת |
| Perplexity | סורק עצמי (`PerplexityBot`) + Google כגיבוי | רלוונטיות סמנטית | FAQ Schema, נתונים מובנים, מקורות PDF/markdown |
| Google AI Overview | אינדקס Google | E-E-A-T + Knowledge Graph | זמין לכל המשתמשים בישראל ובעברית; נתונים מובנים ופסקאות תשובה ברורות עוזרים |
| Google AI Mode | אינדקס Google | E-E-A-T + כיסוי תת-שאלות | משטח נפרד מ-AI Overviews. גם עברית וגם ישראל מופיעות ברשימת הזמינות הרשמית של AI Mode. משתמש ב-query fan-out, אז כסו בדף גם את תת-השאלות הנלוות |
| Gemini (Google) | אינדקס Google + ווב בזמן אמת | E-E-A-T + רעננות | זהה ל-Google Search |
| Copilot (Microsoft) | אינדקס Bing | דירוג Bing + אותות אקוסיסטם MS | Bing Webmaster Tools מאומת, נוכחות ב-LinkedIn/GitHub |
| Claude (עם web search) | אינדקס עצמי של Anthropic דרך `Claude-SearchBot`, בשילוב מנוע חיפוש חיצוני | צפיפות עובדתית + ציטוטים | אישור `Claude-SearchBot` + URL מקור נקי |

**לגבי מנוע החיפוש שמאחורי Claude:** מקובל לייחס את החיפוש של Claude ל-Brave, על בסיס הופעת Brave ברשימת קבלני המשנה המפורסמת של Anthropic ופרמטר בשם `BraveSearchParams` בהגדרת כלי החיפוש. Anthropic מעולם לא נקבה רשמית בשם ספק, אז אל תציגו את זה כעובדה מול לקוח. מה שכן מתועד רשמית זה `Claude-SearchBot`, אז תבצעו אופטימיזציה מולו ולא מול אינדקס חיצוני ספציפי.

**לגבי ההבדל בין AI Overviews ל-AI Mode:** מדובר בשני משטחים שונים. ההנחיה של Google עצמה אומרת שאין דרישות נוספות או אופטימיזציות מיוחדות כדי להופיע באף אחד מהם, כלומר כרטיס הכניסה הוא תוכן רגיל, מועיל ובר-אינדוקס. שניהם עשויים להשתמש בטכניקת query fan-out, כלומר שליחת כמה חיפושים נלווים מאחורי שאילתה אחת, וזאת בדיוק הסיבה הקונקרטית לענות בדף גם על השאלות הסמוכות ולא רק על הכותרת.

**טבלת בוטים (2026):**
- `GPTBot`, סורק האימון של OpenAI. תחסמו אם לא רוצים אימון; תאשרו אם רוצים נוכחות רחבה ב-OpenAI.
- `OAI-SearchBot`, סורק נפרד של OpenAI לתוצאות חיפוש ChatGPT. תאשרו אותו גם אם חוסמים את `GPTBot`, אחרת חיפוש ChatGPT לא יצטט אתכם.
- `ChatGPT-User`, נורה כשמשתמש מפעיל גלישה בצ'אט. תאשרו.
- `PerplexityBot`, סורק האינדקס. תאשרו. הוא מכבד robots.txt.
- `Perplexity-User`, שליפה לפי דרישה כשמשתמש שואל שאלה. תאשרו. שימו לב ש-Perplexity מתעדת שהשליפה הזאת בדרך כלל מתעלמת מכללי robots.txt, כי משתמש אנושי ביקש אותה, אז חסימה פוגעת באינדוקס ולא מונעת שליפה.
- `ClaudeBot`, סורק האימון של Anthropic. תאשרו אם אתם רוצים שהתוכן ישמש לאימון.
- `Claude-SearchBot`, סורק האינדקס לחיפוש של Anthropic. **תאשרו אותו גם אם חסמתם את `ClaudeBot`**, כי הוא זה שהופך אתכם לזכאים לציטוט בתוצאות החיפוש של Claude. אותה הפרדה בדיוק כמו `GPTBot` מול `OAI-SearchBot` אצל OpenAI.
- `Claude-User`, נורה כשמשתמש Claude שואל שאלה שדורשת דף. תאשרו.
- `anthropic-ai` ו-`Claude-Web` הם שמות ישנים שעדיין מסתובבים בדוגמאות robots.txt אבל לא מופיעים בתיעוד הנוכחי של Anthropic. לא מזיק להשאיר, לא שווה להוסיף.
- `Google-Extended`, opt-out לאימון Gemini/Bard (לא משפיע על דירוג Google Search או על ציטוטים ב-AI Overview).
- `CCBot`, Common Crawl, משמש מאמני מודלים רבים.
- `Applebot-Extended`, opt-out לאימון Apple Intelligence.
- `MistralAI-User`, שם שמסתובב כ-fetcher לפי דרישה של Le Chat. לא מצאנו אותו בתיעוד הפומבי של Mistral, אז אמתו לפני שאתם מסתמכים עליו. אין נזק להשאיר אותו מאושר ב-robots.txt.
- `Meta-ExternalAgent`, crawler של מטא למוצרי Meta AI. ניתן לחסום ב-robots.txt כדי לעשות opt-out.

**מעמד llms.txt נכון ל-2026: אופציונלי, ולא סיגנל דירוג או ציטוט.** אל תמכרו את זה ללקוח ככזה. צוות Search Relations של Google אמר שהחיפוש לא משתמש ב-llms.txt ואין כוונה לעשות זאת, והתיעוד של Google לתכונות AI בכלל לא מזכיר אותו, ובמקביל קובע שלא נדרשים קבצים או תגיות נוספים ל-AI Overviews או ל-AI Mode. אף מנוע AI לא הכריז שהוא קורא אותו כקלט לדירוג. תעלו אותו אם בא לכם רישום זול בשכבת הפרוטוקול, על הסיכוי שהקונבנציה תנצח בהמשך, בערך אותו סוג הימור ש-Schema.org היה לפני עשור, אבל רק אחרי היסודות ולעולם לא במקומם. תניחו אינדקס קצר ב-`/llms.txt` לפי המפרט של llmstxt.org. קובץ נלווה ארוך יותר, שנהוג לקרוא לו llms-full.txt, הוא מוסכמה של כלים ולא חלק מהמפרט. גם ל-Open Knowledge Format של Google Cloud (בקיצור OKF, כרגע גרסה 0.2, ספריית קבצי Markdown עם YAML frontmatter) יש בדיוק אותה הסתייגות: שום דבר עדיין לא סורק את הרשת הפתוחה כדי למצוא אותו.

**דרישות אוניברסליות:** תאשרו את בוטי זמן-החיפוש (`OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `Claude-SearchBot`, `Claude-User`) ב-robots.txt, תשמרו על תוכן מרונדר בצד השרת וניתן לאינדוקס, תטמיעו Schema (Article, Organization עם sameAs, FAQPage), תכניסו סטטיסטיקות וציטוטים, ותשמרו על תוכן עדכני באמת. שימו לב ש-llms.txt איננו ברשימה הזאת.

תסתכלו על [references/platform-algorithms.md](./references/platform-algorithms.md) לרשימות בדיקה מפורטות לכל פלטפורמה.

### שלב 7: יישום עקרונות EEAT

מסגרת E-E-A-T של Google (ניסיון, מומחיות, סמכותיות, אמינות) משפיעה הן על SEO מסורתי והן על בחירת תשובות AI.

**אותות EEAT ספציפיים לישראל:**
- **ניסיון:** תכניסו דוגמאות אמיתיות מהשוק הישראלי, מקרי בוחן עם עסקים ישראליים
- **מומחיות:** אישורי מחבר, מומחיות בתחום עברי, הפניות לרגולציה ישראלית
- **סמכותיות:** קישורים נכנסים מדומיינים .co.il, אזכורים בפרסומים ישראליים (גלובס, דה מרקר, כלכליסט)
- **אמינות:** HTTPS, ייחוס ברור בעברית, פרטי קשר עם קידומת 972+, מדיניות פרטיות בעברית

לתוכן YMYL (כסף או חיים) בעברית (רפואי, פיננסי, משפטי), תוודאו שהתוכן נבדק על ידי מומחים ישראליים מוסמכים וכולל הצהרות ויתור מתאימות.

תסתכלו על [references/eeat-principles.md](./references/eeat-principles.md) לפרטי הטמעה.

### שלב 8: בניית נתונים מובנים של Schema.org בעברית

תייצרו סימון JSON-LD מותאם לעסקים ישראליים:

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

**מה חשוב לדעת בישראל:**
1. **שעות שבת:** יום שישי נסגר מוקדם (14:00), שבת סגור
2. **תעודת כשרות:** תשתמשו ב-`additionalProperty` עם הגוף המכשיר (רבנות, בד"ץ)
3. **פורמט טלפון:** תמיד קידומת בינלאומית `972+`
4. **מטבע:** תגדירו `priceCurrency` ל-`ILS`

**סכמות משופרות ל-GEO:** תוסיפו `SpeakableSpecification` לחיפוש קולי וחילוץ AI:
```json
{
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": ["h1", ".summary", ".faq-answer"]
  }
}
```

תסתכלו על [references/schema-templates.md](./references/schema-templates.md) לתבניות JSON-LD מלאות (FAQ, Article, Product, HowTo, Organization, דפוסי @graph משולבים).

### שלב 9: הגדרת גישת בוטי AI ו-llms.txt

תגדירו את `robots.txt` לאפשר את כל בוטי החיפוש המסורתיים וה-AI העיקריים:

```
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# OpenAI: בוטים נפרדים לאימון ולחיפוש
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

# Perplexity
User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

# Anthropic
User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

# Common Crawl (משמש מאמני מודלים רבים)
User-agent: CCBot
Allow: /

# Mistral (Le Chat web search)
User-agent: MistralAI-User
Allow: /

# Meta AI external agent (תשנו ל-Disallow כדי לעשות opt-out)
User-agent: Meta-ExternalAgent
Allow: /

Sitemap: https://example.co.il/sitemap.xml
```

**החלטות שצריך לקבל:**
- אפשור סורקי זמן-חיפוש (`OAI-SearchBot`, `Perplexity-User`, `ChatGPT-User`) מגדיל סיכויים להיות מצוטטים בתגובות AI.
- חסימת `Google-Extended` היא opt-out לאימון Gemini בלי לפגוע בדירוג Google Search או בציטוטים ב-AI Overview.
- חסימת `GPTBot` היא opt-out לאימון מודלים של OpenAI אבל שומרת אתכם זכאים לחיפוש ChatGPT, בתנאי ש-`OAI-SearchBot` ו-`ChatGPT-User` נשארים מאושרים.
- אותה הפרדה קיימת ב-Anthropic: חסימת `ClaudeBot` היא opt-out מאימון, בזמן ש-`Claude-SearchBot` שומר על הזכאות לציטוט בחיפוש של Claude. חסימה של `ClaudeBot` לבדו איננה יציאה מ-Claude, ורק חסימת שלושתם היא.
- תבדקו את המדיניות שלכם באופן קבוע. התחום מתפתח מהר.

**אפשר להוסיף `/llms.txt`, אבל זה אופציונלי:** llms.txt (הוצע על ידי Jeremy Howard, 2024) הוא קונבנציה ולא תקן, ואין לו אפקט מוכח על דירוג או ציטוט. תניחו קובץ markdown קצר ב-`https://example.co.il/llms.txt` שמסכם את מטרת האתר ואת ה-URLים המרכזיים, אם אתם רוצים להירשם מוקדם. אל תיתנו לו לדחוק HTML מרונדר בצד השרת, Schema.org או robots.txt תקין, ואל תדווחו עליו ללקוח כהישג בנראות AI.

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

**ניטור GEO: תמדדו בארבע שכבות, לפי הסדר.** תוצאות GEO מתעכבות (המנוע צריך לסרוק מחדש לפני שהעריכה שלכם יכולה לצוף) ומוסוות על ידי גורמים אחרים (המספר שלכם זז גם כשהמנוע או מתחרה משתנים). לכן תפרידו בין מדד מקורב ומהיר לבין תוצאה אמיתית ואיטית, במקום לקרוא השוואת לפני-ואחרי גולמית.

| שכבה | השאלה | זמן תגובה | מקורב או תוצאה |
|------|-------|-----------|----------------|
| גישת סורקים | האם הבוטים בכלל מצליחים לשלוף ולפענח את הדף? | מיידי | תנאי מקדים |
| יכולת ציטוט | בהינתן הדף, האם הוא נתיק וממוקד תשובה? | דקות | מקורב |
| הופעה בפועל | האם מנוע מצטט אתכם על שאילתה נקייה, בלי שביקשתם? | ימים עד שבועות | תוצאה (GEO) |
| דירוגים והקלקות | מיקום, חשיפות, שיעור הקלקה | שבועות עד חודשים | תוצאה (SEO) |

**תמיד תבדקו את שכבת הגישה לפני שאתם מסיקים משהו על איכות התוכן.** מצב של "עדיין לא נסרק" ומצב של "נסרק אבל לא נבחר" נראים זהים לחלוטין בתיבת התשובה, והתיקון שלהם הפוך. אבחון של בעיית תוכן כשהסיבה האמיתית היא `Claude-SearchBot` חסום מבזבז שבועות.

1. **שכבת הגישה:** תבקשו את הדף בתור כל user agent של בוט, תוודאו החזר 200 וגם שהתוכן נמצא ב-HTML הגולמי ולא מוזרק ב-JavaScript. תעריכו את robots.txt לכל user agent בנפרד ולא במצטבר. תבדקו בלוגים שלכם פניות אמיתיות של בוטים לכל כתובת.
2. **שכבת יכולת הציטוט:** תמסרו כתובת ספציפית למנוע ותשאלו את שאלת היעד. זה עוקף את השהיית הסריקה בנתיבי שליפה חיה, אז אפשר לחזור על זה תוך דקות, אבל זה מוכיח רק יכולת חילוץ ולא שתיבחרו.
3. **שכבת ההופעה בפועל:** תשאלו מערך קבוע של שאילתות בלי למסור את הכתובת, ותתעדו ציטוטים לאורך זמן מול דף ביקורת שלא ערכתם. זאת תוצאת ה-GEO האמיתית.
4. **שכבת הדירוגים:** נתוני Search Console ודירוגים, בצילומי מצב לאורך זמן מול אותו דף ביקורת.

**דוחות ה-AI הגנרטיבי ב-Google Search Console:** גוגל השיקה ב-3 ביוני 2026 דוחות ייעודיים לביצועי AI גנרטיבי, שמכסים AI Overviews, AI Mode ותכונות AI גנרטיבי ב-Discover. הם מדווחים **חשיפות, דפים, מדינות, מכשירים ותאריכים בלבד**. אין בגרסה הזאת נתוני הקלקות, שיעור הקלקה, מיקום או שאילתות, וההשקה הגיעה קודם לתת-קבוצה של אתרים, אז אל תבטיחו ללקוח את הנתונים האלה לפני שווידאתם שהנכס שלו קיבל אותם. הפעילות הזאת ממשיכה להיספר גם בדוח הביצועים הכללי.

כלים חיצוניים למעקב ציטוטי AI (כמו Otterly.ai, Profound או SE Ranking AI Toolkit) מבצעים אוטומציה של שכבת ההופעה בפועל. במקביל תנטרו תעבורת הפניות מפלטפורמות AI ותחפשו את המותג שלכם בכל עוזר כדי לבדוק דיוק ציטוטים.

**בדיקות לעברית:**
1. תוודאו תצוגת RTL תקינה בכל הדפדפנים
2. תבדקו קישור hreflang דו-כיווני
3. תאשרו שרישומי ספריות מקומיות עקביים (NAP: שם, כתובת, טלפון)
4. תריצו `scripts/analyze_keywords.py --audit` לבדיקת כיסוי מילות מפתח

תסתכלו על [references/tools-and-apis.md](./references/tools-and-apis.md) לרשימה מלאה של כלי SEO/GEO חינמיים ובתשלום.

## דוגמאות

### דוגמה 1: מחקר מילות מפתח בעברית
המשתמש אומר: "אני צריך מילות מפתח לאתר נדל"ן ישראלי"
פעולות:
1. זיהוי מילות מפתח שורשיות: נדל"ן, דירה, בית
2. יצירת גרסאות מורפולוגיות: הנדל"ן, בנדל"ן, דירות (רבים), בתים (רבים)
3. צורות סמיכות: סוכן נדל"ן, מחירי דירות
4. הרצת `scripts/analyze_keywords.py --keywords "נדלן,דירה,בית"` לניתוח גרסאות מלא
5. מיפוי גרסאות לדפים לפי עדיפות נפח חיפוש
תוצאה: מפת מילות מפתח מלאה בעברית עם גרסאות מורפולוגיות וצירופי תחיליות

### דוגמה 2: הגדרת hreflang לאתר דו-לשוני
המשתמש אומר: "תגדיר hreflang לאתר ה-.co.il שלי בעברית ואנגלית"
פעולות:
1. ביקורת דפים קיימים לזוגות שפה
2. יצירת תגי hreflang link ל-head של ה-HTML בכל דף
3. יצירת מפת אתר XML עם הערות hreflang
4. אימות קישור דו-כיווני בין גרסאות שפה
תוצאה: הטמעת hreflang מלאה עם טירגוט he-IL ו-en

### דוגמה 3: אופטימיזציית GEO ל-SaaS ישראלי
המשתמש אומר: "תמטב את דף הנחיתה של ה-SaaS הישראלי שלי למנועי חיפוש AI"
פעולות:
1. ביקורת נראות AI נוכחית (לחפש את שם המותג ב-ChatGPT, Perplexity, Claude)
2. יישום שיטות GEO של פרינסטון: סטטיסטיקות עם מקורות, ציטוטי מומחים, הפניות סמכותיות
3. הטמעת FAQPage schema עם זוגות שאלות-תשובות דו-לשוניים
4. הוספת SpeakableSpecification לסעיפי תוכן מרכזיים
5. לוודא שכל בוטי ה-AI מורשים ב-robots.txt
6. מבנה תוכן בפורמט תשובה קודם עם היררכיית H2/H3 ברורה
תוצאה: דף נחיתה ממוטב גם ל-Google.co.il וגם לציטוטים במנועי חיפוש AI

### דוגמה 4: Schema למסעדה ישראלית עם GEO
המשתמש אומר: "תייצר נתונים מובנים למסעדה הכשרה שלי בירושלים"
פעולות:
1. בניית JSON-LD של LocalBusiness/Restaurant עם פורמט כתובת ישראלי
2. שעות פתיחה מותאמות שבת (סגירה מוקדמת ביום שישי, שבת סגור)
3. תעודת כשרות עם פרטי רבנות
4. FAQPage schema לשאלות נפוצות (תפריט, הזמנות, רמת כשרות)
5. SpeakableSpecification לשאילתות עוזרים קוליים
6. Schema תפריט בעברית עם תמחור בש"ח
תוצאה: סימון JSON-LD מלא ממוטב ל-Google Rich Results ולציטוטי AI

### דוגמה 5: ביקורת SEO + GEO מלאה
המשתמש אומר: "תעשה ביקורת לאתר המסחר האלקטרוני הישראלי שלי ל-SEO ולנראות AI"
פעולות:
1. הרצת `python3 scripts/seo_audit.py "https://example.co.il"` לביקורת טכנית
2. בדיקת גישת בוטי AI ב-robots.txt
3. אימות hreflang ואיכות תוכן בעברית
4. ביקורת נתונים מובנים (FAQPage, Product, BreadcrumbList schemas)
5. הערכת אותות EEAT (אישורי מחבר, ציטוטים, מומחיות בעברית)
6. בדיקת נראות AI - לחפש שם מותג ומוצרים ב-ChatGPT, Perplexity, Claude
7. סקירת דוחות ה-AI הגנרטיבי ב-Google Search Console
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
- GEO (אופטימיזציה למנועים גנרטיביים) הוא תחום שמתפתח במהירות. גורמי הדירוג של פלטפורמות AI משתנים תדיר. סוכנים עלולים להמליץ על אסטרטגיות GEO מיושנות אפילו מלפני חצי שנה. Google מציינת ש-AI Overviews זמין לכל המשתמשים בישראל ובעברית, אבל הוא לא מופיע בכל שאילתה; תתייחסו לציטוט ב-AI Overview כסיגנל שאיפתי ולא כמנוף מובטח.
- AI Overview מוריד עדיפות לתוכן עם H1/H2 ממולאים במילות מפתח. אתרים שמדורגים טוב ב-Google הקלאסי יכולים לאבד ציטוטים ב-AI Overview לטובת מתחרים בעלי תנועה נמוכה יותר אך עם פסקת תשובה ישירה נקייה. הפתרון הוא מבני (שכתוב הפתיח לפורמט answer-first), לא עוד מילות מפתח.
- LLMs ישראליים מצטטים תוכן בעברית באופן לא אחיד. דפי נחיתה SaaS פיוניריים בעברית מצוטטים פחות ב-ChatGPT/Claude מאשר דפים מקבילים עם גרסה אנגלית. תשמרו URL אנגלי חלופי עם אותו תוכן ל-AI surface, פלוס URL עברי עם hreflang תקין לדירוג ב-Google.co.il.


## קישורי עזר

| מקור | כתובת | מה לבדוק |
|------|-------|----------|
| Google Search Central | https://developers.google.com/search | גורמי דירוג, נתונים מובנים, Core Web Vitals |
| Google Search Status Dashboard | https://status.search.google.com | עדכוני ליבה פעילים, סטטוס AI Overview |
| Schema.org | https://schema.org | סימון JSON-LD ל-LocalBusiness, FAQ, Article |
| Google Keyword Planner | https://ads.google.com/intl/en/home/tools/keyword-planner/ | נפחי חיפוש בעברית, רעיונות למילות מפתח |
| האקדמיה ללשון העברית | https://hebrew-academy.org.il | מינוח עברי תקני, כללי כתיב |
| מאמר GEO של פרינסטון (Aggarwal et al., 2023) | https://arxiv.org/abs/2311.09735 | שיטות GEO למנועי חיפוש מבוססי AI |
| תיעוד בוטים של OpenAI | https://developers.openai.com/api/docs/bots | התנהגות `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `OAI-AdsBot` |
| תיעוד סורקי Anthropic | https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler | `ClaudeBot`, `Claude-SearchBot`, `Claude-User` ואיך לחסום כל אחד |
| הנחיות Google לתכונות AI | https://developers.google.com/search/docs/appearance/ai-features | מה נדרש ומה לא נדרש ל-AI Overviews ול-AI Mode |
| דוחות AI גנרטיבי ב-Search Console | https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports | אילו מדדים הדוחות באמת חושפים |
| מידע על סורקי Perplexity | https://docs.perplexity.ai/docs/resources/perplexity-crawlers | `PerplexityBot`, `Perplexity-User` |
| הצעת llms.txt | https://llmstxt.org | קונבנציה לאינדקס אתר קריא ל-AI |
| דוח AI Performance של Bing Webmaster Tools | https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview | דוח AI Performance מראה מתי Copilot מצטט אתכם |
| Brave Search | https://brave.com/search/ | אינדקס עצמאי שמיוחס לחיפוש של Claude, בלי אישור רשמי מ-Anthropic |

## פתרון בעיות

### שגיאה: "hreflang mismatch detected"
סיבה: תגי hreflang אינם דו-כיווניים (דף A מקשר ל-B אבל B לא מקשר חזרה ל-A)
פתרון: ודאו שכל הצהרת hreflang היא הדדית. גם הגרסה העברית וגם האנגלית חייבות להפנות אחת לשנייה.

### שגיאה: "RTL rendering issues"
סיבה: חסר מאפיין dir="rtl" או קונפליקטים ב-CSS עם ברירות מחדל של LTR
פתרון: תגדירו dir="rtl" על אלמנט ה-html בדפים עבריים. תשתמשו ב-CSS logical properties (margin-inline-start במקום margin-left).

### שגיאה: "Schema validation failed"
סיבה: סימון JSON-LD מכיל שגיאות או חסרים מאפיינים נדרשים
פתרון: תבדקו עם Google Rich Results Test. בעיות ישראליות נפוצות: פורמט טלפון שגוי (חובה להשתמש ב-972+), חסר addressCountry: IL, או קוד מטבע ILS.

### שגיאה: "Keywords not ranking on google.co.il"
סיבה: התוכן אולי מתורגם מכונה או שחסרות גרסאות מורפולוגיות של מילות מפתח
פתרון: תוודאו שתוכן בעברית כולל צירופי תחיליות טבעיים. תשתמשו ב-`scripts/analyze_keywords.py` כדי לזהות גרסאות חסרות.

### שגיאה: "לא מופיע בתוצאות חיפוש AI"
סיבה: בוטי AI יכולים להיות חסומים, לתוכן חסרים אותות ראויים לציטוט, או שהאתר לא מאונדקס בפלטפורמות הנדרשות
פתרון: תבדקו קודם כל גישה, לפני שאתם מסיקים משהו על איכות התוכן. תבקשו את הדף בתור כל user agent של בוט ותוודאו החזר 200 עם הטקסט קיים ב-HTML הגולמי ולא מוזרק ב-JavaScript. תוודאו ש-robots.txt מאפשר במפורש את `OAI-SearchBot`, `PerplexityBot` ו-`Claude-SearchBot`. אישור של `GPTBot` ו-`ClaudeBot` בלבד מכסה רק את סורקי האימון ומשאיר אתכם לא זכאים לציטוט בחיפוש בשתי הפלטפורמות, וזאת התקלה הנפוצה ביותר כאן. רק אחרי שהגישה תקינה, תיישמו שיטות GEO ותבנו מחדש בפורמט תשובה-קודם.

### שגיאה: "AI מצטט מתחרים במקום את האתר שלי"
סיבה: לתוכן של המתחרה יש צפיפות עובדתית גבוהה יותר, מבנה טוב יותר או ציטוטים סמכותיים יותר
פתרון: תיישמו את שיטות GEO של פרינסטון לפי הסדר שהמאמר מצא כיעיל: קודם ציטוטי מומחים עם ייחוס, אחר כך סטטיסטיקות ספציפיות עם מקורות, ואז שטף וציטוט מקורות. תשתמשו בפורמט תשובה קודם וב-FAQPage schema. תבנו סמכות נושאית דרך אשכולות תוכן.
