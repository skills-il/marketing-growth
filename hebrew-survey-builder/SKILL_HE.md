---
name: hebrew-survey-builder
description: "כתיבת סקרים בעברית (NPS, CSAT, CES, משוב מאירועים, ראיונות גילוי מוצר, מחקר שוק) עם ניסוח ישראלי טבעי, והרצה דרך Google Forms בעזרת Google Workspace CLI (gws) או הדבקה ל-Typeform, SurveyMonkey, Tally, Microsoft Forms, או אימייל/סלאק. כולל גם ייעוץ על תזמון לקהל ישראלי (ימים, שעות וחגים שלא כדאי להפיץ בהם). השתמשו כשמשתמש מבקש לבנות סקר בעברית, להפיץ NPS או CSAT ללקוחות ישראלים, לאסוף משוב אחרי אירוע, לראיין משתמשים בעברית, או להחליט מתי להפיץ סקר לקהל ישראלי. Use when user asks to build a Hebrew survey or run NPS in Israel. אל תשתמשו עבור טפסי ממשלה ישראליים (ראו israeli-gov-form-automator)."
license: MIT
---

# בונה סקרים בעברית

## בעיה

להריץ סקר בעברית זה כאב ראש. Google Forms יודע להציג עברית מימין לשמאל אוטומטית, אבל החלק הקשה הוא לבחור את השאלות הנכונות, לנסח אותן בעברית ישראלית טבעית (ולא בתרגום מילולי מאנגלית), ולייצר את הטופס בלי להיכנס בכלל לממשק. רוב הצוותים מסתפקים בתבנית אנגלית גרועה אחרי Google Translate, והאחוז היענות צונח.

הסקיל הזה נותן לסוכן לבנות סקר שלם בעברית מקצה לקצה דרך `gws forms forms create` ו-`gws forms forms batchUpdate`, ולהחזיר קישור חי לסקר בתוך פרומפט אחד.

## הוראות

### שלב 0: להחליט אם Google Forms זו הפלטפורמה הנכונה

קודם כל לשאול את המשתמש לאיזה כלי הוא רוצה להפיץ את הסקר:

- **פריסה ל-Google Forms**, להשתמש בזרימת `gws` למטה (שלבים 1-9). מחזיר קישור חי לשיתוף.
- **אין גישה למעטפת (shell)** (קלוד דסקטופ, וכל מארח שלא יכול להריץ בינארי מקומי), לכו באותו מסלול כמו שאר הפלטפורמות: `gws` הוא כלי שורת פקודה, ולכן מסלול הפריסה ל-Google Forms פשוט לא זמין שם. הפיקו את התבניות בעברית ואת תוכנית התזמון, ומסרו למשתמש תוכן מוכן להדבקה.
- **פלטפורמות אחרות** (Typeform, SurveyMonkey, Tally, Microsoft Forms, אימייל, סלאק, וואטסאפ), לדלג על שלבי `gws`. לעבור ישר לשלב 1 (בחירת תבנית) ואז ל-`references/export-to-other-platforms.md` להנחיות הדבקה לפי כלי. ניסוח השאלות בעברית וכללי התזמון הישראליים תקפים בכל מקרה.

אם המשתמש כן הולך ל-Google Forms, לוודא ש-`gws` גם מותקן וגם מחובר. אלה שתי בדיקות שונות:

```bash
gws forms --help                              # מותקן? מדפיס usage
gws drive files list --params '{"pageSize": 1}'   # מחובר? דורש הרשאות אמיתיות
```

הפקודה `--help` מסתיימת בהצלחה גם בלי שום הרשאות, אז בפני עצמה היא לא מוכיחה כלום לגבי החיבור. דילוג על הפקודה השנייה הוא הדרך הנפוצה ביותר שבה התהליך מת בשלב 2 עם שגיאת הרשאות במקום בשלב 0 עם שגיאה ברורה.

מבנה הפקודה הוא `gws <service> <resource> [sub-resource] <method>`, ולכן פונים למשאב forms שבתוך שירות forms בתור `gws forms forms <method>`. הכפילות הזו אינה טעות הקלדה.

אם הפקודה לא נמצאת, להפנות את המשתמש להתקין את Google Workspace CLI מ-`github.com/googleworkspace/cli` (בינארי מוכן, או דרך מנהל חבילות כמו npm, Homebrew או cargo, ראו את מקטע ההתקנה במאגר לפקודות העדכניות) ולהתחבר. לא להמציא תשובה ולא להשתמש בכלי אחר. אם המשתמש לא רוצה להתקין את `gws`, אפשר להציע לייצר את התבניות ב-Markdown ולהפנות ל-`references/export-to-other-platforms.md`.

### שלב 1: לבחור תבנית סקר

לשאול את המשתמש איזה סוג סקר הוא צריך ולהתאים לתבנית מתוך `references/hebrew-survey-templates.md`:

| תבנית | מתי להשתמש | סולם |
|-------|--------------|------|
| `nps` | מדידת נאמנות לקוחות ישראלים | 0-10 |
| `csat` | דירוג אינטראקציה בודדת (הזמנה, פנייה לתמיכה) | 1-5 |
| `ces` | מידת המאמץ שנדרש למשתמש (הרשמה, תשלום) | 1-7 |
| `event-feedback` | תחקיר אחרי אירוע (מיטאפ, הרצאה, סדנה) | מעורב |
| `product-discovery` | ראיונות משתמשים בשלב מוקדם | שאלות פתוחות |
| `market-research` | אימות ביקוש למוצר ישראלי חדש | מעורב |

אם הכוונה של המשתמש לא מתאימה לאחת מהתבניות, לשאול שאלת הבהרה אחת. לא לדחוף תבנית שלא מתאימה.

### שלב 2: ליצור טופס ריק

המתודה `create` מקבלת רק `info.title` ו-`info.documentTitle`, לפי Google Forms API. כל שאר השדות (description, items, settings) חייבים להיכנס ב-batchUpdate נפרד. זו מגבלה קשיחה, אל תנסו להעביר שאלות בשלב היצירה.

```bash
gws forms forms create --json '{
  "info": {
    "title": "סקר NPS - <שם חברה>",
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
gws forms forms batchUpdate --params '{"formId": "<FORM_ID>"}' --json '{
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

השדה `location.index` הוא מיקום השאלה בטופס (מתחיל מ-0). חייבים להגדיר אותו גם בהוספת שאלה בודדת, אחרת הבקשה נדחית.

### שלב 4: לכתוב לתוך הטופס את הפתיח וטקסט ההסכמה

המתודה `create` לא מאפשרת `description`, ולכן את שורת האנונימיות או את ההודעה המלאה צריך להגדיר כאן, באותה קריאת `batchUpdate` של השאלות. אם מדלגים על זה, לטופס אין פתיח בכלל, ולחובות ההסכמה שבשלב 9 אין שום דרך להגיע למשיב.

```bash
gws forms forms batchUpdate --params '{"formId": "<FORM_ID>"}' --json '{
  "requests": [
    {
      "updateFormInfo": {
        "info": { "description": "התשובות בסקר הזה אנונימיות ולא נאספים בו פרטים מזהים." },
        "updateMask": "description"
      }
    }
  ]
}'
```

הסקריפט המצורף עושה את זה בשבילכם: `--intro anonymous` כותב את שורת האנונימיות, ו-`--intro identified` כותב את הטקסט שהעברתם ב-`--notice` וגם מוסיף פריט הסכמה חובה באינדקס 0, בדיוק במקום שבו שלב 9 דורש שהוא יישב. ההחלטה אם הסקר אנונימי או מזוהה מתקבלת **עכשיו**, לפני הפרסום, לא אחריו.

### שלב 5: לקבל קישור שיתוף

למשוך את פרטי הטופס ולהחזיר את `responderUri`:

```bash
gws forms forms get --params '{"formId": "<FORM_ID>"}'
```

שדה `responderUri` הוא ה-URL שמשתפים עם המשיבים. **הוא לא עובד עד שהטופס מפורסם, ראו שלב 6.** זה מה שהמשתמש באמת רוצה, להתחיל איתו בתשובה. להחזיר גם את ה-`formId` כדי שיוכל לפתוח מחדש את הטופס בממשק אחר כך.

### שלב 6: לפרסם את הטופס (חובה מאז 30 ביוני 2026)

טופס שנוצר דרך ה-API כבר לא מקבל תשובות עד שמפרסמים אותו. גוגל שינתה את ברירת המחדל: "forms created by the API after June 30, 2026 will be created in an unpublished state. You must publish the forms before they can accept responses", וגם "If no action is taken, then new forms created using APIs after June 30, 2026, will be in an unpublished state by default and won't receive responses."

זו הדרך הכי סבירה למסור למשתמש סקר מת. הקישור נפתח, הטופס נראה תקין, ובשקט לא נאסף כלום. אל תדלגו על השלב הזה ואל תתייחסו אליו כאל ליטוש אופציונלי.

```bash
# קודם בודקים את המבנה המדויק של publishSettings
gws schema forms.forms.setPublishSettings

gws forms forms setPublishSettings \
  --params '{"formId": "<FORM_ID>"}' \
  --json '{"publishSettings": {"publishState": {"isPublished": true, "isAcceptingResponses": true}}, "updateMask": "publishState"}'
```

אחר כך הריצו שוב `gws forms forms get` ואמתו את מצב הפרסום לפני שאתם מוסרים את ה-`responderUri`. קודם מפרסמים, אחר כך מוסרים את הקישור: הסדר הזה הוא מה שמונע מכם לשלוח סקר מת.

שתי הערות נלוות:

- לטפסים ישנים ("legacy forms") אין בכלל את השדה `publishSettings`, כי הם נוצרו לפני מודל הפרסום. לטפסים שנוצרים דרך ה-API יש.
- כדי להגביל מי יכול לענות במקום לשתף קישור פתוח, שתפו את הטופס עם משתמשים ספציפיים דרך `permissions.create` של Drive API. זו קריאה נפרדת ולא דגל של `publishSettings`.

### שלב 7: חיבור ל-Sheets (פעולת ממשק, לא API)

ל-Google Forms API אין כרגע מתודה שמחברת את תשובות הטופס לגיליון Google Sheet ספציפי. זו פעולה חד-פעמית שצריך לעשות בממשק:

1. לפתוח את הטופס בעורך של Forms (את ה-`formId` מקבלים מ-`gws forms forms get`; להדביק אותו בכתובת הטופס בדפדפן או לפתוח מ-Drive).
2. ללחוץ על הלשונית **תגובות** (Responses).
3. ללחוץ על האייקון הירוק של Sheets → **צור גיליון חדש** (או לבחור קיים).

להגיד למשתמש שזו פעולה של לחיצה אחת, ואחריה כל תגובה חדשה תירשם לגיליון אוטומטית. אל תתיימרו שהסקיל עושה את זה.

אם המשתמש רוצה גישה תכנותית לתגובות במקום, אפשר להשתמש ב-`gws forms forms responses list --params '{"formId": "<FORM_ID>"}'` ולשפוך את התוצאות לגיליון דרך `gws sheets`.

### שלב 8: לבחור מתי להפיץ, לקהל ישראלי

סקר מנוסח מצוין שמופץ בזמן הלא נכון יקבל אחוז היענות עלוב. לפני שלוחצים על שיתוף, כדאי לחשוב מתי הסקר ייפול לתיבות:

- **לא להפיץ אחרי הצהריים ביום שישי ובשבת.** שומרי מסורת לא יראו את זה, ועד יום ראשון הסקר נקבר בתיבה.
- **לא להפיץ בשבועות של חג**, סוכות, פסח, ראש השנה, עשרת ימי תשובה, שבועות, יום הזיכרון/יום העצמאות. אחוז ההיענות קורס בשבועות האלה.
- **הימים הכי טובים**: ראשון (תיבות פתוחות לשבוע חדש), שלישי-רביעי (היומיים החזקים ביותר ב-B2B). חמישי עובד אבל נחלש ככל שהיום מתקדם.
- **השעות הכי טובות**: 09:00-11:00 בבוקר, ו-13:00-14:00 אחרי הצהריים. להימנע מלפני 08:30 או אחרי 20:00.
- **סקרים טרנזקציוניים** (CSAT אחרי פנייה לתמיכה, משוב אחרי אירוע) להפיץ מיד אחרי האינטראקציה ולא בבאץ' יומי, אבל אם האירוע נגמר בחמישי בערב, עדיף לחכות עד ראשון בבוקר.

עץ החלטה מלא וקצבים לפי סוג סקר (NPS רבעוני מול חודשי, CSAT לפי פנייה מול באץ', וכו') נמצאים ב-`references/israeli-send-timing.md`. כדאי להציץ שם לפני שסוגרים קצב.

### שלב 9: שיתוף, ובדיקת הסכמה לפני שליחה

אחרי ששלב 6 פרסם את הטופס, ה-responder link עובד לכל מי שמקבל אותו, בכפוף להגבלות הדומיין של חשבון Google Workspace.

**הסכמה ופרטיות.** כברירת מחדל כדאי לשמור על תשובות NPS, CSAT ו-CES אנונימיות, זה גם מגן על המשיבים וגם מעלה את אחוז ההיענות. חובת ההסכמה מדעת לגבי מידע אישי מזוהה קיימת בדין הישראלי הרבה לפני הרפורמה האחרונה. מה שתיקון 13 (בתוקף מ-14 באוגוסט 2025) שינה כאן הוא בעיקר **ההודעה** שחייבים למשיב: מי בעל השליטה במאגר ואיך יוצרים איתו קשר, מה המשמעות של סירוב למסור את המידע, והזכות לעיין במידע ולתקן אותו. אז לפני שמשתפים את הטופס צריך לבדוק אם הוא באמת אנונימי ולא רק נראה אנונימי:

- **טופס בלי שדה מזהה עדיין יכול להיות מזוהה.** שליחת קישור אישי לסקר לרשימת לקוחות, או הטמעת מזהה אישי בקישור, מזהה כל תשובה גם אם הטופס לא מבקש שם או אימייל. צריך להתייחס לזרימה הזו כמזוהה: ליידע את הנמענים מה נאסף ולמה, לתת אפשרות הסרה, ולא לעשות שימוש חוזר ברשימה מעבר לסקר הזה.
- **לכבות את "איסוף כתובות אימייל" בסקרים אנונימיים חיצוניים.** בתוך דומיין של Google Workspace, Google Forms יכול לאסוף אוטומטית את כתובת החשבון של המשיב, וזה שובר בשקט הבטחה לאנונימיות. כדאי לכבות אלא אם באמת צריך זיהוי.
- **להיזהר עם מדגמים קטנים.** שאלת סגמנט (עצמאי / שכיר / בעל עסק) יחד עם הערה חופשית ברשימה קטנה (מפגש, קהל B2B נישתי) מזהה אנשים. אין לבצע פילוח או לדווח על סגמנטים עם מספר תשובות בודד.
- **אם בכל זאת צריך זיהוי** (למשל NPS עם בקשת יצירת קשר), צריך להוסיף שאלת הסכמה ראשונה וחובה ("אני מאשר/ת שאפשר ליצור איתי קשר בעקבות התשובות") *לפני* כל שדה מזהה, ולעולם לא לסמן אותה מראש.

בסקר אנונימי באמת, שורת פתיחה אחת ("התשובות אנונימיות") מספיקה. בזרימות המזוהות שלמעלה צריך לתת הודעה מלאה יותר (מה נאסף, למה, ואפשרות הסרה) ולא שורה אחת. עבור טפסים שאוספים מידע רגיש או ממשלתי, יש להפנות ל-`israeli-gov-form-automator`.

## שרתי MCP מומלצים

| MCP | מתי לשלב |
|-----|----------|
| אין בזמן הכתיבה | אין עדיין MCP ייעודי לסקרים או Google Forms ב-skills-il. להשתמש ב-`gws` ישירות. |

## קישורי עזר

| מקור | קישור | מה לבדוק |
|------|-------|----------|
| מאגר Google Workspace CLI | https://github.com/googleworkspace/cli | הוראות התקנה, הערות גרסה, אימות |
| שינויים ב-API של Google Forms | https://developers.google.com/workspace/forms/api/guides/api-changes-to-google-forms | השינוי של "לא מפורסם כברירת מחדל" ותהליך הפרסום |
| מוסכמות משותפות של gws | https://raw.githubusercontent.com/googleworkspace/cli/main/skills/gws-shared/SKILL.md | מבנה הפקודה והצורה של --params כ-JSON |
| סקיל gws-forms הרשמי | https://raw.githubusercontent.com/googleworkspace/cli/main/skills/gws-forms/SKILL.md | רשימת המתודות הקאנונית של `gws forms` |
| תיעוד Google Forms API v1 | https://developers.google.com/workspace/forms/api/reference/rest/v1/forms | רשימת המתודות (create, get, batchUpdate, setPublishSettings) |
| תיעוד batchUpdate | https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/batchUpdate | מבני הבקשות (CreateItemRequest וכו') |
| תבניות סקרים בעברית | `references/hebrew-survey-templates.md` | ניסוחי NPS, CSAT, CES בעברית טבעית |
| מדריך תזמון לקהל ישראלי | `references/israeli-send-timing.md` | ימי שבוע, שעות, שבועות של חג שכדאי להימנע מהם, קצבים לפי סוג סקר |
| הדבקה לכלים שאינם Google | `references/export-to-other-platforms.md` | איך לקחת את אותן תבניות עברית ל-Typeform, SurveyMonkey, Tally, Microsoft Forms, או אימייל/סלאק |

## משאבים מצורפים

### סקריפטים
- `scripts/build_batchupdate_payload.py`, מקבל שם תבנית (`nps`, `csat`, `ces`, `event-feedback`, `product-discovery`, `market-research`) ומחזיר JSON מוכן לזרוק ל-`gws forms forms batchUpdate --json`.

  ```bash
  python3 scripts/build_batchupdate_payload.py --template nps --intro anonymous
  python3 scripts/build_batchupdate_payload.py --template product-discovery --topic 'ניהול הוצאות בעסק קטן'
  python3 scripts/build_batchupdate_payload.py --template event-feedback --sessions 'פתיחה,הרצאת אורח,פאנל'
  python3 scripts/build_batchupdate_payload.py --template ces --task 'את ההרשמה'
  ```

  הדגלים `--topic` ו-`--sessions` הם **חובה** בתבניות שלהם והסקריפט ייכשל בלעדיהם. זה מכוון: לשתי התבניות האלה יש מקום ריק בתוך נוסח השאלה שהמשיב רואה, ומילוי גנרי ("הבעיה שאנחנו חוקרים", "החלק הראשון") מייצר שאלה שאי אפשר לענות עליה בצורה משמעותית. הדגל `--task` אופציונלי, אבל שם הפעולה הוא מה שהופך את ה-CES לשמיש. הדגל `--intro anonymous|identified` קובע את תיאור הטופס, ו-`identified` גם מוסיף את פריט ההסכמה החובה באינדקס 0.

### מסמכי עזר
- `references/hebrew-survey-templates.md`, רשימת שאלות לכל תבנית בעברית ישראלית טבעית, עם תוויות סולם, סוגי שאלות והערות מתי כל תבנית מתאימה.
- `references/gws-forms-cheatsheet.md`, המתודות המדויקות של `gws forms`, מבנה הפקודות, ופקודות הגילוי, משוכפל מה-SKILL.md הרשמי של gws-forms כדי שתוכלו לעבוד גם בלי אינטרנט.
- `references/israeli-send-timing.md`, מתי להפיץ סקרים לקהל ישראלי (ימי שבוע, שעות, שבועות של חג, וקצבים לפי סוג סקר).
- `references/export-to-other-platforms.md`, איך להשתמש באותן תבניות עברית וכללי תזמון עם Typeform, SurveyMonkey, Tally, Microsoft Forms, או אימייל/סלאק במקרה ש-Google Forms לא הכלי הנכון.

## מלכודות נפוצות

אלה הטעויות שסוכן יעשה בפעם הראשונה:

1. **לנסות להעביר items בזמן `create`.** המתודה `create` מעתיקה רק את `info.title` ואת `info.documentTitle`. כל השאר (description, items, settings) לא מותר. התיעוד של gws אומר רק שהשדות האלה אסורים, ולא אם הם נזרקים בשקט או מוחזרת שגיאה, אז אל תניחו אף אחת מהאפשרויות: קראו את התשובה במקום להסתמך על שגיאה שאולי לא תגיע, ואמתו שהטופס שנוצר ריק לפני שעושים לתוכו `batchUpdate`.
2. **לקרוא ל-`forms.update` במקום ל-`forms.batchUpdate`.** ב-Google Forms API v1 אין מתודה `forms.update`. המתודות היחידות על המשאב `forms` הן `create`, `get`, `batchUpdate` ו-`setPublishSettings`. אם רואים `update` בבלוגים ישנים, זה באמת `batchUpdate`.
3. **להניח שה-API מחבר תגובות ל-Google Sheet.** הוא לא. הכפתור "קישור ל-Sheets" הוא ממשק בלבד. צריך להגיד למשתמש לעשות את זה פעם אחת בלחיצה, או למשוך תגובות דרך `forms.responses.list` ולכתוב ל-Sheet עם `gws sheets`.
4. **לתרגם ניסוחי NPS מאנגלית מילולית.** "How likely are you to recommend us to a friend or colleague?" בתרגום מילה-במילה נשמע פאסיבי ומוזר בעברית. להשתמש בניסוחים מ-`references/hebrew-survey-templates.md`, הם נכתבו בעברית מההתחלה, לא תורגמו. זו הסיבה מספר אחת להיענות נמוכה לסקרים בישראל.
5. **לשכוח את `location.index` בבקשת `createItem`.** גם בהוספת שאלה בודדת, `location.index` חובה. להתחיל מ-0 ולהעלות.
6. **למסור את ה-`responderUri` בלי לפרסם.** מאז 30 ביוני 2026 טופס שנוצר דרך ה-API מתחיל במצב לא מפורסם ולא מקבל תשובות. הקישור נפתח, הטופס מוצג, וכל שליחה פשוט בלתי אפשרית בשקט. תמיד להריץ `setPublishSettings` (שלב 6) לפני שמוסרים את הקישור.
7. **לכתוב `--params formId=<ID>`.** הדגל `--params` מקבל אובייקט JSON ולא `key=value`: `--params '{"formId": "<ID>"}'`. ה-CLI מפרסר אותו בקפדנות ודוחה כל דבר אחר.
8. **להשמיט את שם המשאב.** הפקודה היא `gws forms forms create` ולא `gws forms create`. התבנית היא `gws <service> <resource> <method>`, וכאן גם השירות וגם המשאב נקראים forms. אותה כפילות מופיעה ב-`gws schema forms.forms.batchUpdate`, שהסקיל תמיד כתב נכון.
9. **להשתמש בעברית ב-`documentTitle`.** `documentTitle` הוא שם הקובץ ב-Drive. חלק מתהליכי החיפוש ב-Drive מתמודדים פחות טוב עם שמות בעברית, עדיף להשאיר את `documentTitle` ב-ASCII ולשים את הגרסה העברית ב-`info.title` (הכותרת שהמשתמשים רואים).

## דוגמאות

### דוגמה 1: סקר NPS מהיר ל-SaaS ישראלי
המשתמש אומר: "אני צריך להפיץ NPS ללקוחות שלי, אפשר לבנות לי סקר?"

פעולות:
1. לבחור את התבנית `nps`.
2. `gws forms forms create` עם הכותרת "סקר NPS - <חברה>".
3. `gws forms forms batchUpdate` עם ה-payload של שתי שאלות NPS מ-`references/hebrew-survey-templates.md`.
4. `gws forms forms setPublishSettings` כדי לפרסם (חובה), ואז `gws forms forms get` → להחזיר את `responderUri`.
5. להסביר איך לחבר ל-Sheets בלחיצה אחת אם רוצים את התגובות בגיליון.

### דוגמה 2: סקר משוב אחרי מיטאפ
המשתמש אומר: "תבנה סקר משוב בעברית למיטאפ שהיה אתמול בתל אביב, עד 5 שאלות, תכלול שאלה על אם יחזרו."

פעולות:
1. לבחור את התבנית `event-feedback`.
2. לצמצם ל-5 שאלות, לשים "האם תחזרו למפגש הבא?" כשאלה אחרונה.
3. `create` + `batchUpdate` + `setPublishSettings`.
4. להחזיר את קישור השיתוף.

## פתרון בעיות

### שגיאה: `gws: command not found`
סיבה: Google Workspace CLI לא מותקן ב-PATH.
פתרון: להתקין מ-https://github.com/googleworkspace/cli (להוריד את הבינארי המוכן לפי מערכת ההפעלה, או דרך מנהל חבילות כמו npm, Homebrew או cargo, ראו את מקטע ההתקנה במאגר) ולהתחבר. אל תחליפו בכלי אחר ואל תנסו לקרוא ישירות ל-REST API אלא אם המשתמש ביקש במפורש.

### שגיאה: `INVALID_ARGUMENT` ב-`gws forms forms create` כשמעבירים items
סיבה: `create` דוחה כל דבר חוץ מ-`info.title` ו-`info.documentTitle`.
פתרון: להוציא מה-payload של `create` את `items`, `description` ו-`settings`. להוסיף אותם אחר כך דרך `batchUpdate`.

### שגיאה: `CreateItemRequest.location.index is required`
סיבה: בקשת `createItem` חסרה את `location` או את `location.index`.
פתרון: תמיד לכלול `"location": { "index": <מספר> }` גם בהוספת שאלה בודדת.

### שגיאה: `forms.update not found`
סיבה: קוראים למתודה שלא קיימת ב-Google Forms API v1.
פתרון: להשתמש ב-`forms.batchUpdate` עם בקשת `updateItem` בתוך המערך `requests`, לא `forms.update`.

### שגיאת הרשאות בקריאת ה-`create` הראשונה
סיבה: `gws` מותקן אבל לא מחובר, או מחובר בלי ההרשאות ל-Forms ול-Drive.
פתרון: להריץ מחדש את תהליך ההתחברות של gws ולאשר גישה ל-Forms ול-Drive, ואז לבדוק שוב עם `gws drive files list --params '{"pageSize": 1}'` לפני שחוזרים לשלב 2.

### הקישור לטופס עובד אבל אף תשובה לא מגיעה
סיבה: הטופס נוצר דרך ה-API אחרי 30 ביוני 2026 ומעולם לא פורסם, ולכן הוא לא מקבל תשובות.
פתרון: להריץ `gws forms forms setPublishSettings` (שלב 6), ואז לאמת עם `gws forms forms get` לפני ששולחים את הקישור שוב.

### שגיאה: `Invalid --params JSON`
סיבה: הועבר ל-`--params` ערך בצורת `key=value` במקום אובייקט JSON.
פתרון: להעביר `--params '{"formId": "<ID>"}'`. לעטוף בגרשיים בודדים כדי שהמעטפת לא תיגע בגרשיים הכפולים שבפנים.

### הטקסט בעברית מופיע משמאל לימין
סיבה: לעיתים רחוקות, כותרת שמתחילה בתו ASCII גורמת לפסקה להיות LTR למרות שהתוכן בעברית.
פתרון: לשים את העברית בתחילת ה-`title` (בלי סימני פיסוק או מספר בהתחלה). Google Forms מזהה את כיוון הטקסט לפי התו החזק הראשון.
