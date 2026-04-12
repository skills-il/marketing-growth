---
name: hebrew-podcast-postproduction
description: "Generate complete post-production packages for Hebrew podcasts including RTL show notes with chapter markers, timestamped clip extractions, and platform-specific social captions. Use when a Hebrew podcast episode needs show notes, Spotify/Apple chapter markers, shareable 30-90 second clips, FFmpeg extraction commands, or Hebrew social captions for Instagram Reels, TikTok, X, and LinkedIn from a transcript or audio file. Prevents stitching together 4-5 separate tools and avoids RTL, nikud, and Hebrew subtitle burn-in bugs that generic tools (Kapwing, Maestra, Descript) mishandle. Do NOT use for standalone audio transcription (use video-subtitles), podcast RSS feed generation, audio mixing/mastering, or English-only podcasts."
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---

# Hebrew Podcast Post-Production Kit

## Problem

Hebrew podcasters ship every episode through 4-5 disconnected tools: one for transcription, one for show notes, another for clip-hunting, another for social captions, plus FFmpeg for the actual cutting. Generic tools (Kapwing, Maestra, Descript, Podsqueeze) mishandle RTL text, drop nikud, and produce broken subtitle burn-ins because they do not run FriBidi shaping for Hebrew. This skill consolidates the entire post-production workflow into one coherent package so the agent outputs show notes, chapters, clips, and captions from a single transcript input.

## Instructions

The workflow takes one of two inputs and produces one markdown bundle:

| Input | Required Fields |
|-------|-----------------|
| Whisper / ElevenLabs Scribe JSON | `segments[]` with `start`, `end`, `text` (word-level timestamps preferred) |
| SRT file + optional audio file path | timestamped cues, HH:MM:SS,mmm format |

Output bundle structure:

```
episode-{NN}/
├── show-notes.md            # RTL Hebrew + English show notes
├── chapters/
│   ├── spotify-chapters.txt # Copy-paste into Spotify episode description
│   └── chapters.json        # Podcasting 2.0 Chapters JSON for Apple / RSS feed
├── clips/
│   ├── clip-01.srt          # RTL-aware SRT for burn-in
│   ├── clip-01.ffmpeg.sh    # Extraction + burn-in command
│   └── ...                  # 3-5 clips total
└── social/
    ├── clip-01-instagram.txt
    ├── clip-01-tiktok.txt
    ├── clip-01-x.txt
    └── clip-01-linkedin.txt
```

### Section A: Show Notes Generation

#### Step A1: Parse transcript and detect language

Confirm the transcript is Hebrew (or majority Hebrew with English loanwords). If the input is a Whisper JSON, check `language` field. For SRT input, sample 10 cues and detect Hebrew Unicode block (U+0590 to U+05FF).

If the transcript contains nikud (vowel points U+05B0-U+05BC, U+05BF, U+05C1-U+05C2), strip it for show notes and chapter titles. Nikud survives in the SRT files for subtitle readability but breaks Spotify chapter title rendering.

#### Step A2: Extract chapter boundaries

Chapter boundary detection uses topic shifts, not fixed intervals. Look for:

1. **Explicit markers** - host phrases like "בואו נעבור ל..." / "הנושא הבא" / "אוקיי, אז..." often mark transitions
2. **Speaker turn changes** (if the transcript has speaker labels) - a new guest or segment host usually starts a chapter
3. **Long pauses** - gaps greater than 3 seconds in the transcript (from `segments[n].end` to `segments[n+1].start`) often indicate cuts
4. **Topical drift** - group consecutive segments by semantic similarity; each cluster is a chapter

Target 5-12 chapters for a 30-60 minute episode. Enforce these **Spotify hard rules** (they will otherwise refuse to parse):

| Rule | Value |
|------|-------|
| Minimum chapters | 3 |
| First chapter start time | `00:00` or `00:00:00` |
| Minimum gap between chapters | 30 seconds |
| Title maximum length | 40 characters (plain text, no emojis) |
| Timestamp format | `(HH:MM:SS) Title` or `HH:MM:SS Title` on new lines |

Chapter titles should be **descriptive in Hebrew** (what the chapter is about, not generic like "שיחה"). Example good titles:

```
(00:00) פתיחה והיכרות עם האורח
(02:30) איך התחלת לעבוד בהייטק
(08:45) המעבר לניהול מוצר
(15:20) טעויות שעלו לי ביוקר
(24:00) מה צופן העתיד לתחום
```

Output `chapters/spotify-chapters.txt` with one chapter per line, ready to paste into the Spotify episode description.

#### Step A3: Generate Chapters JSON for Apple / RSS feed

Spotify parses chapters from the episode description. Apple Podcasts and Podcasting 2.0 players use either ID3v2.3 embedded chapter frames or a `chapters.json` file referenced via the `<podcast:chapters>` RSS namespace tag. The `chapters.json` approach is preferred because it does not require re-encoding the MP3 and chapters can be edited after publishing.

Output `chapters/chapters.json` following the Podcasting 2.0 Chapters JSON spec:

```json
{
  "version": "1.2.0",
  "chapters": [
    { "startTime": 0, "title": "פתיחה והיכרות עם האורח" },
    { "startTime": 150, "title": "איך התחלת לעבוד בהייטק" },
    { "startTime": 525, "title": "המעבר לניהול מוצר" }
  ]
}
```

`startTime` is in seconds (integer or float), not HH:MM:SS. Include the RSS tag snippet in the show notes:

```xml
<podcast:chapters url="https://example.com/episodes/NN/chapters.json"
                  type="application/json+chapters" />
```

#### Step A4: Write the show notes markdown

Produce `show-notes.md` with both Hebrew (RTL) and English sections. Use this structure:

```markdown
# פרק NN - {כותרת הפרק}

<div dir="rtl">

## סיכום הפרק
{2-3 שורות בעברית - מה הפרק, מי האורח, הנושא המרכזי}

## אורחים
- **{שם}** - {תפקיד, חברה, קישור}

## ציטוטים מהפרק
> "{ציטוט בולט 1}"
> "{ציטוט בולט 2}"

## פרקים
(00:00) פתיחה והיכרות עם האורח
(02:30) איך התחלת לעבוד בהייטק
...

## קישורים שהוזכרו בפרק
- {רשימה של URLs, ספרים, אנשים שהוזכרו}

</div>

---

## Episode Summary (English)
{Same summary, translated}

## Guests
- **{Name}** - {title, company, link}

## Key Quotes
> "{Highlight 1}"
> "{Highlight 2}"

## Mentioned In This Episode
- {URLs, books, people mentioned}
```

The `<div dir="rtl">` wrapper is required for Hebrew content on most podcast hosts (Transistor, Buzzsprout, Simplecast) because their episode description editors default to LTR. Without it, punctuation marks (periods, commas) render on the wrong side of lines.

### Section B: Clips & Social Captions

#### Step B1: Score segments for shareability

Rank transcript segments by a composite shareability score. For each 30-90 second window, compute:

| Signal | Weight | How to Measure |
|--------|--------|----------------|
| Quotable density | 40% | Ratio of declarative statements to filler words; presence of first-person insights |
| Emotional peaks | 25% | Exclamations, laughter markers, raised-voice indicators, strong positive/negative sentiment |
| Standalone comprehensibility | 20% | Can this segment be understood without preceding context? Does it reference "this" / "that" without an antecedent? |
| Topic hook | 15% | Does it open with a question, surprising claim, or specific number? |

Select the **top 3-5 windows** with at least 60 seconds of separation between them. Prefer 45-75 second clips (Instagram Reels sweet spot) over the 30s floor or 90s ceiling.

#### Step B2: Generate RTL-aware SRT files

For each selected clip, emit a standalone SRT file covering exactly that window, with timestamps **rebased to zero** (the clip starts at 00:00:00,000, not at the absolute episode timestamp).

```srt
1
00:00:00,000 --> 00:00:03,200
אז בואו נדבר על הטעות הכי גדולה שעשיתי

2
00:00:03,200 --> 00:00:06,800
זה היה בגיוס הראשון של הסטארטאפ
```

Rules for Hebrew SRT content:

- Keep nikud only when it resolves genuine ambiguity (homographs). Default to unpointed text - nikud adds noise on small screens
- Break lines at natural phrase boundaries, max 42 characters per line, max 2 lines per cue
- Punctuation marks (`.` `,` `!` `?`) stay at the logical end of the sentence; libass + FriBidi handles the visual positioning at render time

#### Step B3: Generate FFmpeg extraction + burn-in commands

For each clip, emit `clips/clip-NN.ffmpeg.sh`. Use two modes depending on whether the user wants an audio-only clip (for podcast promos) or a video clip with burned-in Hebrew subtitles (for Reels/TikTok).

**Mode 1 - Audio clip, stream copy (fast):**

```bash
ffmpeg -ss 00:12:34 -to 00:13:45 -i episode-NN.mp3 \
  -c copy \
  clips/clip-01.mp3
```

`-ss` before `-i` seeks before decoding (fast but keyframe-bound). For frame-accurate cuts on compressed audio, place `-ss` after `-i` at the cost of slower processing.

**Mode 2 - Video clip with burned-in Hebrew subtitles (re-encode):**

```bash
ffmpeg -ss 00:12:34 -to 00:13:45 -i episode-NN.mp4 \
  -vf "subtitles=clips/clip-01.srt:force_style='FontName=Heebo,FontSize=22,PrimaryColour=&H00FFFFFF,BorderStyle=3,Outline=2,Shadow=0,MarginV=40'" \
  -c:a aac -c:v libx264 -preset fast -crf 20 \
  clips/clip-01.mp4
```

The `subtitles` filter passes the SRT through libass, which requires libass to be compiled with **FriBidi** (bidirectional text resolution) and **HarfBuzz** (complex text shaping). Without both, Hebrew renders as a visual mirror image of the logical string. Verify with:

```bash
ffmpeg -version 2>&1 | grep -E 'libass|fribidi|harfbuzz'
```

On macOS, `brew install ffmpeg` ships libass with both dependencies. On Debian/Ubuntu, the `ffmpeg` package in main ships with them since Ubuntu 22.04.

For `FontName`, use a Hebrew-capable font that fontconfig can resolve. **Heebo**, **Rubik**, **Assistant**, and **Open Sans Hebrew** are Google Fonts options that cover the full Hebrew + Latin range. Install them system-wide before running FFmpeg, otherwise fontconfig falls back to a default that may not contain Hebrew glyphs.

#### Step B4: Generate social captions

For each clip, produce 4 platform-specific captions. Respect these verified 2026 character limits:

| Platform | Hard Limit | Practical Target | Notes |
|----------|-----------|------------------|-------|
| Instagram Reels | 2,200 | First 125 chars visible before "more" | Lead with the hook. Line breaks are free. |
| TikTok | 4,000 | 150-300 | Hashtags help search; 3-5 is optimal. |
| X (free tier) | 280 | 240-260 (leave room for retweet) | One hashtag max, use threads for longer context. |
| LinkedIn | 3,000 | 150-300 for best engagement | First 3 lines are critical (truncation point). |

Each caption must contain:

1. **Hook line** - the most quotable phrase from the clip, without context framing
2. **One sentence of context** - who is speaking and what the episode is about
3. **Call to action** - listen to the full episode at {URL}
4. **Hashtag set** - platform-appropriate (see below)

**Israeli hashtag conventions** (verified against current Hebrew social usage):

- No underscores, no spaces - Hebrew words concatenate: `#פודקאסטישראלי` not `#פודקאסט_ישראלי`
- Mix 2-3 broad tags with 2-3 niche tags
- Broad Hebrew tags: `#פודקאסט` `#פודקאסטישראלי` `#הייטקישראלי` `#יזמותישראלית`
- For cross-border reach, pair Hebrew tags with English equivalents (TikTok search indexes both)

Example Instagram caption:

```
"זו הטעות הכי יקרה שעשיתי בסטארטאפ הראשון"

בפרק החדש {שם האורח} מספר/ת על הכישלון שלימד אותו/ה יותר מכל הצלחה.

האזינו לפרק המלא: {link}

#פודקאסטישראלי #יזמותישראלית #סטארטאפ #podcast #israelitech
```

## Bundled Resources

### References

- [`references/spotify-chapters-rules.md`](references/spotify-chapters-rules.md) - Spotify episode description chapter parsing rules
- [`references/chapters-json-schema.md`](references/chapters-json-schema.md) - Podcasting 2.0 Chapters JSON reference
- [`references/ffmpeg-hebrew-subtitles.md`](references/ffmpeg-hebrew-subtitles.md) - FFmpeg + libass + FriBidi setup for Hebrew burn-in
- [`references/social-caption-limits.md`](references/social-caption-limits.md) - Platform caption limits and Israeli hashtag conventions

### Scripts

- [`scripts/score_segments.py`](scripts/score_segments.py) - Rank transcript segments by shareability signals
- [`scripts/generate_bundle.py`](scripts/generate_bundle.py) - Build the complete output directory structure from a transcript input

## Recommended MCP Servers

No podcast or audio MCP servers are currently available in the skills-il directory. This skill operates standalone on transcript and audio files provided by the user.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Spotify chapter rules | https://support.spotify.com/us/creators/article/enabling-chapters/ | Timestamp format, minimum chapter count, title length limit |
| Podcasting 2.0 Chapters JSON | https://podcasting2.org/docs/podcast-namespace/tags/chapters | Chapters JSON schema, RSS tag format |
| Apple Podcasts audio requirements | https://podcasters.apple.com/support/893-audio-requirements | Accepted formats, ID3 tag rules |
| FFmpeg subtitles filter docs | https://ffmpeg.org/ffmpeg-filters.html#subtitles-1 | libass options, force_style syntax |
| libass RTL support notes | https://github.com/libass/libass | FriBidi + HarfBuzz requirements for Hebrew/Arabic |

## Gotchas

1. **Spotify rejects chapters silently.** If any Spotify rule is violated (first chapter not at 00:00, less than 30s gap, title over 40 chars, HTML inside titles), Spotify does not show an error - it just refuses to parse any chapters for that episode. Validate before submitting. Agents often generate 6-second gap chapters from rapid topic shifts and wonder why nothing renders.

2. **ID3 chapters and Chapters JSON are not equivalent.** Spotify prefers description-based timestamps. Apple prefers ID3v2.3 embedded chapters or Chapters JSON via RSS. There is no one format that works everywhere - agents that pick only one will lose coverage on half the player ecosystem.

3. **FFmpeg `-c copy` only cuts at keyframes.** For audio-only MP3 clips this is usually fine. For video clips, it produces clips that start up to 2 seconds late (until the next keyframe). If frame-accurate cuts matter, re-encode with `libx264 -crf 20`. Agents frequently ship `-c copy` commands and get complaints about "the clip starts in the middle of a word."

4. **Hebrew subtitle burn-in looks correct in VLC but wrong in FFmpeg output.** VLC renders SRTs at playback time using its own libass, so preview is not a truth signal. The burn-in is the truth. If libass was built without FriBidi, the burned-in text is a mirror image of the logical string - correct-looking in source files, reversed in output video. Always verify with `ffmpeg -version | grep fribidi`.

5. **Nikud destroys Spotify chapter titles.** Points (kametz, patach, etc.) count as separate Unicode codepoints against the 40-character limit, and Spotify's title parser truncates mid-codepoint, corrupting the first visible word. Strip nikud from chapter titles; keep it only in SRT files if reading comprehension matters for the target audience.

## Troubleshooting

**"My Spotify episode description has timestamps but no chapters appear in the player."**
Check: (1) first chapter is `(00:00)`, (2) minimum 3 chapters, (3) each chapter is at least 30 seconds after the previous, (4) titles are under 40 characters, (5) no HTML tags inside chapter titles. If all are correct, Spotify can take up to 4 hours to reparse a published episode - wait before republishing.

**"FFmpeg burn-in produces Hebrew text that is visually reversed."**
libass is missing FriBidi support. Rebuild FFmpeg with `--enable-libass --enable-libfribidi --enable-libharfbuzz`, or install the Homebrew / official Debian package which ships with all three.

**"Hebrew characters render as boxes in the burned-in subtitles."**
Fontconfig cannot find a font with Hebrew glyphs. Install a Hebrew font system-wide: `brew install font-heebo` on macOS, or download Heebo/Rubik from Google Fonts and copy to `~/.fonts/` on Linux, then run `fc-cache -fv`.

**"The Chapters JSON file validates but Apple Podcasts does not show chapters."**
The `<podcast:chapters>` tag must be inside each `<item>` (episode) in the RSS feed, not at the channel level. The `url` attribute must be publicly accessible over HTTPS. Apple may take up to 24 hours to re-ingest a modified RSS feed.

**"Agent picked 5 clips but 3 of them overlap or contain pronoun references without context."**
Increase the standalone-comprehensibility weight in the scoring function (Step B1), and add a minimum 60-second gap enforcement between selected clips. Pronouns without antecedents ("he said this") fail the comprehensibility check and should be rejected.



