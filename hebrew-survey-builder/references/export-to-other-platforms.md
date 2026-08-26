# Exporting Hebrew Surveys to Non-Google Platforms

The Hebrew question wording from `hebrew-survey-templates.md` and the timing rules from `israeli-send-timing.md` are platform-agnostic. You only need the `gws forms` flow if you're deploying to Google Forms. For any other tool, copy the question text directly into that tool's form builder.

This reference covers Typeform, SurveyMonkey, Tally, Microsoft Forms, and lightweight channels (email, Slack, WhatsApp).

## General workflow (applies everywhere)

1. Pick a template from `references/hebrew-survey-templates.md` (NPS, CSAT, CES, event-feedback, product-discovery, market-research).
2. Copy the Hebrew question strings, titles, scale labels, options.
3. Paste into the target tool's form builder, matching the question type (rating scale → scale question, paragraph → long text, multiple choice → radio/dropdown).
4. Set the survey's display language or locale to Hebrew where the tool offers it. This affects system-level strings ("Submit" button, progress bar, error messages) so the whole form feels native.
5. Preview the form before sending to confirm Hebrew renders right-to-left. If a title looks LTR, it usually means a leading ASCII character or digit is throwing off BiDi detection, put Hebrew first.

## Typeform

- Start a new typeform and set its display language to Hebrew in settings.
- For NPS/CSAT/CES-style rating questions, use Typeform's rating-scale question type and configure the range to match the template (NPS is 0-10, CSAT is 1-5, CES is 1-7).
- Paste Hebrew titles and scale labels directly into each question's title field.
- Use Typeform's long-text block for open-ended follow-ups.
- Preview in the Typeform builder, Hebrew renders RTL natively.

## SurveyMonkey

- Create a new survey and set the survey language to Hebrew in the survey settings so the system strings (Next, Back, Submit) are localized.
- Use the rating-scale question type for scaled questions and the multiple-choice type for options.
- Paste Hebrew titles, scale anchors, and option text directly.
- Always preview before sending; SurveyMonkey previews show exactly what respondents will see.

## Tally.so

- Create a new form in the Tally form builder.
- Use the rating/scale block for NPS/CSAT/CES and the long-text block for open-ended questions.
- RTL is a **manual setting**, not automatic. Tally lists Hebrew among three RTL-supported languages (Arabic, Hebrew, Yoruba), and per its own docs: "When you select one of these languages, the Text direction setting will appear. Choose the text direction and click Save changes." Set it before you publish, or Hebrew ships LTR.
- Tally is a reasonable option for users who want something simple, fast, and non-Google. It is especially useful for Israeli indie hackers and solo founders.

## Microsoft Forms

- Create a new form and set the form language to Hebrew in Forms settings. This is the path for Israeli enterprise/education environments on Microsoft 365.
- The rating question type and the Likert-style question type cover scale-based surveys; the long-answer type covers open-ended questions.
- Paste Hebrew template text into question titles and sub-labels.
- Useful when the organization already standardizes on Microsoft 365 and has stricter IT approval paths around adding new SaaS tools.

## Plain email / Slack / WhatsApp (lightweight option)

For very short surveys (two or three questions at most), skip form builders entirely:

- Copy the Hebrew template questions into an email, Slack thread, or WhatsApp broadcast.
- Responses come back as text replies, plan to aggregate manually in a spreadsheet.
- Only appropriate for small, tight audiences where you personally know the recipients.
- Do NOT send lightweight "text-reply" surveys to a general mailing list, response rates are lower than a proper form, and you lose structured scale data.

## What still applies, regardless of platform

- **Timing rules** from `references/israeli-send-timing.md`, day of week, time of day, chag weeks, cadence per survey type
- **Hebrew question wording** from `references/hebrew-survey-templates.md`, written in Hebrew first, not translated
- **The "don't translate literally" rule**, the single biggest cause of low response rates in Israel. Copy the Hebrew from the templates verbatim; do not run it through a paraphraser or polishing pass that will drift it back toward English patterns.

## Gotchas when moving between platforms

1. **Don't re-translate through a second channel.** Every time the Hebrew text passes through a translator, paraphraser, or "cleanup" pass, it drifts back toward literal-English phrasing. Copy the Hebrew directly from the reference file and do not touch it.
2. **Always preview RTL before sending.** If you see Hebrew displayed LTR in the preview, it will look broken to recipients. Do not assume auto-detection: it varies by platform.

   | Platform | RTL behaviour | Source |
   |---|---|---|
   | SurveyMonkey | Automatic. "Hebrew, Arabic, and Persian text automatically displays in RTL orientation." | help.surveymonkey.com multilingual-surveys |
   | Typeform | Supported. "Currently, the only right-to-left languages supported are Arabic and Hebrew." | help.typeform.com form-language |
   | Tally | Manual toggle, see above | tally.so/help/supported-languages |
   | Microsoft Forms | Hebrew is a supported interface language, but Microsoft documents nothing about RTL rendering. Preview before committing. | support.microsoft.com languages-supported |
   | Google Forms | Infers direction from the first strong character; a title starting with ASCII or a digit can flip the paragraph LTR. | see SKILL.md Troubleshooting |

3. **Check the free tier before you commit to a platform.** A survey tool that caps responses below your list size wastes the whole send.

   | Platform | Free-tier constraint worth knowing |
   |---|---|
   | Microsoft Forms | On a personal Microsoft account, "the number of responses a form/quiz can receive is up to 200 for free accounts up to 1,000 for paid accounts". Work/school accounts are far higher. |
   | SurveyMonkey | The free Basic plan caps questions per survey (10 at time of writing) and limits how many responses you can view. Check the current pricing page. |
   | Typeform | The free plan's monthly response cap is low enough that a real NPS wave will exhaust it. Check the current pricing page before choosing Typeform for anything at volume. |
   | Tally | Generous free tier, which is why it suits solo founders and indie hackers. |
   | Google Forms | No response cap that a normal survey will reach, which is the main practical reason to prefer it for a large Israeli list. Google does publish per-form limits; check them if your list is very large. |

   Pricing pages change often. Treat the numbers above as a prompt to check, not as current fact.
3. **Do not manually reverse NPS scale numbers.** In Hebrew, users read right-to-left, so on a 0-10 NPS scale some platforms visually flip the scale (10 on the left, 0 on the right). This is correct, do not manually reverse the numbers to "fix" it.
4. **Email subject lines must also be in Hebrew.** For surveys sent via email, the subject line should be Hebrew to match the body. Match the subject language to the body. A Hebrew survey behind an English subject line reads as a mismatched mass mailing to recipients, which is reason enough; no deliverability measurement is cited for it here.
5. **Map question types carefully.** A "rating" in one tool may not support the same range as another. Check before assuming, NPS needs 0-10, CES needs 1-7, and some tools default to 1-5 for all ratings, which silently corrupts your analysis.

## Which platform should I pick?

| Need | Best fit |
|------|----------|
| Free, fast, Google-native, works with `gws` CLI | Google Forms (use `gws forms` flow in SKILL.md) |
| Beautiful branded look, conversational feel | Typeform |
| Enterprise analytics, advanced logic, larger response pools | SurveyMonkey |
| Free and lightweight, Google Forms alternative | Tally |
| Already on Microsoft 365, IT prefers it | Microsoft Forms |
| Tiny audience you personally know (< 10 people) | Email or Slack thread |
