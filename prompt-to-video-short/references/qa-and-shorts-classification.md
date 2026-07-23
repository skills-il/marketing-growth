# Visual QA and YouTube Shorts Classification

## Two-Stage Visual QA (both stages required, neither is optional)

A successful API response is not evidence that a generated asset is usable. Two separate
inspection passes are needed, because each stage introduces different failure modes:

**Stage A — after image generation, before animating:**
Look at the still image for basic object/scene coherence. Complex objects are the highest-
risk category: vehicles, furniture at unusual angles, hands, and machinery are exactly where
image models most often produce geometrically broken results (e.g. a car whose
roofline/window/door don't form a coherent shape), even when the character itself renders
correctly. If a scene fails this check, regenerate it before spending credits on animation —
regenerating a still image is cheap; animating a broken one wastes the (usually more
expensive) motion-generation credits too.

**Stage B — after motion generation, before final assembly:**
Extract one or two frames from the *finished animated clip* (e.g.
`ffmpeg -ss <timestamp> -vframes 1 -y frame.png`) and inspect those too. Motion generation can
introduce artifacts that were not present in the approved still image — most commonly a hand
or limb drifting or detaching partway through the clip. Checking only the pre-animation image
misses this entire class of defect.

Do not skip Stage B because Stage A passed — they catch different things.

## Lip-Sync: When It Works and When It Doesn't

Audio-driven lip-sync / talking-head models are trained on and tuned for photoreal human
faces. On flat, 2D-vector, or heavily stylized illustrated characters, they can fail
*silently*: the call succeeds, credits are charged, a video comes back with the new audio
muxed in — but the mouth never actually moves. A quick watch-through can miss this because
the eye fills in motion that isn't there.

Verification method: crop just the mouth region and compare it across several timestamps
spread through the clip. If the mouth is pixel-identical (or nearly so) across all of them
despite several seconds of speech audio, lip-sync did not work, regardless of what the job
status reported.

For flat/vector character styles, the practical default is to **not** attempt audio-driven
lip-sync at all: general body/camera motion (pans, zooms, gesture loops) combined with
voiceover and burned-in captions is the standard production pattern for this content genre,
not a fallback or compromise. Reserve lip-sync attempts for photoreal or near-photoreal
character styles, and even then, verify with the mouth-crop method before trusting it.

## Getting a Short Correctly Classified as a Short

YouTube's Shorts shelf/tab is driven by a mix of technical criteria (duration under 60s,
vertical 9:16-ish aspect ratio) and a classification signal that is easy to miss:

- **Put `#Shorts` in the video title itself**, not only in the description. Description-only
  placement has been observed to be unreliable — a video meeting every technical criterion,
  with `#Shorts` in the description, did not appear in the Shorts shelf until the title was
  updated to include the tag directly.
- Videos uploaded through the public Data API (`videos.insert`) have been observed to be less
  reliably auto-classified than the same content uploaded through the native app/Shorts
  camera flow, even when all technical criteria are met — belt-and-suspenders title tagging
  matters more for API uploads specifically.
- If a Short still shows as a regular video shortly after upload while its privacy status is
  `unlisted`, that is not necessarily a failure. Shorts-shelf classification has been observed
  to resolve only after the video is switched to `public` (or simply after more processing
  time coincident with that change) — re-check after making it public and after a few more
  minutes before concluding the classification failed and re-uploading.
- A related pitfall: reading a video's metadata back immediately after an update call
  (`videos.update`) can return stale cached data even when the update itself succeeded a
  moment earlier. Don't treat one immediate verification read as ground truth if a change
  appears not to have taken effect — check again before assuming failure.

## Metadata: Always Produce This, Every Time

For every finished video, regardless of format, produce and deliver in full (not
summarized/titles-only):
- A polished, specific title (with `#Shorts` appended for anything under 60s/vertical)
- A polished description, ending in a brief disclaimer appropriate to the content's niche
  (e.g. "for educational purposes only, not professional advice" for finance/health/legal
  topics)
- A set of relevant tags

This is a standing requirement, not something to skip when working outside the normal
pipeline (e.g. during an upstream outage) — write it by hand in that case rather than
omitting it.
