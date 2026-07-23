---
name: prompt-to-video-short
description: "Turn one topic or prompt into a finished faceless YouTube video or Short, end to end: script, TTS narration, character-locked scene images, AI-animated motion, FFmpeg assembly with burned-in captions, and title/description/tags metadata. Use when the user asks to create a faceless YouTube video or Short from a topic, wants a full script-to-video production pipeline, or mentions 'faceless channel', 'AI video pipeline', 'YouTube Short automation'. Do NOT use for live-action/human-hosted videos, audio-only podcasts, or non-YouTube platforms."
license: MIT
metadata:
  author: bardogo7
  version: 1.0.0
  category: marketing-growth
---

# Prompt to Video & Short

## Purpose

Produce a complete faceless YouTube video (long-form or Short) from a single topic/prompt,
using an animated character and AI-generated visuals instead of a real on-camera host.
Covers the full chain: script -> narration -> scene images -> motion -> assembly -> captions
-> metadata -> delivery/upload.

This skill is provider-agnostic. It assumes access to *some* model in each category (a text
model, a TTS model, an image model, a video/motion model, FFmpeg, and a local
speech-to-text model for captions) but does not hardcode any single vendor.

## When to Use

- User gives one topic/idea and wants a ready-to-upload video or Short out the other end
- Building or operating a faceless YouTube channel (animated/2D character, no real host)
- User mentions "faceless channel", "AI video pipeline", "script to video", "YouTube Short
  automation", or similar
- Continuing an existing production (a channel with an established character/visual style)

**Do NOT use for:** live-action or human-hosted video, audio-only podcast production, or
platforms other than YouTube (Shorts classification rules in this skill are YouTube-specific).

## Required Input

1. **Topic or prompt** (one sentence is enough)
2. **Format**: Short (~15-60s) or full video (target 4-6 min, hard cap 8 min)
3. **Optional `character_profile.json`** — visual style, character description, color
   palette, TTS voice ID, target word count. If absent, ask the user for these once and
   reuse them for every future video in the same series (see
   [references/character-consistency.md](references/character-consistency.md)).

## Approval Gates (default behavior)

- Before any credit-spending generation call (image, motion, TTS, upscale, etc.), state the
  checked cost and get explicit approval — do not guess a cost, check it first.
- Before publishing/uploading, get a separate explicit approval, even if generation was
  already approved.
- A user may grant a standing "topic-only approval" for a specific established series (run
  the whole pipeline unattended after picking a topic). Treat this as scoped to that one
  series, not a blanket rule for all future work, unless the user says otherwise.

## Pipeline Stages

### Step 1: Script
Write narration text sized to the format: for a Short, ~2-4 short sentences per scene, total
10-45s of speech; for a full video, target word count = desired minutes x ~140 words/minute
(measure your actual TTS engine's real pace once and use that instead of assuming 140).

### Step 2: Narration (TTS)
Generate the voice track from the script using the character's assigned voice. Keep the same
voice ID across every video in a series — do not substitute a different voice "just for this
one," even temporarily; if the primary voice is unavailable, tell the user and wait rather
than shipping a mismatched voice.

### Step 3: Scene Breakdown
Split the narration into scenes using **measured** audio duration, not a guess:
`scene_count = ceil(real_narration_seconds / per_clip_ceiling_seconds)`
Use ~10s per clip for full videos, ~5s for Shorts (most motion models lose coherence past
this per-shot length). See [references/pipeline-math.md](references/pipeline-math.md) for
the full formula and worked examples. For Shorts specifically, default to 3 scenes even at
very short total lengths — 2 scenes reads as visually flat.

### Step 4: Scene Image Prompts (Character Lock)
Build each scene's image prompt from a fixed "character lock" text block (exact wording,
reused verbatim every time) plus the scene-specific action/setting, and chain the
first-generated scene image in as a visual reference for every later scene. This is what
keeps the character's face/outfit/colors consistent across a whole video. Full technique and
example prompt block in
[references/character-consistency.md](references/character-consistency.md).

### Step 5: Generate & Inspect Images
Generate each scene image, then **visually inspect it before moving on** — check for broken
object geometry (hands, vehicles, furniture, and anything at an unusual angle are the most
common failure). If a scene fails this check, regenerate it (cheap) rather than animating a
broken image. Do not treat "the API call returned 200" as proof the image is usable.

### Step 6: Animate Each Scene
Send each approved scene image (plus its narration segment, if the model takes audio) to the
motion/video model to produce the moving clip.

### Step 7: Inspect the Animated Clips Too
Extract 1-2 frames from each *finished* clip (e.g. `ffmpeg -ss <t> -vframes 1`) and inspect
those as well. Motion generation introduces its own artifacts (a hand drifting or detaching
mid-motion) that were not present in the approved still image — checking only the source
image is not enough.

### Step 8: Assemble
Concatenate the clips and mux in the full narration track with FFmpeg. Verify the output
with `ffprobe -show_format` (not just the process exit code) before trusting it — a captioned
or assembled file can come out truncated/corrupted even when the calling process reported
success.

### Step 9: Captions
Transcribe the final audio locally (e.g. faster-whisper) and burn subtitles in as a hard
(non-optional) part of every delivered video, not a toggle. Re-verify the burned file with
`ffprobe` after this step too, for the same reason as Step 8.

### Step 10: Metadata
For every finished video, always produce, in full (not summarized): a polished title, a
polished description ending in a short disclaimer appropriate to the niche (e.g.
educational/not-professional-advice for finance/health/legal topics), and a set of tags. See
[references/qa-and-shorts-classification.md](references/qa-and-shorts-classification.md) for
the exact rules that make a Short actually get classified as a Short by YouTube.

### Step 11: Delivery
Either hand off the finished file + metadata to a fixed folder for manual upload, or — if
YouTube API credentials are configured and the user has approved it — publish directly. Never
auto-publish without the separate approval described above.

## Examples

### Example 1: New Short
User says: "Make a 20-second Short about why people overpay for extended warranties."
Result: 3-scene script (~50-60 words total) -> narration -> character-locked scene images
(inspected) -> animated clips (inspected) -> assembled + captioned -> title/description/tags
with `#Shorts` in the title -> delivered for approval before upload.

### Example 2: Full video, existing series
User says: "Next video: the psychology of impulse buying." (character_profile.json already
exists from a prior video)
Result: ~700-word script (~5 min at 140 wpm) -> narration -> ~20 scenes at ~10s each -> full
pipeline through metadata -> delivered to the series' standard output location.

## Troubleshooting

### Error: A generated scene image has an anatomically/geometrically broken object
Cause: Complex objects (vehicles, furniture at odd angles, multiple hands) are where image
models most often fail, even when the character itself renders fine.
Solution: Regenerate just that scene (usually cheap) before animating it. Never skip the
visual-inspection step to save time.

### Error: A Short doesn't show up in YouTube's Shorts shelf
Cause: YouTube's primary programmatic classification signal is `#Shorts` appearing in the
**title** itself, not just the description — API uploads are also documented as less
reliably auto-classified than app-uploaded Shorts even when duration/aspect-ratio criteria
are met.
Solution: Always put `#Shorts` in the title (not only the description). If it still shows as
a regular video while `unlisted`, that can resolve after the video is made `public` — wait
and re-check rather than assuming failure and re-uploading.

### Error: Burned-in caption output plays but looks corrupted, or ffprobe reports "moov atom
not found," despite the burn-in process exiting with code 0
Cause: A background/detached FFmpeg process can report success before the file is fully
flushed to disk.
Solution: Re-run the burn-in step (it's fast — it reuses the already-generated subtitle
file). Always confirm with `ffprobe -show_format` before treating output as final, not just
the exit code.

### Error: Audio-driven lip-sync produces zero visible mouth movement on a flat/2D-vector
character
Cause: Lip-sync/talking-head models are built and tuned for photoreal faces; they frequently
fail silently (still charge for the run, return a video with new audio, but no real mouth
tracking) on flat illustrated character styles.
Solution: For flat/vector-style characters, skip audio-driven lip-sync. General body/camera
motion + voiceover + captions is the actual norm for this content genre, not a compromise.
Spot-check by cropping the mouth region across a few timestamps — a quick full-video watch is
not enough to catch this.

### Error: Scene count feels wrong (too few/many relative to the narration)
Cause: Scene count was guessed instead of computed from the real, measured narration
duration.
Solution: Always generate the narration audio first, measure its real duration, then compute
scene count from that (see Step 3 / references/pipeline-math.md). Do not plan scene count
before you have real audio to measure.
