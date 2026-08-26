---
name: hebrew-survey-builder
description: "Write Hebrew surveys (NPS, CSAT, CES, event feedback, product discovery, market research) with natural Israeli phrasing, and either deploy them as live Google Forms via the Google Workspace CLI (gws) or paste them into Typeform, SurveyMonkey, Tally, Microsoft Forms, or email/Slack. Also advises on Israeli-specific send timing (days, hours, chagim to avoid) and cadence. Use when the user asks to build a survey in Hebrew, run an NPS or CSAT for Israeli customers, collect event feedback, run user interviews in Hebrew, decide when to send a survey to Israeli audiences, or asks about \"סקר\", \"שאלון\", \"משוב\", \"NPS\", \"CSAT\", or survey cadence. Do NOT use for Israeli government forms (see israeli-gov-form-automator)."
license: MIT
compatibility: The Google Forms deployment path needs the Google Workspace CLI (gws) installed and authenticated plus a Google account with Forms access, so it runs only on shell-capable hosts (Claude Code, Cursor, openclaw). On Claude Desktop the skill still produces paste-ready Hebrew templates and the send-timing plan; see Step 0.
---

# Hebrew Survey Builder

## Problem

Running surveys in Hebrew is painful. Google Forms renders Hebrew text right-to-left automatically, but the hard part is choosing the right questions, phrasing them in natural Israeli Hebrew (not stiff literal translations from English), and actually creating the form without clicking through the UI. Most teams default to bad English templates run through Google Translate, which tank response rates.

This skill lets an agent build a complete Hebrew survey end-to-end using `gws forms forms create` + `gws forms forms batchUpdate`, returning a live, shareable form URL within a single prompt.

## Instructions

### Step 0: Decide if Google Forms is the right target

Start by asking which tool the user wants the survey deployed on:

- **Google Forms**, use the `gws` flow below (Steps 1-9). Produces a live, shareable URL.
- **No shell available** (Claude Desktop, and any host that cannot run a local binary), take the same route as the non-Google platforms below: `gws` is a CLI, so the Google Forms deployment path is unavailable there by construction. Produce the Hebrew templates and the timing plan, and hand the user paste-ready content.
- **Typeform, SurveyMonkey, Tally, Microsoft Forms, email, Slack, WhatsApp**, skip the `gws` steps. Go straight to Step 1 (pick template), then jump to `references/export-to-other-platforms.md` for per-tool paste-in instructions. The Hebrew question wording and Israeli timing rules apply regardless of platform.

If the user is deploying to Google Forms, confirm the `gws` CLI is installed **and** authenticated. These are two different checks:

```bash
gws forms --help                              # installed? prints usage
gws drive files list --params '{"pageSize": 1}'   # authenticated? needs real credentials
```

`--help` exits 0 with no credentials at all, so on its own it proves nothing about auth. Skipping the second command is the most common way this flow dies at Step 2 with an auth error instead of at Step 0 with a clear one.

Command shape is `gws <service> <resource> [sub-resource] <method>`, so the forms resource inside the forms service is addressed as `gws forms forms <method>`. The doubled word is not a typo.

If the command is not found, tell the user to install the Google Workspace CLI from `github.com/googleworkspace/cli` (a pre-built binary, or via a package manager such as npm, Homebrew, or cargo, see the repo's install section for the current commands) and authenticate it. Do not attempt to fabricate a response. Do not use a different CLI. If the user does not want to install `gws`, offer to generate the templates in Markdown and point them to `references/export-to-other-platforms.md` instead.

### Step 1: Pick the survey template

Ask the user which kind of survey they need. Map their intent to one of these templates in `references/hebrew-survey-templates.md`:

| Template | When to use | Scale |
|----------|-------------|-------|
| `nps` | Measure Israeli customer loyalty | 0-10 |
| `csat` | Rate a single interaction / order / support ticket | 1-5 |
| `ces` | Measure effort of a task (e.g. sign-up, checkout) | 1-7 |
| `event-feedback` | Post-event debrief (meetups, workshops, webinars) | mixed |
| `product-discovery` | Early-stage user interviews about a pain point | open-ended |
| `market-research` | Demand validation for a new Israeli product | mixed |

If the user's intent doesn't fit cleanly, ask one clarifying question. Don't force a template that doesn't match.

### Step 2: Create the empty form

The `create` method only accepts the form title and document_title, per the Google Forms API. All other fields (description, items, settings) must be added in a separate `batchUpdate` call. This is a hard constraint, do not try to pass items at creation time.

```bash
gws forms forms create --json '{
  "info": {
    "title": "סקר NPS - <company name>",
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

`location.index` is the zero-based position of the item in the form. Always set it, even for a single-item insert, the API rejects the request otherwise.

### Step 4: Write the intro and consent text into the form

`create` disallows `description`, so the anonymity line or the fuller notice has to be set here, in the same `batchUpdate` pass as the questions. If you skip this the form has no intro at all, and the consent obligations in Step 8 have no delivery path.

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

The bundled script does this for you: `--intro anonymous` writes the anonymity line, and `--intro identified` writes your `--notice` text AND prepends a required consent item at index 0, which is where Step 8 requires it to sit. Decide anonymous-vs-identifiable **now**, before the form is published, not after.

### Step 5: Get the share URL

Fetch the form metadata and return the `responderUri` to the user:

```bash
gws forms forms get --params '{"formId": "<FORM_ID>"}'
```

The `responderUri` field is the URL to share with respondents. **It does not work until the form is published; see Step 6.** This is what the user actually wants, lead with it in your reply. Also include the `formId` so the user can re-open the form in the Forms UI later.

### Step 6: Publish the form (MANDATORY since 30 June 2026)

**A form created through the API no longer accepts responses until you publish it.** Google changed the default: "forms created by the API after June 30, 2026 will be created in an unpublished state. You must publish the forms before they can accept responses", and "If no action is taken, then new forms created using APIs after June 30, 2026, will be in an unpublished state by default and won't receive responses."

This is the single most likely way to hand a user a dead survey. The form opens, looks correct, and silently collects nothing. Do not skip this step and do not treat it as optional polish.

```bash
# Inspect the exact publishSettings shape first
gws schema forms.forms.setPublishSettings

gws forms forms setPublishSettings \
  --params '{"formId": "<FORM_ID>"}' \
  --json '{"publishSettings": {"publishState": {"isPublished": true, "isAcceptingResponses": true}}, "updateMask": "publishState"}'
```

Then re-run `gws forms forms get` and confirm the publish state before you hand over the `responderUri`. Publish first, hand over the link second: the order is what stops you shipping a dead survey.

Two related notes:

- Legacy forms (created before the publishing model existed) do not support `publishSettings` at all, because they have no such field. Forms you create through the API do.
- To restrict who can respond rather than sharing an open link, share the form with specific users via the Drive API's `permissions.create`. That is a separate call, not a `publishSettings` flag.

### Step 7: Guide Sheets linking (UI step, not API)

The Google Forms API does not currently expose a method to connect a form's responses to a specific Google Sheet. This must be done once in the UI:

1. Open the form in the Forms editor (the URL comes back from `gws forms forms get`; copy the `formId` into the browser-side Forms UI, or open it from Drive).
2. Click the **Responses** tab.
3. Click the green Sheets icon → **Create a new spreadsheet** (or select an existing one).

Tell the user this is a one-time click, and that after it's done, every new response will land in the linked Sheet automatically. Do not claim the skill handles this step.

If the user wants API-level response access instead, use `gws forms forms responses list --params '{"formId": "<FORM_ID>"}'` to pull responses and pipe them into `gws sheets` yourself.

### Step 8: Pick the right send time for Israeli audiences

A perfectly worded survey sent at the wrong time tanks your response rate. Before you push the form, think about *when* it will land in people's inboxes:

- **Avoid Friday afternoon and Shabbat.** Observant recipients are offline; by Sunday it's buried.
- **Avoid chag weeks entirely**, Sukkot, Pesach, Rosh Hashanah, Yom Kippur period, Shavuot, Yom HaZikaron/Yom HaAtzmaut. Response rates collapse during these weeks.
- **Best days**: Sunday (fresh inboxes), Tuesday-Wednesday (strongest B2B engagement). Thursday is acceptable but drifts softer late in the day.
- **Best hours**: 09:00-11:00 morning window, 13:00-14:00 post-lunch lull. Avoid before 08:30 or after 20:00.
- **Transactional surveys** (post-ticket CSAT, post-event feedback) should fire immediately after the interaction, not on a batch schedule, but still hold them for Sunday morning if the event ended Thursday evening.

The full decision tree and per-survey-type cadence (NPS quarterly vs monthly, CSAT per-ticket vs batched, etc.) is in `references/israeli-send-timing.md`. Consult it before committing to a cadence.

### Step 9: Share, and check consent before you send

Once Step 5 has published the form, the responder link works for anyone who has it, within the creator's Google account rules (Workspace domain restrictions still apply).

**Consent and privacy.** Keep NPS, CSAT, and CES responses anonymous by default, it both protects respondents and lifts response rates. Israeli law has required informed consent (הסכמה מדעת) for identifiable personal data since long before the recent reform. What Amendment 13 (in force 14 August 2025) changed here is mainly the **notice** you owe the respondent: who the controller is and how to reach them, what happens if they refuse, and their right to access and correct their data. So before you share the form, check whether it is *actually* anonymous, not just anonymous-looking:

- **A form with no identifying field can still be identifiable.** Emailing a personalized survey link to a customer list, or pre-filling a respondent token, re-identifies every answer even if the form asks for no name or email. Treat that flow as identifiable: tell recipients what you collect and why, give an opt-out, and don't reuse the list beyond this survey.
- **Turn off "Collect email addresses" for anonymous external surveys.** Inside a Google Workspace domain, Google Forms can auto-capture the respondent's account email, which silently breaks an "anonymous" promise. Disable it unless you actually need identity.
- **Watch small samples.** A segment question (עצמאי / שכיר / בעל עסק) plus a free-text comment on a small list (a meetup, a niche B2B audience) re-identifies people. Don't cross-tab or report segments with only a handful of responses.
- **If you do need identity** (e.g. a follow-up-contact NPS), add a leading required consent item ("אני מאשר/ת שאפשר ליצור איתי קשר בעקבות התשובות") *before* any identifying field, and never pre-tick it.

For a genuinely anonymous survey, a one-line intro ("התשובות אנונימיות" / "Responses are anonymous") is enough. For the identifiable flows above, give the fuller notice (what you collect, why, and an opt-out) rather than a single line. For forms that gather sensitive or government data, defer to `israeli-gov-form-automator`.

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
| API changes to Google Forms | https://developers.google.com/workspace/forms/api/guides/api-changes-to-google-forms | The unpublished-by-default change and the publishing flow |
| gws shared conventions | https://raw.githubusercontent.com/googleworkspace/cli/main/skills/gws-shared/SKILL.md | Command shape and the JSON form of --params |
| Hebrew survey templates (local) | `references/hebrew-survey-templates.md` | NPS, CSAT, CES, event, product discovery wording |
| Israeli send-time guide (local) | `references/israeli-send-timing.md` | Day/hour guidance, chag weeks to avoid, cadence rules |
| Export to non-Google platforms (local) | `references/export-to-other-platforms.md` | How to paste the Hebrew templates into Typeform, SurveyMonkey, Tally, Microsoft Forms, email/Slack |

## Bundled Resources

### Scripts
- `scripts/build_batchupdate_payload.py`, take a template name (`nps`, `csat`, `ces`, `event-feedback`, `product-discovery`, `market-research`) and emit a ready-to-pipe JSON payload for `gws forms forms batchUpdate --json`.

  ```bash
  python3 scripts/build_batchupdate_payload.py --template nps --intro anonymous
  python3 scripts/build_batchupdate_payload.py --template product-discovery --topic 'ניהול הוצאות בעסק קטן'
  python3 scripts/build_batchupdate_payload.py --template event-feedback --sessions 'פתיחה,הרצאת אורח,פאנל'
  python3 scripts/build_batchupdate_payload.py --template ces --task 'את ההרשמה'
  ```

  `--topic` and `--sessions` are **required** for their templates and the script exits non-zero without them. That is deliberate: those two templates have a slot in the respondent-facing question text, and a generic filler ("the problem we are researching", "the first part") produces a question nobody can answer meaningfully. `--task` is optional but naming the task makes CES usable. `--intro anonymous|identified` sets the form description, and `identified` also prepends the required consent item at index 0.

### References
- `references/hebrew-survey-templates.md`, every template's question list in natural Israeli Hebrew, with scale labels, question types, and notes on when each template is appropriate.
- `references/gws-forms-cheatsheet.md`, the exact gws forms methods, command structure, and discovery commands, mirrored from the upstream `gws-forms` skill so you can work offline.
- `references/israeli-send-timing.md`, when to send surveys to Israeli audiences (day of week, time of day, chag weeks to avoid, per-survey-type cadence rules).
- `references/export-to-other-platforms.md`, how to use the same Hebrew templates and timing rules with Typeform, SurveyMonkey, Tally, Microsoft Forms, or plain email/Slack when Google Forms is not the right tool.

## Gotchas

These are the mistakes an agent will most likely make on first try:

1. **Trying to pass items at `create` time.** The `create` method only copies `info.title` and `info.documentTitle`. Everything else (description, items, settings) is disallowed. Upstream says only that these fields are disallowed, not whether they are dropped or rejected, so do not assume either: read the response rather than branching on an error that may never arrive, and confirm the created form is empty before you `batchUpdate` into it.
2. **Calling `forms.update` instead of `forms.batchUpdate`.** Google Forms API v1 does NOT have a `forms.update` method. The only methods on the forms resource are `create`, `get`, `batchUpdate`, and `setPublishSettings`. If you see `update` in older docs or blog posts, substitute `batchUpdate`.
3. **Assuming the API links responses to a Google Sheet.** It doesn't. The "Link to Sheets" button is UI-only. Tell the user to do it once by hand, or poll `forms.responses.list` and write to a Sheet yourself via `gws sheets`.
4. **Translating English NPS phrasing literally.** "How likely are you to recommend us to a friend or colleague?" translated word-for-word sounds stiff and passive in Hebrew. Use the wording in `references/hebrew-survey-templates.md`, it was written in Hebrew first, not translated. This is the main reason bad surveys get bad response rates in Israel.
5. **Forgetting `location.index` in a `createItem` request.** Even for a single-question insert, `location.index` is required. Start at `0` and increment.
6. **Handing over the `responderUri` without publishing.** Since 30 June 2026 an API-created form starts unpublished and accepts no responses. The link resolves, the form renders, and every submission is silently impossible. Always run `setPublishSettings` (Step 6) before you give the user the link.
7. **Writing `--params formId=<ID>`.** The `--params` flag takes a JSON object, not `key=value`: `--params '{"formId": "<ID>"}'`. The CLI parses it strictly and rejects anything else.
8. **Dropping the resource token.** The command is `gws forms forms create`, not `gws forms create`. The pattern is `gws <service> <resource> <method>`, and here both the service and the resource are called `forms`. The same doubling shows up in `gws schema forms.forms.batchUpdate`, which the skill has always had right.
9. **Using Hebrew in `documentTitle`.** `documentTitle` is the Drive filename. Some Drive search flows handle Hebrew filenames awkwardly, keep `documentTitle` in ASCII, put the Hebrew version in `info.title` (the user-facing form title).

## Examples

### Example 1: Quick NPS for an Israeli SaaS
User says: "אני צריך להפיץ NPS ללקוחות שלי, אפשר לבנות לי סקר?"

Actions:
1. Pick the `nps` template.
2. `gws forms forms create` with title "סקר NPS - <company>".
3. `gws forms forms batchUpdate` with the 2-question NPS payload from `references/hebrew-survey-templates.md`.
4. `gws forms forms setPublishSettings` to publish (mandatory), then `gws forms forms get` → return the `responderUri`.
5. Tell the user how to link to Sheets in one click if they want responses in a spreadsheet.

### Example 2: Post-event feedback for a meetup
User says: "Build a post-event survey in Hebrew for yesterday's Tel Aviv meetup, 5 questions max, include one about whether they'd come again."

Actions:
1. Pick the `event-feedback` template.
2. Trim it to 5 questions, keep "האם תחזרו למפגש הבא?" as the last question.
3. `create` + `batchUpdate` + `setPublishSettings`.
4. Return the share link.

## Troubleshooting

### Error: `gws: command not found`
Cause: Google Workspace CLI is not installed on PATH.
Solution: Install from https://github.com/googleworkspace/cli (download the pre-built binary for your OS, or use a package manager such as npm, Homebrew, or cargo, see the repo's install section), then re-authenticate. Do not attempt to substitute another CLI or `curl` the REST API directly unless the user explicitly asks.

### Error: `INVALID_ARGUMENT` on `gws forms forms create` when passing items
Cause: `create` rejects everything except `info.title` and `info.documentTitle`.
Solution: Remove `items`, `description`, and `settings` from the create payload. Add them afterwards via `batchUpdate`.

### Error: `CreateItemRequest.location.index is required`
Cause: The createItem request was missing `location` or `location.index`.
Solution: Always include `"location": { "index": <number> }` even for a single-item insert.

### Error: `forms.update not found`
Cause: Calling a method that doesn't exist in the Google Forms API v1.
Solution: Use `forms.batchUpdate` with an `updateItem` request inside the `requests` array, not `forms.update`.

### Error: an auth / permission failure on the first `create`
Cause: `gws` is installed but not authenticated, or is authenticated without the Forms and Drive scopes.
Solution: re-run the gws auth flow and grant Forms and Drive access, then re-check with `gws drive files list --params '{"pageSize": 1}'` before retrying Step 2.

### The form link works but no responses ever arrive
Cause: the form was created through the API after 30 June 2026 and was never published, so it is not accepting responses.
Solution: run `gws forms forms setPublishSettings` (Step 6), then confirm with `gws forms forms get` before re-sharing the link.

### Error: `Invalid --params JSON`
Cause: `--params` was given `key=value` instead of a JSON object.
Solution: `--params '{"formId": "<ID>"}'`. Wrap in single quotes so the shell leaves the inner double quotes alone.

### Hebrew text appears left-to-right in the created form
Cause: Very rarely, a title that starts with an ASCII character will direct the paragraph LTR even though the body is Hebrew.
Solution: Put Hebrew first in `title` (no leading punctuation or number). Google Forms infers direction from the first strong character.
