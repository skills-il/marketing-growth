# Podcasting 2.0 Chapters JSON

The Podcasting 2.0 `podcast:chapters` tag references an external JSON file that describes chapter boundaries, titles, optional images, and optional URLs. This format is supported by Apple Podcasts (as an alternative to ID3v2.3 embedded chapters), Buzzsprout, RSS.com, Transistor, and Podcasting 2.0 players (Fountain, Podverse, Castamatic, etc.).

## RSS tag

Place one tag per `<item>` (episode), inside the `<item>` element, at the same level as `<title>` and `<description>`:

```xml
<item>
  <title>Episode 42</title>
  <description>...</description>
  <podcast:chapters url="https://cdn.example.com/podcast/episodes/42/chapters.json"
                    type="application/json+chapters" />
</item>
```

The `url` attribute must be a publicly accessible HTTPS URL. The `type` attribute must be exactly `application/json+chapters`.

## JSON schema

Minimum required fields per chapter: `startTime` and `title`. Optional fields: `endTime`, `url`, `img`, `toc`.

```json
{
  "version": "1.2.0",
  "chapters": [
    {
      "startTime": 0,
      "title": "פתיחה"
    },
    {
      "startTime": 150,
      "title": "איך זה התחיל",
      "img": "https://cdn.example.com/ep42/chapter2.jpg"
    },
    {
      "startTime": 525,
      "endTime": 900,
      "title": "הטעות שעלתה לי ביוקר",
      "url": "https://example.com/related-article"
    }
  ]
}
```

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `version` | string | yes | `"1.2.0"` is current |
| `chapters` | array | yes | At least 2 entries |
| `chapters[].startTime` | number | yes | Seconds from the start of the audio, integer or float |
| `chapters[].title` | string | yes | Plain text, UTF-8, no length limit enforced by the spec |
| `chapters[].endTime` | number | no | Seconds, usually omitted (next chapter's startTime is the end) |
| `chapters[].url` | string | no | Link to an external resource for the chapter |
| `chapters[].img` | string | no | Image URL for the chapter (displayed in some players) |
| `chapters[].toc` | boolean | no | `false` hides from "table of contents" view but keeps jump point |

## Hosting the JSON file

The file must be:

1. Accessible over HTTPS
2. Served with `Content-Type: application/json` (most players also accept `application/json+chapters`)
3. CORS-permissive if you want web players to fetch it - add `Access-Control-Allow-Origin: *`

Common hosts: S3 + CloudFront, Cloudflare R2, Bunny CDN, or the podcast host's own asset storage if available.

## Apple Podcasts specifics

Apple Podcasts supports Chapters JSON as of 2024. It also supports the older ID3v2.3 embedded chapter format. If both exist (JSON via RSS and chapters embedded in the MP3), behaviour is host-dependent - prefer one method per episode to avoid duplication.

## Reference

- Podcasting 2.0 chapters spec (see Reference Links in SKILL.md)
