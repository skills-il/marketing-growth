# Domain coverage checklist, hebrew-survey-builder

Anchor for expert review. Scope: building and deploying Hebrew surveys (NPS, CSAT, CES, event, discovery, market research) for Israeli audiences via Google Forms (gws CLI) or other platforms, plus Israeli send-timing.

## Must cover (core)
- Correct survey-instrument conventions: NPS 0-10 (promoter 9-10 / passive 7-8 / detractor 0-6), CSAT 1-5, CES 1-7. (Standard CX definitions.)
- Natural Israeli Hebrew phrasing, not literal English-to-Hebrew translation (the #1 driver of low IL response rates).
- Google Forms deployment via gws: `create` (title + documentTitle only) then `batchUpdate` for items; share via `responderUri`. (Upstream gws-forms skill + Forms API v1.)
- No `forms.update` method exists in Forms API v1 (only create/get/batchUpdate/setPublishSettings).
- Responses-to-Sheets link is UI-only, not exposed by the API.
- Israeli send-timing: avoid Friday afternoon/Shabbat and chag weeks; best Sunday + Tue/Wed mornings; per-survey-type cadence.
- Consent/privacy: keep NPS/CSAT/CES anonymous by default; if responses are identifiable, Privacy Protection Law Amendment 13 (in force Aug 2025) requires explicit consent and a clear notice of what is collected and why.
- Platform portability: same Hebrew templates work on Typeform, SurveyMonkey, Tally, Microsoft Forms, email/Slack.

## Should cover (advanced)
- RTL rendering: Google Forms infers direction from the first strong character; keep documentTitle ASCII, Hebrew in info.title.
- gws install channels (binary + package managers) and auth prerequisite.
- Cadence guardrails: NPS quarterly (monthly feels spammy to IL B2B), CSAT per-ticket not per-agent, discovery interviews spaced ≥2 weeks.

## Out of scope (explicit)
- Israeli government / PII-heavy forms, deferred to `israeli-gov-form-automator`.
- Statistical analysis of results / dashboards.
- Email-deliverability / domain authentication (SPF/DKIM), a separate concern from survey authoring.

## Authoritative sources
- Google Workspace CLI (gws): https://github.com/googleworkspace/cli
- gws-forms canonical skill: https://raw.githubusercontent.com/googleworkspace/cli/main/skills/gws-forms/SKILL.md
- Google Forms API v1: https://developers.google.com/workspace/forms/api/reference/rest/v1/forms
- Privacy Protection Law Amendment 13: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
