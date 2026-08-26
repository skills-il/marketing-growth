# Hebrew Survey Templates

Every template below was written in Hebrew first, not translated from English. The phrasings are what Israeli users would actually say out loud, direct, warm, slightly informal. Use them as-is unless the user explicitly asks for more formal language.

## `nps`, Net Promoter Score

Best for: measuring Israeli customer loyalty at the relationship level.

Scale: 0-10, with 9-10 = promoter, 7-8 = passive, 0-6 = detractor.

**Questions:**

1. (0-10 scale, required)
   - Title: עד כמה סביר שתמליצו עלינו לחבר או קולגה?
   - `lowLabel`: בכלל לא סביר
   - `highLabel`: בהחלט סביר
2. (paragraph text, optional)
   - Title: מה הסיבה המרכזית לציון שנתתם?

**Notes:**
- Do NOT add a 3rd question asking for "improvements", it hurts response rate and you already get it free-text in Q2.
- Don't use the word "ממליצים" (recommend) in both Q1 and Q2, it sounds repetitive. Q2 asks for the *reason* for the score.
- Literal English-to-Hebrew translations of NPS wording are the #1 reason response rates drop in Israel, use the phrasing above, which was written in Hebrew first.
- Interpret the score against the right baseline. Do not read a raw Israeli NPS against a US SaaS benchmark. Cross-cultural differences in how respondents use the ends of a scale are a real phenomenon in the survey-methods literature, but there is no Israel-specific measurement cited here, so treat 'Israelis score lower' as an untested hypothesis rather than a fact. The methodological point stands on its own regardless: compare each wave to your OWN previous waves. A trend in your own series is interpretable; an absolute number against someone else's benchmark is not. Compare each wave to your own previous waves, not to imported benchmarks, and hold the question wording and send-timing constant so the trend is the signal.

## `csat`, Customer Satisfaction

Best for: rating a single interaction (support ticket, order, onboarding call).

Scale: 1-5.

**Questions:**

1. (1-5 scale, required)
   - Title: עד כמה הייתם מרוצים מהחוויה?
   - `lowLabel`: ממש לא מרוצים
   - `highLabel`: ממש מרוצים
2. (multiple choice, optional), What stood out?
   - Title: מה בלט לכם?
   - Options: "המהירות", "היחס האישי", "הפתרון שקיבלתי", "אף אחד מהאפשרויות", "משהו אחר"
3. (paragraph, optional)
   - Title: משהו שנוכל לשפר?

## `ces`, Customer Effort Score

Best for: measuring how easy a specific task was (sign-up, checkout, returning a product).

Scale: 1-7 (standard CES 2.0). It is an agreement statement, so HIGHER is better (1 = strongly disagree it was easy, 7 = strongly agree it was easy). Both polarities exist in the wild: the original CES phrasing ("how easy was it...", where LOWER effort is better) is still documented by major CX vendors, while CES 2.0 uses this agreement statement where HIGHER is better. Either is defensible. What is not defensible is mixing them, or leaving the direction unstated: pick one, write the scale labels so the direction is unambiguous, and keep it constant across waves or your trend line reverses meaning halfway through.

**Questions:**

1. (1-7 scale, required)
   - Title: הצוות שלנו הקל עליכם להשלים <את הפעולה>
   - `lowLabel`: כלל לא מסכים/ה
   - `highLabel`: מסכים/ה לחלוטין
2. (paragraph, optional)
   - Title: אם משהו היה מסורבל, מה זה היה?

## `event-feedback`, Post-event debrief

Best for: meetups, workshops, webinars, the feedback form you send 24-48h after an event.

**Questions:**

1. (1-5 scale, required)
   - Title: עד כמה האירוע ענה על הציפיות שלכם?
   - `lowLabel`: בכלל לא
   - `highLabel`: לגמרי
2. (multiple choice, required), Which session did you get the most from?
   - Title: מאיזה חלק באירוע הפקתם הכי הרבה?
   - Options: list the session titles in Hebrew, plus "אף אחד במיוחד". These are respondent-facing and MUST be the real agenda titles; the script enforces this with a required `--sessions`.
3. (paragraph, optional)
   - Title: מה היה יכול להפוך את האירוע הבא לטוב יותר?
4. (multiple choice, required: כן / לא / עוד לא יודע/ת. The "not sure yet" escape is deliberate, forcing a binary on return-intent inflates both ends.)
   - Title: האם תחזרו למפגש הבא?

**Notes:**
- Don't ask for ratings per session, reduces response rate dramatically. Ask which one was *most* useful.
- The "יחזרו למפגש הבא" question is the most actionable for meetup organizers.

## `product-discovery`, Early-stage user interviews

Best for: pain-point discovery before building anything. All questions are open-ended.

**Questions:**

1. (paragraph, required)
   - Title: ספרו לנו על הפעם האחרונה שנתקלתם ב<בעיה שאתם חוקרים>. מה קרה?
   - The `<...>` slot is respondent-facing text and MUST be filled. The script enforces this with a required `--topic`.
2. (paragraph, required)
   - Title: מה ניסיתם לעשות כדי לפתור את זה?
3. (paragraph, optional)
   - Title: מה היה הכי מתסכל בתהליך?
4. (paragraph, optional)
   - Title: אם היה פתרון קסם, איך הוא היה נראה בעיניכם?

**Notes:**
- The "tell me about the last time" framing is much more valuable than "would you use a product that...". The user is forced to remember concrete behavior rather than speculate.
- Avoid the literal translation "האם תשתמשו במוצר ש-...", it invites polite "yes" answers.

## `market-research`, Demand validation for a new Israeli product

Best for: pre-launch validation, segmentation, pricing sensitivity.

**Questions:**

1. (paragraph, optional)
   - Title: יש משהו בתחום הזה שמציק לכם? אם כן, ספרו לנו מה
2. (1-5 scale, required)
   - Title: כמה זה משפיע עליכם יום-יום?
   - `lowLabel`: כמעט בכלל לא
   - `highLabel`: משפיע מאוד
3. (multiple choice, optional), Willingness to pay
   - Title: אם היה קיים פתרון שפותר את זה, כמה הייתם מוכנים לשלם עליו בחודש?
   - Options: "לא הייתי משלם/ת", "עד 20 ₪", "21-50 ₪", "51-100 ₪", "מעל 100 ₪"
4. (multiple choice, optional), Audience segment
   - Title: מה הכי מתאר אתכם?
   - Options: "עצמאי/ת", "שכיר/ה", "בעל/ת עסק קטן", "מנהל/ת בחברה", "אחר"

**Notes:**
- The pricing question is intentionally soft ("אם היה קיים פתרון"), asking hypothetically drops hostility but still gives a directional signal. Don't treat the answers as commitments.
- Always include the "לא הייתי משלם/ת" option. Forcing a price commitment creates social-desirability bias.
- **Q1 is deliberately optional and deliberately not leading.** A demand-validation survey whose first required question presupposes the problem manufactures the signal it is meant to measure: a respondent with no pain will invent one rather than abandon the form. A respondent who answers "there is no such problem for me" is a finding, not a non-response.
- **The segment question is LAST and optional, on purpose.** SKILL.md Step 9 names "segment question plus free text on a small list" as the canonical way a nominally anonymous survey re-identifies people. Leading with it, required, would make the default shape of this template break the skill's own privacy rule. Do not move it back to the top, and do not report segment cross-tabs below about n=10.
- **Pricing bands do not share boundaries.** Overlapping bands (20-50 next to 50-100) leave a respondent whose answer is exactly 50 with two defensible choices, and the distribution becomes uninterpretable exactly at the boundary where a pricing decision gets made.
- **These bands are consumer-scale.** For a B2B instrument raise them by an order of magnitude or ask for an annual figure instead.

## Formatting for `gws forms forms batchUpdate`

For every question above, the `createItem` request shape is:

```json
{
  "createItem": {
    "item": {
      "title": "<question title from this file>",
      "questionItem": {
        "question": {
          "required": true,
          "<questionType>": { ... }
        }
      }
    },
    "location": { "index": <zero-based> }
  }
}
```

Question type mapping:

| Template type | API field | Example fields |
|---------------|-----------|----------------|
| scale (NPS, CSAT, CES) | `scaleQuestion` | `low`, `high`, `lowLabel`, `highLabel` |
| paragraph text | `textQuestion` | `paragraph: true` |
| short text | `textQuestion` | (no `paragraph` flag) |
| multiple choice | `choiceQuestion` | `type: "RADIO"`, `options: [{ value }]` |
| yes/no | `choiceQuestion` | `type: "RADIO"`, two options |

Always inspect `gws schema forms.forms.batchUpdate` in your session to confirm field names match your installed gws version before sending large payloads.
