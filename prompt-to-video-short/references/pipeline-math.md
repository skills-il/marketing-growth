# Pipeline Math: Word Count, Scene Count, Cost Estimation

## Narration Length -> Word Count

Do not assume a generic "words per minute" figure for text-to-speech — measure it once for
the actual voice/engine being used (generate a short test line, measure its real duration,
compute `words / (duration_seconds / 60)`), then reuse that measured rate for every future
script in the series. A commonly-cited baseline is ~140 words/minute for natural-paced
narration, but real engines vary — treat 140 as a starting estimate to verify, not a constant
to trust blindly.

Target word count:
```
target_words = target_minutes * measured_words_per_minute
```

For a hard maximum runtime (e.g. "never exceed 8 minutes"), compute the corresponding word
count ceiling from the same rate and build in a tolerance band (e.g. ±10-15%) rather than a
single exact number, since actual TTS output length varies slightly run to run.

## Narration Duration -> Scene Count

Never guess the number of scenes before real narration audio exists. Once the TTS audio is
generated, measure its actual duration and compute:

```
scene_count = ceil(real_narration_seconds / per_clip_ceiling_seconds)
```

`per_clip_ceiling_seconds` is the practical length beyond which a given motion/video model's
single-shot output starts losing coherence (motion artifacts, drift) — this is model-specific
and should be verified per provider, but ~10 seconds for full-length video and ~5 seconds for
Shorts are reasonable starting points to verify against.

Then distribute the narration proportionally across that many scenes. Watch for a specific
edge case: at short total narration lengths (typical for Shorts), a naive even split can put
one or more scenes under the motion model's *minimum* clip duration (many models have a floor
around 3 seconds). When that happens, reduce the scene count rather than requesting clips
below the model's minimum.

### Worked Example
- Real narration duration: 34 seconds, format: Short, per-clip ceiling: 5s
- `scene_count = ceil(34 / 5) = 7` scenes at the ceiling — but Shorts read better with fewer,
  slightly longer scenes for visual variety. A commonly effective compromise: default to 3
  scenes and let per-scene duration come out around 10-12s each here, checking that no
  resulting scene falls under the motion model's minimum before committing.

## Cost Estimation Before Spending

Before any credit-spending generation call, get the actual cost from the provider's own
pricing/cost-check endpoint or documentation — never estimate a AI-generation cost from
memory or a prior project's numbers, since providers change pricing and per-unit costs (e.g.
per-second video pricing, flat-rate image pricing) are usually queryable directly. State the
checked number to the user before running the paid call, per the approval-gate rule in the
main SKILL.md.
