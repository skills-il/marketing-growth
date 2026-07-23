# Character Consistency: Lock Block + Reference Chaining

Faceless-channel viewers notice immediately if the character's face, outfit, or color
palette drifts between scenes. Two techniques fix this reliably and should always be used
together, not as alternatives.

## 1. The Character Lock Block

Keep a fixed, word-for-word description of the character and prepend it to *every* scene
image prompt, unchanged. Do not paraphrase or shorten it "to save tokens" — small wording
changes are exactly what causes drift between scenes generated minutes apart.

Template:

```
CHARACTER LOCK (do not deviate):
[Name] — [hair: exact color/length/style], [exact outfit and colors],
[build/proportions if stylistically relevant], [art style tag, e.g. "polished 2D cel-shaded
illustration, soft gradients, directional lighting"]. This character must look identical in
every scene: same face shape, same hair, same outfit, same color palette.

SCENE: [scene-specific action, setting, camera framing — this part changes per scene]
```

Store this block once in the series' `character_profile.json` (or equivalent config) and
read it back verbatim for every scene, across every video in the series — not just within
one video.

## 2. Reference-Image Chaining

Generate the *first* scene of a video normally (character lock + scene description only). For
every scene after that, pass the first scene's generated image as a visual reference input
to the image model (image-to-image / reference-image parameter), in addition to the text
prompt. This anchors face/outfit/palette far more reliably than text alone, especially for
distinctive stylized character designs.

If the image model supports multiple reference images, prefer chaining from the single
"canonical" first-scene image for the whole video rather than each scene referencing the
previous one — chaining scene-to-scene lets small drift compound over a long video, while
always referencing the same canonical image does not.

## Applying This Across a Series, Not Just One Video

The character lock block and the canonical reference image should be reused across *every*
video in a series, not regenerated per-video. If the visual style is upgraded later (higher
render fidelity, new lighting approach, etc.), update the style tag portion of the lock block
but keep the character description itself (face, hair, outfit) unchanged — viewers should
still recognize the same character, just at higher production quality.

## What NOT to Drop for Convenience

If a later step in the pipeline changes providers (e.g. switching image or animation
vendors), preserve the same character-lock + reference-chaining behavior with the new
provider's equivalent mechanism. Do not silently drop character consistency to make a
provider swap easier — verify the new provider can still take a reference image before
committing to the switch.
