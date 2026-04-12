# FFmpeg + Hebrew Subtitle Burn-in

Burning Hebrew subtitles into a video clip with FFmpeg requires three libraries working together: **libass** (subtitle renderer), **FriBidi** (bidirectional text resolution), and **HarfBuzz** (complex text shaping). All three must be present at the FFmpeg build time. FriBidi or HarfBuzz missing at build time means Hebrew text renders as a visual mirror image of the logical string.

## Verify your FFmpeg build

```bash
ffmpeg -version 2>&1 | grep -E 'libass|fribidi|harfbuzz'
```

Expected output (at least three lines, each containing one of the libraries):

```
--enable-libass
--enable-libfribidi
--enable-libharfbuzz
```

If any of these three is missing, reinstall FFmpeg from a source that includes them:

| Platform | Command | Notes |
|----------|---------|-------|
| macOS | `brew install ffmpeg` | Homebrew ships all three by default |
| Ubuntu 22.04+ | `apt install ffmpeg` (as root) | Main package in recent Ubuntu |
| Debian 12+ | `apt install ffmpeg` (as root) | Main package in recent Debian |
| Windows | Download from `ffmpeg.org` builds | Use the full-feature build, not minimal |
| Docker | `jrottenberg/ffmpeg:latest` | Full-feature image |

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
curl -L "https://fonts.google.com/download?family=Heebo" -o heebo.zip
unzip heebo.zip -d ~/.fonts/heebo
fc-cache -fv
```

Verify fontconfig sees the font:

```bash
fc-list | grep -i heebo
```

## Common failure modes

**Text is mirrored left-to-right.**
FriBidi missing from libass. Reinstall FFmpeg with a build that includes `--enable-libfribidi`.

**Hebrew characters render as empty boxes.**
Fontconfig cannot find a font with Hebrew glyphs. Install a Hebrew-capable font, run `fc-cache -fv`, and reference it by exact name in `force_style`.

**Punctuation appears on the wrong side of the line.**
Actually, this is usually correct. Hebrew bidi rules place LTR punctuation after (visually: to the left of) the last Hebrew character in a line. If it looks wrong to you, it is probably right to a Hebrew reader - verify with a native speaker before trying to "fix" it.

**Subtitles are styled but invisible.**
The `MarginV` value may push the subtitle off-screen on a very short clip. Reduce to 20 or remove the parameter entirely.

**Colon inside `force_style` breaks the filter.**
FFmpeg filter arguments use `:` as a separator. If any style value contains a colon, escape the entire `force_style` string with backslashes around inner colons, or use the `.ass` format instead of `subtitles=` with `force_style`.

## Reference

- FFmpeg subtitles filter docs (see Reference Links in SKILL.md)
- libass upstream README (see Reference Links in SKILL.md)
