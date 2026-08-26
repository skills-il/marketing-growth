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

The spec requires exactly one attribute per chapter: `startTime`. Everything else, `title` included, is optional (`endTime`, `url`, `img`, `toc`). Always write a `title` anyway: a chapter with no title is useless to a listener, and Spotify's description-based chapters require one. The distinction matters when validating a third-party file, where a missing `title` is legal and must not be rejected.

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
| `chapters` | array | yes | The spec sets no minimum entry count. Spotify separately requires at least 3 chapters for its own description-based parsing. |
| `chapters[].startTime` | number | yes | Seconds from the start of the audio, integer or float |
| `chapters[].title` | string | no (optional per spec) | Plain text, UTF-8, no length limit enforced by the spec. Write one regardless. |
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

Apple Podcasts supports the older ID3v2.3 embedded chapter format. Support for Chapters JSON via the RSS namespace tag is claimed by several hosts but is not stated on an Apple-owned page, so do not rely on it as Apple's documented behaviour; the Podcasting 2.0 players (Fountain, Podverse, Castamatic) are where the JSON file is reliably rendered. If both exist (JSON via RSS and chapters embedded in the MP3), behaviour is host-dependent - prefer one method per episode to avoid duplication.

## Reference

- Podcasting 2.0 chapters spec (see Reference Links in SKILL.md)
