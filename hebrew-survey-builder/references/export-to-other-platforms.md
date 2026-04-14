# Exporting Hebrew Surveys to Non-Google Platforms

The Hebrew question wording from `hebrew-survey-templates.md` and the timing rules from `israeli-send-timing.md` are platform-agnostic. You only need the `gws forms` flow if you're deploying to Google Forms. For any other tool, copy the question text directly into that tool's form builder.

This reference covers Typeform, SurveyMonkey, Tally, Microsoft Forms, and lightweight channels (email, Slack, WhatsApp).

## General workflow (applies everywhere)

1. Pick a template from `references/hebrew-survey-templates.md` (NPS, CSAT, CES, event-feedback, product-discovery, market-research).
2. Copy the Hebrew question strings — titles, scale labels, options.
3. Paste into the target tool's form builder, matching the question type (rating scale → scale question, paragraph → long text, multiple choice → radio/dropdown).
4. Set the survey's display language or locale to Hebrew where the tool offers it. This affects system-level strings ("Submit" button, progress bar, error messages) so the whole form feels native.
5. Preview the form before sending to confirm Hebrew renders right-to-left. If a title looks LTR, it usually means a leading ASCII character or digit is throwing off BiDi detection — put Hebrew first.

## Typeform

- Start a new typeform and set its display language to Hebrew in settings.
- For NPS/CSAT/CES-style rating questions, use Typeform's rating-scale question type and configure the range to match the template (NPS is 0-10, CSAT is 1-5, CES is 1-7).
- Paste Hebrew titles and scale labels directly into each question's title field.
- Use Typeform's long-text block for open-ended follow-ups.
- Preview in the Typeform builder — Hebrew renders RTL natively.

## SurveyMonkey

- Create a new survey and set the survey language to Hebrew in the survey settings so the system strings (Next, Back, Submit) are localized.
- Use the rating-scale question type for scaled questions and the multiple-choice type for options.
- Paste Hebrew titles, scale anchors, and option text directly.
- Always preview before sending; SurveyMonkey previews show exactly what respondents will see.

## Tally.so

- Create a new form in the Tally form builder.
- Use the rating/scale block for NPS/CSAT/CES and the long-text block for open-ended questions.
- Hebrew text renders RTL automatically in the published form.
- Tally is a reasonable option for users who want something simple, fast, and non-Google. It is especially useful for Israeli indie hackers and solo founders.

## Microsoft Forms

- Create a new form and set the form language to Hebrew in Forms settings. This is the path for Israeli enterprise/education environments on Microsoft 365.
- The rating question type and the Likert-style question type cover scale-based surveys; the long-answer type covers open-ended questions.
- Paste Hebrew template text into question titles and sub-labels.
- Useful when the organization already standardizes on Microsoft 365 and has stricter IT approval paths around adding new SaaS tools.

## Plain email / Slack / WhatsApp (lightweight option)

For very short surveys (two or three questions at most), skip form builders entirely:

- Copy the Hebrew template questions into an email, Slack thread, or WhatsApp broadcast.
- Responses come back as text replies — plan to aggregate manually in a spreadsheet.
- Only appropriate for small, tight audiences where you personally know the recipients.
- Do NOT send lightweight "text-reply" surveys to a general mailing list — response rates are lower than a proper form, and you lose structured scale data.

## What still applies, regardless of platform

- **Timing rules** from `references/israeli-send-timing.md` — day of week, time of day, chag weeks, cadence per survey type
- **Hebrew question wording** from `references/hebrew-survey-templates.md` — written in Hebrew first, not translated
- **The "don't translate literally" rule** — the single biggest cause of low response rates in Israel. Copy the Hebrew from the templates verbatim; do not run it through a paraphraser or polishing pass that will drift it back toward English patterns.

## Gotchas when moving between platforms

1. **Don't re-translate through a second channel.** Every time the Hebrew text passes through a translator, paraphraser, or "cleanup" pass, it drifts back toward literal-English phrasing. Copy the Hebrew directly from the reference file and do not touch it.
2. **Always preview RTL before sending.** If you see Hebrew displayed LTR in the preview, it will look broken to recipients. Most platforms auto-detect direction, but some have quirks around titles that start with ASCII characters or digits.
3. **Do not manually reverse NPS scale numbers.** In Hebrew, users read right-to-left, so on a 0-10 NPS scale some platforms visually flip the scale (10 on the left, 0 on the right). This is correct — do not manually reverse the numbers to "fix" it.
4. **Email subject lines must also be in Hebrew.** For surveys sent via email, the subject line should be Hebrew to match the body. English subject + Hebrew body gets filed as spam more often.
5. **Map question types carefully.** A "rating" in one tool may not support the same range as another. Check before assuming — NPS needs 0-10, CES needs 1-7, and some tools default to 1-5 for all ratings, which silently corrupts your analysis.

## Which platform should I pick?

| Need | Best fit |
|------|----------|
| Free, fast, Google-native, works with `gws` CLI | Google Forms (use `gws forms` flow in SKILL.md) |
| Beautiful branded look, conversational feel | Typeform |
| Enterprise analytics, advanced logic, larger response pools | SurveyMonkey |
| Free and lightweight, Google Forms alternative | Tally |
| Already on Microsoft 365, IT prefers it | Microsoft Forms |
| Tiny audience you personally know (< 10 people) | Email or Slack thread |
