---
name: hebrew-survey-builder
description: "Create live Google Forms in Hebrew with RTL-aware templates for NPS, CSAT, event feedback, product discovery, and market research, using the Google Workspace CLI (gws). Also advises on Israeli-specific send timing (days, hours, chagim to avoid). Use when the user asks to build a survey in Hebrew, run an NPS or CSAT for Israeli customers, collect event feedback, run user interviews in Hebrew, decide when to send a survey to Israeli audiences, or asks about \"סקר\", \"שאלון\", \"משוב\", \"NPS\", \"CSAT\", or survey cadence. Produces a real, shareable Google Form URL with questions that render right-to-left, not a static document. Do NOT use for Typeform, SurveyMonkey, Tally, or Israeli government forms (see israeli-gov-form-automator)."
license: MIT
compatibility: Requires the Google Workspace CLI (gws) to be installed and authenticated, plus a Google account with Forms access. Works with Claude Code, Cursor, GitHub Copilot, Windsurf, and openclaw.
---

# Hebrew Survey Builder

## Problem

Running surveys in Hebrew is painful. Google Forms renders Hebrew text right-to-left automatically, but the hard part is choosing the right questions, phrasing them in natural Israeli Hebrew (not stiff literal translations from English), and actually creating the form without clicking through the UI. Most teams default to bad English templates run through Google Translate, which tank response rates.

This skill lets an agent build a complete Hebrew survey end-to-end using `gws forms create` + `gws forms batchUpdate`, returning a live, shareable form URL within a single prompt.

## Instructions

### Step 0: Verify gws is installed and authenticated

Before doing anything, confirm the agent has the tool and it is wired up:

```bash
gws forms --help
```

If the command is not found, tell the user to install the Google Workspace CLI from `github.com/googleworkspace/cli` and authenticate it. Do not attempt to fabricate a response. Do not use a different CLI.

### Step 1: Pick the survey template

Ask the user which kind of survey they need. Map their intent to one of these templates in `references/hebrew-survey-templates.md`:

| Template | When to use | Scale |
|----------|-------------|-------|
| `nps` | Measure Israeli customer loyalty | 0–10 |
| `csat` | Rate a single interaction / order / support ticket | 1–5 |
| `ces` | Measure effort of a task (e.g. sign-up, checkout) | 1–7 |
| `event-feedback` | Post-event debrief (meetups, workshops, webinars) | mixed |
| `product-discovery` | Early-stage user interviews about a pain point | open-ended |
| `market-research` | Demand validation for a new Israeli product | mixed |

If the user's intent doesn't fit cleanly, ask one clarifying question. Don't force a template that doesn't match.

### Step 2: Create the empty form

The `create` method only accepts the form title and document_title, per the Google Forms API. All other fields (description, items, settings) must be added in a separate `batchUpdate` call. This is a hard constraint — do not try to pass items at creation time.

```bash
gws forms create --json '{
  "info": {
    "title": "סקר NPS – <company name>",
    "documentTitle": "NPS Survey <date>"
  }
}'
```

Capture the `formId` from the response. You need it for every following call.

The `documentTitle` is the filename as it appears in Google Drive. Keep it ASCII so the file is easy to find in Drive; put the Hebrew in `title` (the title users see on the form itself).

### Step 3: Add questions via batchUpdate

Use `forms.batchUpdate` with a `requests` array. Each question is a `createItem` request. To inspect the exact parameter shape first:

```bash
gws schema forms.forms.batchUpdate
```

Build the payload from the template you chose in Step 1. Example for a 2-question NPS form:

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

`location.index` is the zero-based position of the item in the form. Always set it, even for a single-item insert — the API rejects the request otherwise.

### Step 4: Get the share URL

Fetch the form metadata and return the `responderUri` to the user:

```bash
gws forms get --params formId=<FORM_ID>
```

The `responderUri` field is the public URL to share with respondents. This is what the user actually wants — lead with it in your reply. Also include the `formId` so the user can re-open the form in the Forms UI later.

### Step 5: Guide Sheets linking (UI step, not API)

The Google Forms API does not currently expose a method to connect a form's responses to a specific Google Sheet. This must be done once in the UI:

1. Open the form in the Forms editor (the URL comes back from `gws forms get`; copy the `formId` into the browser-side Forms UI, or open it from Drive).
2. Click the **Responses** tab.
3. Click the green Sheets icon → **Create a new spreadsheet** (or select an existing one).

Tell the user this is a one-time click, and that after it's done, every new response will land in the linked Sheet automatically. Do not claim the skill handles this step.

If the user wants API-level response access instead, use `gws forms responses list --params formId=<FORM_ID>` to pull responses and pipe them into `gws sheets` yourself.

### Step 6: Pick the right send time for Israeli audiences

A perfectly worded survey sent at the wrong time tanks your response rate. Before you push the form, think about *when* it will land in people's inboxes:

- **Avoid Friday afternoon and Shabbat.** Observant recipients are offline; by Sunday it's buried.
- **Avoid chag weeks entirely** — Sukkot, Pesach, Rosh Hashanah, Yom Kippur period, Shavuot, Yom HaZikaron/Yom HaAtzmaut. Response rates collapse during these weeks.
- **Best days**: Sunday (fresh inboxes), Tuesday–Wednesday (strongest B2B engagement). Thursday is acceptable but drifts softer late in the day.
- **Best hours**: 09:00–11:00 morning window, 13:00–14:00 post-lunch lull. Avoid before 08:30 or after 20:00.
- **Transactional surveys** (post-ticket CSAT, post-event feedback) should fire immediately after the interaction, not on a batch schedule — but still hold them for Sunday morning if the event ended Thursday evening.

The full decision tree and per-survey-type cadence (NPS quarterly vs monthly, CSAT per-ticket vs batched, etc.) is in `references/israeli-send-timing.md`. Consult it before committing to a cadence.

### Step 7: Publish and share

By default, a newly created form is accessible to anyone with the responder link, inside the creator's Google account rules (Workspace domain restrictions still apply). If the user needs to change who can respond, use:

```bash
gws schema forms.forms.setPublishSettings
```

to see the exact `publishSettings` shape, then call `gws forms setPublishSettings` with the right flags. The Google Forms API notes that legacy forms do not support `publish_settings` — newly created API forms do.

## Recommended MCP Servers

| MCP | When to pair |
|-----|--------------|
| None at time of writing | No Hebrew-survey or Google Forms MCP is published on skills-il yet. Use `gws` CLI directly. |

## Reference Links

| Source | URL | What to check |
|--------|-----|---------------|
| Google Workspace CLI repo | https://github.com/googleworkspace/cli | Install instructions, release notes, auth flow |
| Official gws-forms skill | https://raw.githubusercontent.com/googleworkspace/cli/main/skills/gws-forms/SKILL.md | Canonical list of gws forms methods and constraints |
| Google Forms API v1 reference | https://developers.google.com/workspace/forms/api/reference/rest/v1/forms | Authoritative method list (create, get, batchUpdate, setPublishSettings) |
| Forms batchUpdate reference | https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/batchUpdate | Request types (CreateItemRequest, UpdateItemRequest, etc.) |
| Hebrew survey templates (local) | `references/hebrew-survey-templates.md` | NPS, CSAT, CES, event, product discovery wording |
| Israeli send-time guide (local) | `references/israeli-send-timing.md` | Day/hour guidance, chag weeks to avoid, cadence rules |

## Bundled Resources

### Scripts
- `scripts/build_batchupdate_payload.py` — take a template name (`nps`, `csat`, `ces`, `event-feedback`, `product-discovery`, `market-research`) and emit a ready-to-pipe JSON payload for `gws forms batchUpdate --json`. Usage: `python3 scripts/build_batchupdate_payload.py --template nps`.

### References
- `references/hebrew-survey-templates.md` — every template's question list in natural Israeli Hebrew, with scale labels, question types, and notes on when each template is appropriate.
- `references/gws-forms-cheatsheet.md` — the exact gws forms methods, command structure, and discovery commands, mirrored from the upstream `gws-forms` skill so you can work offline.
- `references/israeli-send-timing.md` — when to send surveys to Israeli audiences (day of week, time of day, chag weeks to avoid, per-survey-type cadence rules).

## Gotchas

These are the mistakes an agent will most likely make on first try:

1. **Trying to pass items at `create` time.** The `create` method only copies `info.title` and `info.documentTitle`. Everything else (description, items, settings) is silently disallowed. You MUST follow up with `batchUpdate` to add questions.
2. **Calling `forms.update` instead of `forms.batchUpdate`.** Google Forms API v1 does NOT have a `forms.update` method. The only methods on the forms resource are `create`, `get`, `batchUpdate`, and `setPublishSettings`. If you see `update` in older docs or blog posts, substitute `batchUpdate`.
3. **Assuming the API links responses to a Google Sheet.** It doesn't. The "Link to Sheets" button is UI-only. Tell the user to do it once by hand, or poll `forms.responses.list` and write to a Sheet yourself via `gws sheets`.
4. **Translating English NPS phrasing literally.** "How likely are you to recommend us to a friend or colleague?" translated word-for-word sounds stiff and passive in Hebrew. Use the wording in `references/hebrew-survey-templates.md` — it was written in Hebrew first, not translated. This is the main reason bad surveys get bad response rates in Israel.
5. **Forgetting `location.index` in a `createItem` request.** Even for a single-question insert, `location.index` is required. Start at `0` and increment.
6. **Using Hebrew in `documentTitle`.** `documentTitle` is the Drive filename. Some Drive search flows handle Hebrew filenames awkwardly — keep `documentTitle` in ASCII, put the Hebrew version in `info.title` (the user-facing form title).

## Examples

### Example 1: Quick NPS for an Israeli SaaS
User says: "אני צריך להפיץ NPS ללקוחות שלי, אפשר לבנות לי סקר?"

Actions:
1. Pick the `nps` template.
2. `gws forms create` with title "סקר NPS – <company>".
3. `gws forms batchUpdate` with the 2-question NPS payload from `references/hebrew-survey-templates.md`.
4. `gws forms get` → return the `responderUri`.
5. Tell the user how to link to Sheets in one click if they want responses in a spreadsheet.

### Example 2: Post-event feedback for a meetup
User says: "Build a post-event survey in Hebrew for yesterday's Tel Aviv meetup, 5 questions max, include one about whether they'd come again."

Actions:
1. Pick the `event-feedback` template.
2. Trim it to 5 questions, keep "האם תחזרו למפגש הבא?" as the last question.
3. `create` + `batchUpdate`.
4. Return the share link.

## Troubleshooting

### Error: `gws: command not found`
Cause: Google Workspace CLI is not installed on PATH.
Solution: Install from https://github.com/googleworkspace/cli (download the pre-built binary for your OS), then re-authenticate. Do not attempt to substitute another CLI or `curl` the REST API directly unless the user explicitly asks.

### Error: `INVALID_ARGUMENT` on `gws forms create` when passing items
Cause: `create` rejects everything except `info.title` and `info.documentTitle`.
Solution: Remove `items`, `description`, and `settings` from the create payload. Add them afterwards via `batchUpdate`.

### Error: `CreateItemRequest.location.index is required`
Cause: The createItem request was missing `location` or `location.index`.
Solution: Always include `"location": { "index": <number> }` even for a single-item insert.

### Error: `forms.update not found`
Cause: Calling a method that doesn't exist in the Google Forms API v1.
Solution: Use `forms.batchUpdate` with an `updateItem` request inside the `requests` array, not `forms.update`.

### Hebrew text appears left-to-right in the created form
Cause: Very rarely, a title that starts with an ASCII character will direct the paragraph LTR even though the body is Hebrew.
Solution: Put Hebrew first in `title` (no leading punctuation or number). Google Forms infers direction from the first strong character.
