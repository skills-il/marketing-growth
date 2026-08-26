# FFmpeg + Hebrew Subtitle Burn-in

Burning Hebrew subtitles into a video clip with FFmpeg requires three libraries working together: **libass** (subtitle renderer), **FriBidi** (bidirectional text resolution), and **HarfBuzz** (complex text shaping). Only the first is an FFmpeg build option. FriBidi and HarfBuzz are dependencies **of libass**, resolved when libass itself is built, and they never appear in FFmpeg's configuration line.

## Verify your FFmpeg build

```bash
ffmpeg -filters | grep ' subtitles '            # no output = this build has no libass at all
ffmpeg -version | grep -o -- '--enable-libass'  # should print --enable-libass
```

**Do not use `ffmpeg -version | grep -E 'libass|fribidi|harfbuzz'` as the Hebrew-readiness test.** `--enable-libfribidi` and `--enable-libharfbuzz` are FFmpeg's build flags for the **drawtext** filter, not for libass. FFmpeg's own `configure` help describes them as:

```
--enable-libfribidi      enable libfribidi, improves drawtext filter [no]
--enable-libharfbuzz     enable libharfbuzz, needed for drawtext filter [no]
```

A build that renders Hebrew subtitles perfectly will show neither. The `homebrew-ffmpeg/ffmpeg` tap recommended below does not pass `--enable-libfribidi` at all, and its Hebrew burn-in is correct, because its `libass` dependency links fribidi and harfbuzz itself. Grepping for those two strings produces a false "broken build" verdict and sends you into a reinstall loop on a build that was never broken.

To inspect the libass side:

```bash
brew info libass            # macOS: expect fribidi and harfbuzz under Dependencies
pkg-config --modversion libass
```

If `ffmpeg -filters` has no `subtitles` entry, reinstall FFmpeg from a source that includes libass:

| Platform | Command | Notes |
|----------|---------|-------|
| macOS (default brew) | `brew install ffmpeg` | Does NOT include libass as of 2026 (verified against the homebrew-core formula dependency list); the `subtitles` filter is absent entirely and burn-in fails. Use one of the rows below instead. |
| macOS (recommended) | `brew tap homebrew-ffmpeg/ffmpeg && brew install homebrew-ffmpeg/ffmpeg/ffmpeg` | Links `ffmpeg` on PATH with libass + FriBidi + HarfBuzz. Do NOT append `--with-libass` (removed, errors out). If core ffmpeg is installed, `brew unlink ffmpeg` first |
| macOS (alternative) | `brew install ffmpeg-full` | homebrew-core, bundles libass + HarfBuzz, but KEG-ONLY: bare `ffmpeg` still points at the non-libass build. Call `"$(brew --prefix ffmpeg-full)/bin/ffmpeg"` or add that bin dir to PATH |
| Ubuntu / Debian | `apt install ffmpeg` (as root) | The distro package is built against libass, and the distro `libass9` links fribidi and harfbuzz. Confirm on your release with `ffmpeg -filters \| grep ' subtitles '` rather than assuming. |
| Windows | Download from `ffmpeg.org` builds | Use the full-feature build, not minimal |
| Docker | `jrottenberg/ffmpeg:latest` | Full-feature image |

After install, verify the filter is actually present:

```bash
ffmpeg -filters | grep ' subtitles '
```

Empty output means libass is still missing and the burn-in pipeline will fail. A missing `fribidi` or `harfbuzz` string in `ffmpeg -version` is **not** a fault; see above.

## Shaping: the option that actually matters for Hebrew

Both the `subtitles` and `ass` filters expose a `shaping` option in current FFmpeg (`shaping` sits in the shared option macro in `libavfilter/vf_subtitles.c`, expanded into both filters' option tables; it was exposed on `subtitles` on 2026-06-23, so older builds have it only on `ass`). FFmpeg documents the `complex` mode as "Required for correct rendering of complex scripts such as Arabic, **Hebrew**, Devanagari and Thai. Requires libass to be built with HarfBuzz."

Prefer adding it to `subtitles`, which keeps `force_style` working:

```bash
ffmpeg -i clip.mp4 -vf "subtitles=clip.srt:force_style='FontName=Heebo':shaping=complex" -c:a copy out.mp4
```

Check first with `ffmpeg -hide_banner -h filter=subtitles | grep shaping`. If the option is absent, convert to ASS and set the style inside the file, because `force_style` is a `subtitles`-only option that the `ass` filter does not accept:

```bash
ffmpeg -i clip.srt clip.ass   # then edit the [V4+ Styles] Style: line
ffmpeg -i clip.mp4 -vf "ass=clip.ass:shaping=complex" -c:a copy out.mp4
```

If Hebrew is mis-ordered on a build whose libass does link FriBidi, this is almost always the cause, not a missing bidi library.

## Burn-in command

```bash
ffmpeg -ss 00:12:34 -to 00:13:45 \
  -i episode-NN.mp4 \
  -vf "subtitles=clips/clip-01.srt:force_style='FontName=Heebo,FontSize=22,PrimaryColour=&H00FFFFFF,BorderStyle=3,Outline=2,Shadow=0,MarginV=40'" \
  -c:a aac -c:v libx264 -preset fast -crf 20 \
  clips/clip-01.mp4
```

The `subtitles` filter reads the SRT from disk and renders it through libass. The `force_style` parameter overrides ASS style defaults - the values above produce white text with a solid dark outline, vertically margined 40 pixels from the bottom (good for Instagram Reels and TikTok where UI overlays the bottom of the frame).

## Font requirements

libass resolves `FontName` through fontconfig. For Hebrew, the font must contain:

1. The full Hebrew Unicode block (U+0590 to U+05FF)
2. Ideally also Latin extended, digits, and punctuation (so English words in the caption render correctly)

Recommended fonts that cover both:

| Font | Source | Notes |
|------|--------|-------|
| Heebo | Google Fonts | Clean sans-serif, good for mobile |
| Rubik | Google Fonts | Rounded, friendly, high legibility |
| Assistant | Google Fonts | Neutral, tech-product aesthetic |
| Open Sans Hebrew | Google Fonts | Variant of Open Sans with Hebrew |

Install system-wide so fontconfig can find them:

```bash
# macOS
brew install --cask font-heebo font-rubik font-assistant

# Linux
mkdir -p ~/.fonts
# The google/fonts repo serves the variable TTF directly, no zip step and no
# JS-rendered download page in the way.
curl -L "https://raw.githubusercontent.com/google/fonts/main/ofl/heebo/Heebo%5Bwght%5D.ttf" \
  -o ~/.fonts/Heebo.ttf
fc-cache -fv
```

Verify fontconfig sees the font:

```bash
fc-list | grep -i heebo
```

## Common failure modes

**Text is mirrored left-to-right.**
FriBidi missing from libass. Reinstall the libass dependency chain (`brew reinstall fribidi harfbuzz libass`, then reinstall FFmpeg from the homebrew-ffmpeg tap). Rebuilding FFmpeg with `--enable-libfribidi` does nothing here: that flag belongs to the drawtext filter.

**Hebrew characters render as empty boxes.**
Fontconfig cannot find a font with Hebrew glyphs. Install a Hebrew-capable font, run `fc-cache -fv`, and reference it by exact name in `force_style`. For multi-word family names like `Open Sans Hebrew`, the `FontName=` value must match the exact fontconfig family string, confirm it with `fc-list | grep -i hebrew` first, otherwise libass silently falls back to a non-Hebrew face and renders boxes.

**Punctuation appears on the wrong side of the line.**
Actually, this is usually correct. Hebrew bidi rules place LTR punctuation after (visually: to the left of) the last Hebrew character in a line. If it looks wrong to you, it is probably right to a Hebrew reader - verify with a native speaker before trying to "fix" it.

**Subtitles are styled but invisible.**
The `MarginV` value may push the subtitle off-screen on a very short clip. Reduce to 20 or remove the parameter entirely.

**Colon inside `force_style` breaks the filter.**
FFmpeg filter arguments use `:` as a separator. If any style value contains a colon, escape the entire `force_style` string with backslashes around inner colons, or use the `.ass` format instead of `subtitles=` with `force_style`.

## Reference

- FFmpeg subtitles filter docs (see Reference Links in SKILL.md)
- libass upstream README (see Reference Links in SKILL.md)
