---
name: hebrew-survey-builder
description: "יצירת סקרי Google Forms חיים בעברית עם תבניות RTL ל-NPS, CSAT, משוב מאירועים, ראיונות גילוי מוצר ומחקר שוק, וגם ייעוץ על תזמון (ימים, שעות וחגים שלא כדאי להפיץ בהם). השתמשו כשמשתמש מבקש לבנות סקר בעברית, להפיץ NPS או CSAT ללקוחות ישראלים, לאסוף משוב אחרי אירוע, לראיין משתמשים בעברית, או להחליט מתי להפיץ סקר לקהל ישראלי. מחזיר קישור עובד ל-Google Form, לא מסמך סטטי. Use when user asks to build a Hebrew survey or run NPS in Israel. אל תשתמשו עבור Typeform, SurveyMonkey, Tally או טפסי ממשלה."
license: MIT
---

# בונה סקרים בעברית

## בעיה

להריץ סקר בעברית זה כאב ראש. Google Forms יודע להציג עברית מימין לשמאל אוטומטית, אבל החלק הקשה הוא לבחור את השאלות הנכונות, לנסח אותן בעברית ישראלית טבעית (ולא בתרגום מילולי מאנגלית), ולייצר את הטופס בלי להיכנס בכלל לממשק. רוב הצוותים מסתפקים בתבנית אנגלית גרועה אחרי Google Translate, והאחוז היענות צונח.

הסקיל הזה נותן לסוכן לבנות סקר שלם בעברית מקצה לקצה דרך `gws forms create` ו-`gws forms batchUpdate`, ולהחזיר קישור חי לסקר בתוך פרומפט אחד.

## הוראות

### שלב 0: לוודא ש-gws מותקן ומחובר

לפני הכל, לבדוק שהכלי זמין ומוגדר:

```bash
gws forms --help
```

אם הפקודה לא נמצאת, להפנות את המשתמש להתקין את Google Workspace CLI מ-`github.com/googleworkspace/cli` ולהתחבר. לא להמציא תשובה ולא להשתמש בכלי אחר.

### שלב 1: לבחור תבנית סקר

לשאול את המשתמש איזה סוג סקר הוא צריך ולהתאים לתבנית מתוך `references/hebrew-survey-templates.md`:

| תבנית | מתי להשתמש | סולם |
|-------|--------------|------|
| `nps` | מדידת נאמנות לקוחות ישראלים | 0–10 |
| `csat` | דירוג אינטראקציה בודדת (הזמנה, פנייה לתמיכה) | 1–5 |
| `ces` | מידת המאמץ שנדרש למשתמש (הרשמה, תשלום) | 1–7 |
| `event-feedback` | תחקיר אחרי אירוע (מיטאפ, הרצאה, סדנה) | מעורב |
| `product-discovery` | ראיונות משתמשים בשלב מוקדם | שאלות פתוחות |
| `market-research` | אימות ביקוש למוצר ישראלי חדש | מעורב |

אם הכוונה של המשתמש לא מתאימה לאחת מהתבניות, לשאול שאלת הבהרה אחת. לא לדחוף תבנית שלא מתאימה.

### שלב 2: ליצור טופס ריק

המתודה `create` מקבלת רק `info.title` ו-`info.documentTitle`, לפי Google Forms API. כל שאר השדות (description, items, settings) חייבים להיכנס ב-batchUpdate נפרד. זו מגבלה קשיחה — אל תנסו להעביר שאלות בשלב היצירה.

```bash
gws forms create --json '{
  "info": {
    "title": "סקר NPS – <שם חברה>",
    "documentTitle": "NPS Survey <תאריך>"
  }
}'
```

לשמור את ה-`formId` מהתגובה. צריך אותו לכל קריאה אחר כך.

ה-`documentTitle` הוא שם הקובץ ב-Google Drive. מומלץ להשאיר אותו ב-ASCII כדי שיהיה קל למצוא ב-Drive; את העברית לשים ב-`title` (הכותרת שמופיעה בטופס עצמו).

### שלב 3: להוסיף שאלות דרך batchUpdate

לקרוא ל-`forms.batchUpdate` עם מערך `requests`. כל שאלה היא בקשת `createItem`. לבדוק קודם את מבנה הפרמטרים:

```bash
gws schema forms.forms.batchUpdate
```

לבנות את ה-payload מהתבנית. דוגמה לטופס NPS בן שתי שאלות:

```bash
gws forms batchUpdate --params formId=<FORM_ID> --json '{
  "requests": [
    {
      "createItem": {
        "item": {
          "title": "עד כמה סביר שתמליצו עלינו לחבר או קולגה?",
          "questionItem": {
            "question": {
              "required": true,
              "scaleQuestion": {
                "low": 0,
                "high": 10,
                "lowLabel": "בכלל לא סביר",
                "highLabel": "בהחלט סביר"
              }
            }
          }
        },
        "location": { "index": 0 }
      }
    },
    {
      "createItem": {
        "item": {
          "title": "מה הסיבה המרכזית לציון שנתתם?",
          "questionItem": {
            "question": {
              "required": false,
              "textQuestion": { "paragraph": true }
            }
          }
        },
        "location": { "index": 1 }
      }
    }
  ]
}'
```

השדה `location.index` הוא מיקום השאלה בטופס (מתחיל מ-0). חייבים להגדיר אותו גם בהוספת שאלה בודדת — אחרת הבקשה נדחית.

### שלב 4: לקבל קישור שיתוף

למשוך את פרטי הטופס ולהחזיר את `responderUri`:

```bash
gws forms get --params formId=<FORM_ID>
```

שדה `responderUri` הוא ה-URL הציבורי שמשתפים עם המשיבים. זה מה שהמשתמש באמת רוצה — להתחיל איתו בתשובה. להחזיר גם את ה-`formId` כדי שיוכל לפתוח מחדש את הטופס בממשק אחר כך.

### שלב 5: חיבור ל-Sheets (פעולת ממשק, לא API)

ל-Google Forms API אין כרגע מתודה שמחברת את תשובות הטופס לגיליון Google Sheet ספציפי. זו פעולה חד-פעמית שצריך לעשות בממשק:

1. לפתוח את הטופס בעורך של Forms (את ה-`formId` מקבלים מ-`gws forms get`; להדביק אותו בכתובת הטופס בדפדפן או לפתוח מ-Drive).
2. ללחוץ על הלשונית **תגובות** (Responses).
3. ללחוץ על האייקון הירוק של Sheets → **צור גיליון חדש** (או לבחור קיים).

להגיד למשתמש שזו פעולה של לחיצה אחת, ואחריה כל תגובה חדשה תירשם לגיליון אוטומטית. אל תתיימרו שהסקיל עושה את זה.

אם המשתמש רוצה גישה תכנותית לתגובות במקום, אפשר להשתמש ב-`gws forms responses list --params formId=<FORM_ID>` ולשפוך את התוצאות לגיליון דרך `gws sheets`.

### שלב 6: לבחור מתי להפיץ — לקהל ישראלי

סקר מנוסח מצוין שמופץ בזמן הלא נכון יקבל אחוז היענות עלוב. לפני שלוחצים על שיתוף, כדאי לחשוב מתי הסקר ייפול לתיבות:

- **לא להפיץ אחרי הצהריים ביום שישי ובשבת.** שומרי מסורת לא יראו את זה, ועד יום ראשון הסקר נקבר בתיבה.
- **לא להפיץ בשבועות של חג** — סוכות, פסח, ראש השנה, עשרת ימי תשובה, שבועות, יום הזיכרון/יום העצמאות. אחוז ההיענות קורס בשבועות האלה.
- **הימים הכי טובים**: ראשון (תיבות פתוחות לשבוע חדש), שלישי–רביעי (היומיים החזקים ביותר ב-B2B). חמישי עובד אבל נחלש לקראת הצהריים.
- **השעות הכי טובות**: 09:00–11:00 בבוקר, ו-13:00–14:00 אחרי הצהריים. להימנע מלפני 08:30 או אחרי 20:00.
- **סקרים טרנזקציוניים** (CSAT אחרי פנייה לתמיכה, משוב אחרי אירוע) להפיץ מיד אחרי האינטראקציה ולא בבאץ' יומי — אבל אם האירוע נגמר בחמישי בערב, עדיף לחכות עד ראשון בבוקר.

עץ החלטה מלא וקצבים לפי סוג סקר (NPS רבעוני מול חודשי, CSAT לפי פנייה מול באץ', וכו') נמצאים ב-`references/israeli-send-timing.md`. כדאי להציץ שם לפני שסוגרים קצב.

### שלב 7: פרסום ושיתוף

כברירת מחדל, טופס שנוצר דרך ה-API נגיש לכל מי שמקבל את ה-responder link, בכפוף להגבלות הדומיין של חשבון Google Workspace. אם צריך לשנות מי יכול להשיב:

```bash
gws schema forms.forms.setPublishSettings
```

לבדוק את מבנה `publishSettings` ואז לקרוא ל-`gws forms setPublishSettings` עם הדגלים המתאימים. שימו לב: לטפסים ישנים ("legacy forms") אין את השדה `publish_settings`. טפסים שנוצרו דרך ה-API כן תומכים בו.

## שרתי MCP מומלצים

| MCP | מתי לשלב |
|-----|----------|
| אין בזמן הכתיבה | אין עדיין MCP ייעודי לסקרים או Google Forms ב-skills-il. להשתמש ב-`gws` ישירות. |

## קישורי עזר

| מקור | קישור | מה לבדוק |
|------|-------|----------|
| מאגר Google Workspace CLI | https://github.com/googleworkspace/cli | הוראות התקנה, הערות גרסה, אימות |
| סקיל gws-forms הרשמי | https://raw.githubusercontent.com/googleworkspace/cli/main/skills/gws-forms/SKILL.md | רשימת המתודות הקאנונית של `gws forms` |
| תיעוד Google Forms API v1 | https://developers.google.com/workspace/forms/api/reference/rest/v1/forms | רשימת המתודות (create, get, batchUpdate, setPublishSettings) |
| תיעוד batchUpdate | https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/batchUpdate | מבני הבקשות (CreateItemRequest וכו') |
| תבניות סקרים בעברית | `references/hebrew-survey-templates.md` | ניסוחי NPS, CSAT, CES בעברית טבעית |
| מדריך תזמון לקהל ישראלי | `references/israeli-send-timing.md` | ימי שבוע, שעות, שבועות של חג שכדאי להימנע מהם, קצבים לפי סוג סקר |

## משאבים מצורפים

### סקריפטים
- `scripts/build_batchupdate_payload.py` — מקבל שם תבנית (`nps`, `csat`, `ces`, `event-feedback`, `product-discovery`, `market-research`) ומחזיר JSON מוכן לזרוק ל-`gws forms batchUpdate --json`. שימוש: `python3 scripts/build_batchupdate_payload.py --template nps`.

### מסמכי עזר
- `references/hebrew-survey-templates.md` — רשימת שאלות לכל תבנית בעברית ישראלית טבעית, עם תוויות סולם, סוגי שאלות והערות מתי כל תבנית מתאימה.
- `references/gws-forms-cheatsheet.md` — המתודות המדויקות של `gws forms`, מבנה הפקודות, ופקודות הגילוי — משוכפל מה-SKILL.md הרשמי של gws-forms כדי שתוכלו לעבוד גם בלי אינטרנט.
- `references/israeli-send-timing.md` — מתי להפיץ סקרים לקהל ישראלי (ימי שבוע, שעות, שבועות של חג, וקצבים לפי סוג סקר).

## מלכודות נפוצות

אלה הטעויות שסוכן יעשה בפעם הראשונה:

1. **לנסות להעביר items בזמן `create`.** המתודה `create` מעתיקה רק את `info.title` ואת `info.documentTitle`. כל השאר (description, items, settings) לא מותר. חייב לעשות `batchUpdate` אחרי זה כדי להוסיף שאלות.
2. **לקרוא ל-`forms.update` במקום ל-`forms.batchUpdate`.** ב-Google Forms API v1 אין מתודה `forms.update`. המתודות היחידות על המשאב `forms` הן `create`, `get`, `batchUpdate` ו-`setPublishSettings`. אם רואים `update` בבלוגים ישנים, זה באמת `batchUpdate`.
3. **להניח שה-API מחבר תגובות ל-Google Sheet.** הוא לא. הכפתור "קישור ל-Sheets" הוא ממשק בלבד. צריך להגיד למשתמש לעשות את זה פעם אחת בלחיצה, או למשוך תגובות דרך `forms.responses.list` ולכתוב ל-Sheet עם `gws sheets`.
4. **לתרגם ניסוחי NPS מאנגלית מילולית.** "How likely are you to recommend us to a friend or colleague?" בתרגום מילה-במילה נשמע פאסיבי ומוזר בעברית. להשתמש בניסוחים מ-`references/hebrew-survey-templates.md` — הם נכתבו בעברית מההתחלה, לא תורגמו. זו הסיבה מספר אחת להיענות נמוכה לסקרים בישראל.
5. **לשכוח את `location.index` בבקשת `createItem`.** גם בהוספת שאלה בודדת, `location.index` חובה. להתחיל מ-0 ולהעלות.
6. **להשתמש בעברית ב-`documentTitle`.** `documentTitle` הוא שם הקובץ ב-Drive. חלק מתהליכי החיפוש ב-Drive מתמודדים פחות טוב עם שמות בעברית — עדיף להשאיר את `documentTitle` ב-ASCII ולשים את הגרסה העברית ב-`info.title` (הכותרת שהמשתמשים רואים).

## דוגמאות

### דוגמה 1: סקר NPS מהיר ל-SaaS ישראלי
המשתמש אומר: "אני צריך להפיץ NPS ללקוחות שלי, אפשר לבנות לי סקר?"

פעולות:
1. לבחור את התבנית `nps`.
2. `gws forms create` עם הכותרת "סקר NPS – <חברה>".
3. `gws forms batchUpdate` עם ה-payload של שתי שאלות NPS מ-`references/hebrew-survey-templates.md`.
4. `gws forms get` → להחזיר את `responderUri`.
5. להסביר איך לחבר ל-Sheets בלחיצה אחת אם רוצים את התגובות בגיליון.

### דוגמה 2: סקר משוב אחרי מיטאפ
המשתמש אומר: "תבנה סקר משוב בעברית למיטאפ שהיה אתמול בתל אביב, עד 5 שאלות, תכלול שאלה על אם יחזרו."

פעולות:
1. לבחור את התבנית `event-feedback`.
2. לצמצם ל-5 שאלות, לשים "האם תחזרו למפגש הבא?" כשאלה אחרונה.
3. `create` + `batchUpdate`.
4. להחזיר את קישור השיתוף.

## פתרון בעיות

### שגיאה: `gws: command not found`
סיבה: Google Workspace CLI לא מותקן ב-PATH.
פתרון: להתקין מ-https://github.com/googleworkspace/cli (להוריד את הבינארי המוכן לפי מערכת ההפעלה) ולהתחבר. אל תחליפו בכלי אחר ואל תנסו לקרוא ישירות ל-REST API אלא אם המשתמש ביקש במפורש.

### שגיאה: `INVALID_ARGUMENT` ב-`gws forms create` כשמעבירים items
סיבה: `create` דוחה כל דבר חוץ מ-`info.title` ו-`info.documentTitle`.
פתרון: להוציא מה-payload של `create` את `items`, `description` ו-`settings`. להוסיף אותם אחר כך דרך `batchUpdate`.

### שגיאה: `CreateItemRequest.location.index is required`
סיבה: בקשת `createItem` חסרה את `location` או את `location.index`.
פתרון: תמיד לכלול `"location": { "index": <מספר> }` גם בהוספת שאלה בודדת.

### שגיאה: `forms.update not found`
סיבה: קוראים למתודה שלא קיימת ב-Google Forms API v1.
פתרון: להשתמש ב-`forms.batchUpdate` עם בקשת `updateItem` בתוך המערך `requests`, לא `forms.update`.

### הטקסט בעברית מופיע משמאל לימין
סיבה: לעיתים רחוקות, כותרת שמתחילה בתו ASCII גורמת לפסקה להיות LTR למרות שהתוכן בעברית.
פתרון: לשים את העברית בתחילת ה-`title` (בלי סימני פיסוק או מספר בהתחלה). Google Forms מזהה את כיוון הטקסט לפי התו החזק הראשון.
