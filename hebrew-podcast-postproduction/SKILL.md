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
| Whisper JSON (local `openai-whisper`, or the API with `whisper-1` + `verbose_json`) | `language`, `segments[]` with `start`, `end`, `text` |
| ElevenLabs Scribe JSON | `language_code` and `words[]`, each with `text`, `start`, `end`, `type`. Scribe returns **no** `segments[]` array. |
| SRT file + optional audio file path | timestamped cues, HH:MM:SS,mmm format |

Two input-shape traps that break the workflow before it starts:

- **Scribe is word-level only.** `scripts/score_segments.py` accepts it and groups the words into pseudo-segments on `type: "spacing"` gaps, but any code that reaches for `transcript["segments"]` or `transcript["language"]` on Scribe output raises `KeyError`. The fields are `words` and `language_code`.
- **`gpt-4o-transcribe` / `gpt-4o-mini-transcribe` return no timestamps at all.** Those models only support `response_format=json`. For a transcript this skill can use, run local `openai-whisper`, call the API with `whisper-1` + `response_format=verbose_json`, or use Scribe.

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

Confirm the transcript is Hebrew (or majority Hebrew with English loanwords). If the input is a Whisper JSON, check the `language` field; if it is Scribe JSON, check `language_code`. For SRT input, sample 10 cues and detect Hebrew Unicode block (U+0590 to U+05FF).

If the transcript contains nikud (vowel points U+05B0-U+05BC, U+05BF, U+05C1-U+05C2), strip it for show notes and chapter titles. Nikud survives in the SRT files for subtitle readability but breaks Spotify chapter title rendering.

#### Step A2: Extract chapter boundaries

Chapter boundary detection uses topic shifts, not fixed intervals. Look for:

1. **Explicit markers** - host phrases like "בואו נעבור ל..." / "הנושא הבא" / "אוקיי, אז..." often mark transitions
2. **Speaker turn changes** (if the transcript has speaker labels) - a new guest or segment host usually starts a chapter
3. **Long pauses** - gaps greater than 3 seconds in the transcript (from `segments[n].end` to `segments[n+1].start`) often indicate cuts
4. **Topical drift** - group consecutive segments by semantic similarity; each cluster is a chapter

Target 5-12 chapters for a 30-60 minute episode. Enforce these **Spotify hard rules** (they will otherwise refuse to parse):

| Rule | Value | Enforced? |
|------|-------|-----------|
| Minimum chapters | 3 | Hard requirement |
| First chapter start time | `00:00` or `00:00:00` | Hard requirement |
| Minimum gap between chapters | 30 seconds | Hard requirement |
| Chapter order | Chronological | Hard requirement |
| Title content | Plain text, no emojis, no HTML | Hard requirement |
| Index prefixes in titles | Removed by Spotify. `1 - Introduction` is reformatted. | Silently rewritten |
| Title length | Spotify's wording is "aim for chapter titles under 40 characters" | **Recommendation, not a maximum** |
| Timestamp format | `(MM:SS)`, `MM:SS`, `(HH:MM:SS)` and `HH:MM:SS` all accepted, one chapter per line | Hard requirement |

The 40-character figure matters more for Hebrew than for English, because Hebrew carries fewer ideas per character in a chapter title. Treat it as a readability target: `generate_bundle.py` warns on it and errors only on the rules Spotify actually enforces. Do not drop a clear Hebrew title to hit 40 characters exactly.

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
  -vf "subtitles=clips/clip-01.srt:force_style='FontName=Heebo,FontSize=22,PrimaryColour=&H00FFFFFF,BorderStyle=3,Outline=2,Shadow=0,MarginV=40':shaping=complex" \
  -c:a aac -b:a 192k -c:v libx264 -preset fast -crf 20 \
  clips/clip-01.mp4
```

The `:shaping=complex` at the end of the filter string is not optional for Hebrew; see below.

The `subtitles` filter passes the SRT through libass, which needs **FriBidi** (bidirectional resolution) and **HarfBuzz** (complex shaping) to lay out Hebrew. Those two are dependencies of **libass itself**, resolved when libass is built, so they do NOT appear in FFmpeg's own configuration line. Verify the FFmpeg side like this:

```bash
ffmpeg -filters | grep ' subtitles '   # no output = this build has no libass at all
ffmpeg -version | grep -o -- '--enable-libass'
```

**Do not grep `ffmpeg -version` for `fribidi` or `harfbuzz` as a Hebrew-readiness test.** `--enable-libfribidi` and `--enable-libharfbuzz` are FFmpeg's own build flags for the **drawtext** filter, not for libass: FFmpeg's `configure` describes them as "improves drawtext filter" and "needed for drawtext filter". A perfectly working Hebrew build shows neither. The homebrew-ffmpeg tap recommended below does not pass `--enable-libfribidi` at all, and still renders Hebrew correctly, because its libass dependency pulls in fribidi and harfbuzz. Testing for those two strings produces a false "broken build" verdict on a build that is fine.

To check the libass side instead:

```bash
brew info libass          # macOS: expect fribidi and harfbuzz in Dependencies
pkg-config --modversion libass
```

**For Hebrew, always force `shaping=complex`.** libass's default shaper (`auto`) is not enough for Hebrew: FFmpeg documents the `complex` mode as "Required for correct rendering of complex scripts such as Arabic, **Hebrew**, Devanagari and Thai. Requires libass to be built with HarfBuzz." This is the single most common cause of Hebrew that comes out mis-ordered on a build whose libass *does* link FriBidi.

The option was exposed on the `subtitles` filter on 2026-06-23. On a build that has it you keep styling and shaping together, which is what you want:

```bash
ffmpeg -ss 00:12:34 -to 00:13:45 -i episode-NN.mp4 \
  -vf "subtitles=clips/clip-01.srt:force_style='FontName=Heebo,FontSize=22,PrimaryColour=&H00FFFFFF,BorderStyle=3,Outline=2,Shadow=0,MarginV=40':shaping=complex" \
  -c:a aac -b:a 192k -c:v libx264 -preset fast -crf 20 \
  clips/clip-01.mp4
```

Check your build before relying on it, since a build predating that commit rejects the option:

```bash
ffmpeg -hide_banner -h filter=subtitles | grep shaping
```

If it is absent, fall back to the `ass` filter, which has always had the option, and **set the style inside the file**: `force_style` is a `subtitles`-filter option that the `ass` filter does not accept, so a naive switch silently drops Heebo and every other style setting and you get the default Arial (and, with no Hebrew-covering Arial, tofu boxes).

```bash
ffmpeg -i clips/clip-01.srt clips/clip-01.ass
# then edit the [V4+ Styles] "Style:" line in clip-01.ass to set Heebo, size 22,
# Outline 2, MarginV 40 before burning in:
ffmpeg -ss 00:12:34 -to 00:13:45 -i episode-NN.mp4 \
  -vf "ass=clips/clip-01.ass:shaping=complex" \
  -c:a aac -b:a 192k -c:v libx264 -preset fast -crf 20 \
  clips/clip-01.mp4
```

On macOS, the default `brew install ffmpeg` formula does NOT include libass / FriBidi / HarfBuzz, so subtitle burn-in fails silently or produces mirrored Hebrew. The cleanest fix that puts a working `ffmpeg` on your PATH is the homebrew-ffmpeg tap, which enables libass (with FriBidi + HarfBuzz) by default: `brew tap homebrew-ffmpeg/ffmpeg && brew install homebrew-ffmpeg/ffmpeg/ffmpeg` (do NOT append `--with-libass`, that option no longer exists in Homebrew and will error out; if the core `ffmpeg` is already installed, run `brew unlink ffmpeg` first so the tap build links). The homebrew-core `ffmpeg-full` formula also bundles libass + HarfBuzz, but it is **keg-only** (Homebrew does not symlink it onto PATH), so after `brew install ffmpeg-full` the bare `ffmpeg` command still points at the non-libass build, you must call it by full path, e.g. `"$(brew --prefix ffmpeg-full)/bin/ffmpeg"`, or prepend that `bin` dir to PATH. On Debian/Ubuntu the distro `ffmpeg` package is built against libass and the distro `libass` links fribidi and harfbuzz, but confirm on your own release rather than assuming. After install, verify with `ffmpeg -filters | grep ' subtitles '` (empty output means libass is still missing). Do not expect `fribidi` or `harfbuzz` in `ffmpeg -version`; see the note above on why their absence is not a fault.

For `FontName`, use a Hebrew-capable font that fontconfig can resolve. **Heebo**, **Rubik**, **Assistant**, and **Open Sans Hebrew** are Google Fonts options that cover the full Hebrew + Latin range. Install them system-wide before running FFmpeg, otherwise fontconfig falls back to a default that may not contain Hebrew glyphs. For multi-word family names like `Open Sans Hebrew`, the `FontName=` value must match the exact fontconfig family string, check it with `fc-list | grep -i hebrew` first, otherwise libass silently falls back to a non-Hebrew face and renders boxes.

#### Step B3.5: Normalise loudness before shipping any clip

A clip cut straight out of an episode inherits whatever level the episode was mastered at, so a set of clips from different episodes plays back at visibly different volumes. Apple publishes an explicit target: audio should be "preconditioned so the overall loudness remains around -16 dB LKFS, with a +/- 1 dB tolerance, and that the true-peak value doesn't exceed -1 dB FS", measured per ITU-R BS.1770-5. Mastering to Apple's published -16 LKFS target is the safe default: playback normalisation on the major services is applied on their side, so an episode delivered near this target needs no per-platform variant.

Two-pass `loudnorm` is the accurate way to hit it (single-pass is a live estimate and overshoots):

```bash
# Pass 1 - measure, prints a JSON block
ffmpeg -i clips/clip-01.mp3 -af loudnorm=I=-16:TP=-1:LRA=11:print_format=json -f null -

# Pass 2 - apply, substituting the five measured_* values from pass 1
ffmpeg -i clips/clip-01.mp3 \
  -af loudnorm=I=-16:TP=-1:LRA=11:measured_I=..:measured_TP=..:measured_LRA=..:measured_thresh=..:offset=..:linear=true \
  -ar 48000 -b:a 192k clips/clip-01-norm.mp3
```

Normalise the episode master too, before cutting. Apple's own minimums for the delivered file are 44.1 kHz at 64 kbps for stereo MP3, with 128-256 kbps at 44.1/48 kHz recommended; the `-c copy` audio path in Step B3 preserves whatever the source already is, so a low-bitrate master stays low-bitrate in every clip.

#### Step B4: Generate social captions

For each clip, produce 4 platform-specific captions. Respect these verified 2026 character limits:

| Platform | Documented Limit | Practical Target | Notes |
|----------|-----------------|------------------|-------|
| Instagram Reels | 2,200 | 100-150 | Meta also caps a media caption at 30 hashtags and 20 @-mentions. Lead with the hook. |
| TikTok | 2,200 (UTF-16 runes) | 150-300 | This is the only figure TikTok publishes, in the Content Posting API. Its help center documents no caption limit. Hebrew letters count as one rune each; emoji count as two. |
| X (free tier) | 280 | 240-260 (leave room for a quote-post) | Long posts are Premium-only; X does not publish the Premium ceiling on an X-owned page, so do not plan around a specific number. One hashtag max. |
| LinkedIn (post) | 3,000 | 150-300 | Above 3,000, LinkedIn directs you to write an Article instead. First ~3 lines are the truncation point. |

The older "TikTok allows 4,000" figure that circulates widely is not stated on any TikTok-owned page. Write to 2,200 and the caption is safe on every surface.

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

## Examples

### Example 1: 35-minute solo interview, Whisper JSON input

Input: `episode-12.json` (Whisper output, Hebrew, 2,108 segments) + `episode-12.mp3`.

Score the transcript, then hand the chosen chapters and clips to the bundler (`generate_bundle.py` emits files; it does not pick clips or write captions for you):

```bash
python3 scripts/score_segments.py episode-12.json --top 4 --min-gap 60
# author chapters_input.json + clips_input.json from the ranked output, then:
python3 scripts/generate_bundle.py \
  --episode 12 \
  --audio episode-12.mp3 \
  --chapters chapters_input.json \
  --clips clips_input.json \
  --output episode-12/ \
  --mode audio
```

Output bundle:

```
episode-12/
├── show-notes.md            (RTL Hebrew + EN summary, 7 chapters)
├── chapters/
│   ├── spotify-chapters.txt  (7 lines, chronological, first at 00:00, gaps >= 60s)
│   └── chapters.json         (Podcasting 2.0 v1.2.0)
├── clips/
│   ├── clip-01.srt           (00:08:42 - 00:09:48 in original, rebased to 00:00)
│   ├── clip-01.ffmpeg.sh     (mode 2: video burn-in command)
│   ├── clip-02.{srt,ffmpeg.sh}
│   ├── clip-03.{srt,ffmpeg.sh}
│   └── clip-04.{srt,ffmpeg.sh}  (4 clips, 60-75s each, >= 60s gap)
└── social/
    ├── clip-01-{instagram,tiktok,x,linkedin}.txt   (4 platforms x 4 clips = 16 caption files)
    └── ...
```

A 7-chapter, 4-clip bundle is the median for a 30-45 minute solo interview. Note that `show-notes.md` is shown here for completeness of the bundle layout but is **not** written by `generate_bundle.py`: the script emits `chapters/`, `clips/` and `social/`, and the show notes are authored by the agent per Step A4.

### Example 2: 60-minute panel with 3 speakers, SRT input

Input: `episode-23.srt` (timestamped cues only, no speaker labels) + `episode-23.mp4` (filmed for video repurposing).

Run the same two steps, passing the video file as `--audio` (the flag names the source media, whichever track type it carries) and selecting video mode:

```bash
python3 scripts/generate_bundle.py \
  --episode 23 \
  --audio episode-23.mp4 \
  --chapters chapters_input.json \
  --clips clips_input.json \
  --output episode-23/ \
  --mode video
```

Output bundle includes 9 chapters (panel format triggers more topic shifts), 5 clips, and the `clips/clip-NN.ffmpeg.sh` files use mode 2 (video burn-in) because `--mode video` was passed. Each clip captures one speaker's standout moment, with the scoring function favoring segments where the standalone-comprehensibility signal is high (the script penalizes clips that open with "and then he said" or other antecedent-dependent phrasing).

Show notes will tag each chapter with the speaker if speaker labels are present. Without speaker labels, chapters are titled by topic. The Hebrew show-notes Quotes section pulls the top 3 emotional-peak segments by score, which for a panel often surfaces the most-shared exchange of the episode.

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
| Spotify chapter rules | https://support.spotify.com/us/creators/article/episode-chapters/ | Timestamp format, minimum chapter count, title length limit |
| Podcasting 2.0 Chapters JSON | https://podcasting2.org/docs/podcast-namespace/tags/chapters | Chapters JSON schema, RSS tag format |
| Apple Podcasts audio requirements | https://podcasters.apple.com/support/893-audio-requirements | Accepted formats, ID3 tag rules |
| FFmpeg subtitles filter docs | https://ffmpeg.org/ffmpeg-filters.html#subtitles-1 | libass options, force_style syntax |
| libass RTL support notes | https://github.com/libass/libass | FriBidi + HarfBuzz requirements for Hebrew/Arabic |
| TikTok Content Posting API | https://developers.tiktok.com/doc/content-posting-api-reference-direct-post/ | The only caption length TikTok publishes (`title` field) |

## Gotchas

1. **Spotify rejects chapters silently.** If any enforced Spotify rule is violated (first chapter not at 00:00, fewer than 3 chapters, less than 30s gap, out-of-order chapters, HTML or emojis inside titles), Spotify does not show an error - it just refuses to parse any chapters for that episode. Validate before submitting. Agents often generate 6-second gap chapters from rapid topic shifts and wonder why nothing renders.

2. **ID3 chapters and Chapters JSON are not equivalent.** Spotify prefers description-based timestamps. Apple prefers ID3v2.3 embedded chapters or Chapters JSON via RSS. There is no one format that works everywhere - agents that pick only one will lose coverage on half the player ecosystem.

3. **FFmpeg `-c copy` only cuts at keyframes.** For audio-only MP3 clips this is usually fine. For video clips, it produces clips that start up to 2 seconds late (until the next keyframe). If frame-accurate cuts matter, re-encode with `libx264 -crf 20`. Agents frequently ship `-c copy` commands and get complaints about "the clip starts in the middle of a word."

4. **Hebrew subtitle burn-in looks correct in VLC but wrong in FFmpeg output.** VLC renders SRTs at playback time using its own libass, so preview is not a truth signal. The burn-in is the truth. Check the output file, never the preview. If the burned-in Hebrew is wrong, work the two causes in order: force `shaping=complex` via the `ass` filter (by far the more common cause), and only then check that libass itself links FriBidi with `brew info libass`. Do NOT diagnose this with `ffmpeg -version | grep fribidi`: that string is absent from working Hebrew builds, because `--enable-libfribidi` configures the drawtext filter, not libass.

5. **Apple Podcasts transcripts do not support Hebrew yet.** Apple ingests `<podcast:transcript>` (VTT/SRT), but the supported-language list (en, da, nl, fi, fr, de, it, no, pt, es, sv) excludes Hebrew. The transcript file you produce can still be hosted in your RSS feed via `<podcast:transcript>`, and other Podcasting 2.0 players (Fountain, Podverse, Castamatic) will render it; Apple just will not. Spotify auto-generates English-only transcripts; for Hebrew shows, your hosted SRT is the only option.

6. **Nikud destroys Spotify chapter titles.** Points (kametz, patach, etc.) are separate Unicode codepoints, so a pointed title burns through the 40-character readability target for no visible gain and is harder to scan at chapter-list size. Strip nikud from chapter titles; keep it only in SRT files if reading comprehension matters for the target audience.

## Troubleshooting

**"My Spotify episode description has timestamps but no chapters appear in the player."**
Check: (1) first chapter is `(00:00)`, (2) minimum 3 chapters, (3) each chapter is at least 30 seconds after the previous, (4) chapters are in chronological order, (5) no HTML or emojis inside chapter titles. Title length is not a rejection cause: Spotify only advises staying under 40 characters. If all are correct, Spotify says description updates take "a few hours" to reflect across listening platforms - wait before republishing rather than re-saving repeatedly.

**"FFmpeg burn-in produces Hebrew text that is visually reversed."**
libass was built without FriBidi. Rebuilding **FFmpeg** will not fix this and `--enable-libfribidi` is the wrong lever (it belongs to the drawtext filter). Reinstall the libass dependency chain instead: on macOS `brew reinstall fribidi harfbuzz libass` then reinstall FFmpeg from the homebrew-ffmpeg tap; on Debian/Ubuntu the packaged `libass9` already links both. Confirm with `brew info libass` (or `ldd $(pkg-config --variable=libdir libass)/libass.so`) that fribidi is in the dependency list. In practice every mainstream libass package links FriBidi, so if Hebrew is scrambled the cause is far more likely the shaping default, see the next entry.

**"Hebrew burn-in is still scrambled and libass does link FriBidi."**
This is the common case, and it is a shaping problem, not a bidi one. Add `:shaping=complex` to the `subtitles` filter (or, on a build that lacks it there, convert to ASS and use `ass=clip.ass:shaping=complex`, styling the file's `[V4+ Styles]` line since `force_style` does not exist on the `ass` filter). If it persists, continue below.

**"Hebrew is still mis-ordered after forcing `shaping=complex`."**
On macOS, libass + SRT can still mis-order mixed Hebrew/Latin/digit lines even with FriBidi compiled in. Pre-shape each cue with `python-bidi` (`from bidi import get_display` on 0.6.x, or the compatible `from bidi.algorithm import get_display`, applied to the cue text before burn-in), or convert the SRT to `.ass` with the runs pre-ordered. The `video-use-best-practices` skill documents the full python-bidi pre-shape recipe for this exact macOS failure.

**"Hebrew characters render as boxes in the burned-in subtitles."**
Fontconfig cannot find a font with Hebrew glyphs. Install a Hebrew font system-wide: `brew install --cask font-heebo` on macOS, or download Heebo/Rubik from Google Fonts and copy to `~/.fonts/` on Linux, then run `fc-cache -fv`.

**"The Chapters JSON file validates but Apple Podcasts does not show chapters."**
The `<podcast:chapters>` tag must be inside each `<item>` (episode) in the RSS feed, not at the channel level. The `url` attribute must be publicly accessible over HTTPS. Apple re-ingests feeds on its own schedule and publishes no guaranteed interval, so allow for a delay of hours before concluding the tag is wrong.

**"Agent picked 5 clips but 3 of them overlap or contain pronoun references without context."**
Increase the standalone-comprehensibility weight in the scoring function (Step B1), and add a minimum 60-second gap enforcement between selected clips. Pronouns without antecedents ("he said this") fail the comprehensibility check and should be rejected.




