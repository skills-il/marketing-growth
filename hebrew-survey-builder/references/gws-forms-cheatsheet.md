# gws forms cheatsheet

Mirrored from the upstream `gws-forms` skill in `github.com/googleworkspace/cli` so you can work offline. If anything here drifts from upstream, upstream is authoritative — refetch from `skills/gws-forms/SKILL.md`.

## Command format

```bash
gws forms <resource> <method> [flags]
```

## Methods on the `forms` resource

Exactly these four, plus two sub-resources:

| Method | Purpose |
|--------|---------|
| `create` | Create a new form. Only `info.title` and `info.documentTitle` are accepted — items, description, and settings are silently rejected. |
| `get` | Fetch a form's metadata, including `responderUri` (the public share URL). |
| `batchUpdate` | The ONLY way to modify a form after creation. Takes a `requests` array. |
| `setPublishSettings` | Change who can respond. Legacy forms don't support this; API-created forms do. |

Sub-resources:

- `responses` — list/get responses (`gws forms responses list`, `gws forms responses get`)
- `watches` — create/list/delete push notifications when responses come in

There is **no `forms.update`** method. If you see it in old docs or blog posts, it means `forms.batchUpdate` with an `updateItem` request.

## batchUpdate request types

Inside the `requests` array, each request is one of:

| Request type | Purpose |
|--------------|---------|
| `updateFormInfo` | Change title, description of the form itself |
| `updateSettings` | Change form-level settings (e.g. quiz mode) |
| `createItem` | Add a new question or section |
| `moveItem` | Reorder items |
| `deleteItem` | Remove a question |
| `updateItem` | Edit an existing question's content |

A `createItem` request needs exactly these fields:

```json
{
  "createItem": {
    "item":     { /* Item object */ },
    "location": { "index": 0 }
  }
}
```

Both `item` and `location` are required. `location.index` is zero-based.

## Discovery

Always inspect before sending a big payload:

```bash
# List all methods on the forms resource
gws forms --help

# Inspect the exact parameter and JSON shape for a specific method
gws schema forms.forms.batchUpdate
gws schema forms.forms.create
gws schema forms.forms.setPublishSettings
```

`gws schema` is the authoritative source for the installed version of gws — preferred over any third-party doc or this cheatsheet if they disagree.

## Common flags

| Flag | Use |
|------|-----|
| `--json '{ ... }'` | Pass the request body as JSON |
| `--params key=value` | Pass URL path/query params (e.g. `formId=XYZ`) |

## Endpoint reference

Prefer `gws` in all cases — it wraps the REST API, handles auth, and keeps command shapes in sync with Google's Discovery Service. If you need the raw REST endpoints, look them up in the Google Forms API v1 reference rather than caching them here; they evolve.

The one endpoint worth knowing by heart is the `batchUpdate` path, because it's mentioned directly in Google's docs:

`POST https://forms.googleapis.com/v1/forms/{formId}:batchUpdate`

Authentication is handled by `gws` for you — don't roll your own OAuth unless the user has a clear reason to bypass `gws`.
