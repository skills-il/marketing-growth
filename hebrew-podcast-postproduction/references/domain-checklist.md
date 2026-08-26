# Domain coverage checklist, hebrew-podcast-postproduction

Anchor for expert review. Scope: end-to-end Hebrew podcast post-production from a transcript/SRT: RTL show notes, Spotify + Apple/Podcasting-2.0 chapters, clip scoring, FFmpeg extraction + Hebrew subtitle burn-in, platform social captions.

## Must cover (core)
- Spotify chapter rules, separating enforced from advisory: enforced = min 3 chapters, first at 00:00, >=30s gap, chronological order, plain text with no emojis/HTML, index prefixes stripped. Advisory = "aim for chapter titles under 40 characters" (a Tips-section recommendation, NOT a parse requirement).
- Podcasting 2.0 Chapters JSON (version 1.2.0; `version` + `chapters` are the only required top-level properties; `startTime` in seconds is the only required per-chapter attribute, `title` is optional per spec) + <podcast:chapters> RSS tag inside each <item>.
- FFmpeg clip extraction (-ss/-to) and Hebrew subtitle burn-in via libass, which needs FriBidi + HarfBuzz **at libass build time**. Must state that `--enable-libfribidi` / `--enable-libharfbuzz` are FFmpeg's drawtext-filter flags and are NOT a valid readiness test, and that `shaping=complex`, which FFmpeg documents as required for Hebrew, must be set explicitly (available on `subtitles` since 2026-06-23 and on `ass` throughout; `force_style` is a `subtitles`-only option).
- Correct macOS install for an libass-enabled ffmpeg (homebrew-ffmpeg tap links `ffmpeg` on PATH; default brew ffmpeg lacks libass; homebrew-core ffmpeg-full also works but is keg-only, call by full path). Hebrew font install (--cask font-heebo etc.).
- RTL/nikud handling: strip nikud from chapter titles, keep where it disambiguates; <div dir="rtl"> wrapper for hosts.
- Social caption limits per platform, each traceable to a platform-owned page: IG 2200 (Meta media reference), TikTok 2200 UTF-16 runes (Content Posting API; the widely-quoted 4,000 appears on no TikTok-owned page), X 280 free tier, LinkedIn 3000 post. Plus Israeli hashtag conventions (no underscores, concatenated Hebrew).
- Clip scoring heuristic (quotable density / emotional peaks / standalone comprehensibility / topic hook).

## Should cover (advanced)
- Apple Podcasts auto-transcript languages exclude Hebrew; host your own SRT/VTT via <podcast:transcript>.
- -c copy keyframe caveat for video clips; re-encode for frame-accurate cuts.
- Transcript input shapes: Whisper `segments[]`/`language` vs ElevenLabs Scribe `words[]`/`language_code` (Scribe has no `segments[]`); gpt-4o-transcribe returns no timestamps at all.
- Loudness normalisation before release: Apple's published -16 dB LKFS +/- 1 with true peak <= -1 dB FS, two-pass `loudnorm`, and Apple's MP3 bitrate minimums.
- VLC-vs-FFmpeg burn-in truth (VLC preview is not the burned output).

## Out of scope (explicit)
- Standalone transcription (defer to video-subtitles), RSS feed generation, audio mixing/mastering, English-only podcasts (all in the skill description).

## Authoritative sources
- Spotify chapters: https://support.spotify.com/us/creators/article/episode-chapters/
- Podcasting 2.0 chapters: https://podcasting2.org/docs/podcast-namespace/tags/chapters
- FFmpeg subtitles filter: https://ffmpeg.org/ffmpeg-filters.html#subtitles-1
- libass: https://github.com/libass/libass
- Homebrew ffmpeg-full: https://formulae.brew.sh/formula/ffmpeg-full
