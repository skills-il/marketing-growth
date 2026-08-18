# Domain coverage checklist, hebrew-podcast-postproduction

Anchor for expert review. Scope: end-to-end Hebrew podcast post-production from a transcript/SRT: RTL show notes, Spotify + Apple/Podcasting-2.0 chapters, clip scoring, FFmpeg extraction + Hebrew subtitle burn-in, platform social captions.

## Must cover (core)
- Spotify chapter hard rules (min 3, first at 00:00, >=30s gap, <=40-char plain-text titles).
- Podcasting 2.0 Chapters JSON (version 1.2.0, startTime in seconds, title) + <podcast:chapters> RSS tag.
- FFmpeg clip extraction (-ss/-to) and Hebrew subtitle burn-in via libass needing FriBidi + HarfBuzz.
- Correct macOS install for an libass-enabled ffmpeg (homebrew-ffmpeg tap links `ffmpeg` on PATH; default brew ffmpeg lacks libass; homebrew-core ffmpeg-full also works but is keg-only, call by full path). Hebrew font install (--cask font-heebo etc.).
- RTL/nikud handling: strip nikud from chapter titles, keep where it disambiguates; <div dir="rtl"> wrapper for hosts.
- Social caption limits per platform (IG 2200, TikTok 4000, X 280, LinkedIn 3000) + Israeli hashtag conventions (no underscores, concatenated Hebrew).
- Clip scoring heuristic (quotable density / emotional peaks / standalone comprehensibility / topic hook).

## Should cover (advanced)
- Apple Podcasts auto-transcript languages exclude Hebrew; host your own SRT/VTT via <podcast:transcript>.
- -c copy keyframe caveat for video clips; re-encode for frame-accurate cuts.
- VLC-vs-FFmpeg burn-in truth (VLC preview is not the burned output).

## Out of scope (explicit)
- Standalone transcription (defer to video-subtitles), RSS feed generation, audio mixing/mastering, English-only podcasts (all in the skill description).

## Authoritative sources
- Spotify chapters: https://support.spotify.com/us/creators/article/episode-chapters/
- Podcasting 2.0 chapters: https://podcasting2.org/docs/podcast-namespace/tags/chapters
- FFmpeg subtitles filter: https://ffmpeg.org/ffmpeg-filters.html#subtitles-1
- libass: https://github.com/libass/libass
- Homebrew ffmpeg-full: https://formulae.brew.sh/formula/ffmpeg-full
