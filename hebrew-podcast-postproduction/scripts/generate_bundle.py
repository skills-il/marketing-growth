#!/usr/bin/env python3
"""
Generate a complete post-production bundle for a Hebrew podcast episode.

This is a scaffolding helper: it takes a transcript + chapter list + clip list
and writes the directory structure described in SKILL.md. The agent (or a
human) is responsible for providing the semantic inputs (chapter titles,
clip selection, social captions). This script handles the mechanical file
emission, timestamp formatting, and FFmpeg command generation.

Usage:
    python generate_bundle.py \\
        --episode 42 \\
        --audio episode-42.mp3 \\
        --chapters chapters_input.json \\
        --clips clips_input.json \\
        --output ./episode-42/

chapters_input.json:
    [
      {"startTime": 0, "title": "פתיחה"},
      {"startTime": 150, "title": "איך זה התחיל"}
    ]

clips_input.json:
    [
      {
        "id": 1,
        "start": 754.3,
        "end": 825.1,
        "srt_cues": [
          {"start": 0.0, "end": 3.2, "text": "..."},
          ...
        ],
        "captions": {
          "instagram": "...",
          "tiktok": "...",
          "x": "...",
          "linkedin": "..."
        }
      }
    ]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


# Vowel points and cantillation only. U+05BE MAQAF, U+05C0 PASEQ and
# U+05C3 SOF PASUQ are punctuation and are deliberately excluded, matching
# the nikud definition in SKILL.md Step A1.
NIKUD_RE = re.compile(r"[\u0591-\u05BD\u05BF\u05C1\u05C2\u05C4\u05C5\u05C7]")


def strip_nikud(text: str) -> str:
    """Remove Hebrew vowel points only.

    Deliberately narrower than the full U+0591-U+05C7 block: that range also
    holds MAQAF (U+05BE), PASEQ (U+05C0) and SOF PASUQ (U+05C3), which are
    punctuation, not nikud. Stripping the maqaf turns "בית-ספר" into "ביתספר".
    """
    return NIKUD_RE.sub("", text)


def format_hhmmss(seconds: float, millis: bool = False) -> str:
    """Format seconds as HH:MM:SS, optionally with milliseconds.

    The clip SRT cues are rebased to the clip's true fractional start, so a cut
    point truncated to a whole second desyncs every burned-in cue by up to a
    second. FFmpeg accepts HH:MM:SS.mmm on -ss/-to, so use millis=True for cut
    points and plain HH:MM:SS for human-facing chapter lines.
    """
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    if millis:
        s = seconds % 60
        return f"{h:02d}:{m:02d}:{s:06.3f}"
    return f"{h:02d}:{m:02d}:{int(seconds % 60):02d}"


VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}
AUDIO_EXTS = {".mp3", ".m4a", ".wav", ".aac", ".flac", ".ogg", ".opus"}


def check_mode_matches_media(audio_path: str, mode: str) -> str | None:
    """Return a warning if --mode contradicts the source file's extension.

    Neither direction is survivable at ffmpeg run time: audio mode on an MP4
    stream-copies H.264 into an .mp3 container ("Could not find tag for codec
    h264"), and video mode on an MP3 applies -vf to a file with no video
    stream. The script does not probe the file, so this is an extension check,
    not a guarantee.
    """
    ext = Path(audio_path).suffix.lower()
    if mode == "audio" and ext in VIDEO_EXTS:
        return (
            f"--mode audio was used with a video file ({ext}). The emitted "
            f"'-c copy' command will fail. Pass --mode video."
        )
    if mode == "video" and ext in AUDIO_EXTS:
        return (
            f"--mode video was used with an audio-only file ({ext}). The "
            f"emitted '-vf subtitles=...' command has no video stream to draw "
            f"on. Pass --mode audio."
        )
    return None


def format_srt_ts(seconds: float) -> str:
    total_ms = round(seconds * 1000)
    h = total_ms // 3_600_000
    m = (total_ms % 3_600_000) // 60_000
    s = (total_ms % 60_000) // 1000
    ms = total_ms % 1000
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def validate_spotify_chapters(chapters: list[dict]) -> tuple[list[str], list[str]]:
    """Split Spotify's rules into what it enforces and what it merely advises.

    Returns (errors, warnings). Only the enforced rules are errors. The
    40-character title figure is worded by Spotify as "aim for chapter titles
    under 40 characters", under "Tips for chapter titles" - it is a
    readability recommendation, not a parse requirement, and treating it as
    fatal rejects legitimate Hebrew titles, which carry fewer ideas per
    character than English ones.
    """
    errors: list[str] = []
    warnings: list[str] = []
    if len(chapters) < 3:
        errors.append(f"need at least 3 chapters, got {len(chapters)}")
    if chapters and chapters[0]["startTime"] != 0:
        errors.append(f"first chapter must start at 0, got {chapters[0]['startTime']}")
    for i, ch in enumerate(chapters):
        title = strip_nikud(ch["title"])
        if len(title) > 40:
            warnings.append(
                f"chapter {i} title is {len(title)} chars; Spotify advises under 40 "
                f"for readability (not a hard limit): {title[:24]}..."
            )
        if re.match(r"^\s*\d+\s*[-.)]\s+", title):
            warnings.append(
                f"chapter {i} title starts with an index; Spotify strips it "
                f"(\"1 - Introduction\" is reformatted): {title[:24]}..."
            )
        if i > 0:
            gap = ch["startTime"] - chapters[i - 1]["startTime"]
            if gap < 0:
                errors.append(
                    f"chapter {i} starts before chapter {i - 1}; Spotify requires "
                    f"chronological order"
                )
            elif gap < 30:
                errors.append(f"chapter {i} only {gap}s after previous (min 30s)")
    return errors, warnings


def write_spotify_chapters(chapters: list[dict], out_path: Path) -> None:
    lines = []
    for ch in chapters:
        title = strip_nikud(ch["title"])
        ts = format_hhmmss(ch["startTime"])
        lines.append(f"({ts}) {title}")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_chapters_json(chapters: list[dict], out_path: Path) -> None:
    payload = {
        "version": "1.2.0",
        "chapters": [
            {"startTime": ch["startTime"], "title": ch["title"]}
            for ch in chapters
        ],
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_srt(cues: list[dict], out_path: Path) -> None:
    lines: list[str] = []
    for idx, cue in enumerate(cues, start=1):
        lines.append(str(idx))
        lines.append(f"{format_srt_ts(cue['start'])} --> {format_srt_ts(cue['end'])}")
        lines.append(cue["text"].strip())
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


FFMPEG_VIDEO_TEMPLATE = """#!/usr/bin/env bash
set -euo pipefail

ffmpeg -y \\
  -ss {start_ts} -to {end_ts} \\
  -i "{audio}" \\
  -vf "subtitles={srt_path}:force_style='FontName=Heebo,FontSize=22,PrimaryColour=&H00FFFFFF,BorderStyle=3,Outline=2,Shadow=0,MarginV=40':shaping=complex" \\
  -c:a aac -b:a 192k -c:v libx264 -preset fast -crf 20 \\
  "{output}"

# shaping=complex is what makes Hebrew lay out correctly. It was exposed on the
# subtitles filter in FFmpeg on 2026-06-23; on an older build the option is
# rejected. Check with:
#   ffmpeg -hide_banner -h filter=subtitles | grep shaping
# If it is absent, drop ":shaping=complex" above and instead convert to ASS,
# which has always had the option:
#   ffmpeg -i {srt_path} clip.ass
#   ffmpeg -y -ss {start_ts} -to {end_ts} -i "{audio}" \\
#     -vf "ass=clip.ass:shaping=complex" -c:a aac -c:v libx264 -crf 20 "{output}"
# Note that force_style is a subtitles-filter option only; the ass filter does
# not accept it, so set FontName/FontSize in the .ass [V4+ Styles] Style line.
"""

FFMPEG_AUDIO_TEMPLATE = """#!/usr/bin/env bash
set -euo pipefail

ffmpeg -y \\
  -ss {start_ts} -to {end_ts} \\
  -i "{audio}" \\
  -c copy \\
  "{output}"
"""


def write_ffmpeg_script(clip: dict, audio_path: str, srt_path: str, out_path: Path, mode: str) -> None:
    start_ts = format_hhmmss(clip["start"], millis=True)
    end_ts = format_hhmmss(clip["end"], millis=True)
    output_ext = "mp4" if mode == "video" else "mp3"
    output = out_path.parent / f"clip-{clip['id']:02d}.{output_ext}"
    template = FFMPEG_VIDEO_TEMPLATE if mode == "video" else FFMPEG_AUDIO_TEMPLATE
    out_path.write_text(
        template.format(
            start_ts=start_ts,
            end_ts=end_ts,
            audio=audio_path,
            srt_path=srt_path,
            output=output,
        ),
        encoding="utf-8",
    )
    out_path.chmod(0o755)


def write_social_captions(clip: dict, out_dir: Path) -> None:
    for platform, text in clip.get("captions", {}).items():
        (out_dir / f"clip-{clip['id']:02d}-{platform}.txt").write_text(
            text + "\n", encoding="utf-8"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episode", type=int, required=True)
    parser.add_argument("--audio", required=True, help="Path to episode audio file")
    parser.add_argument("--chapters", required=True, help="Path to chapters_input.json")
    parser.add_argument("--clips", required=True, help="Path to clips_input.json")
    parser.add_argument("--output", required=True, help="Output directory")
    parser.add_argument("--mode", choices=["audio", "video"], default="audio")
    args = parser.parse_args()

    out = Path(args.output)
    (out / "chapters").mkdir(parents=True, exist_ok=True)
    (out / "clips").mkdir(exist_ok=True)
    (out / "social").mkdir(exist_ok=True)

    chapters = json.loads(Path(args.chapters).read_text(encoding="utf-8"))
    clips = json.loads(Path(args.clips).read_text(encoding="utf-8"))

    mode_warning = check_mode_matches_media(args.audio, args.mode)
    if mode_warning:
        print(f"WARNING: {mode_warning}")

    errors, warnings = validate_spotify_chapters(chapters)
    if warnings:
        print("Spotify chapter warnings (non-fatal):")
        for w in warnings:
            print(f"  - {w}")
    if errors:
        print("Spotify chapter validation errors:")
        for e in errors:
            print(f"  - {e}")
        return 1

    write_spotify_chapters(chapters, out / "chapters" / "spotify-chapters.txt")
    write_chapters_json(chapters, out / "chapters" / "chapters.json")

    for clip in clips:
        clip_id = clip["id"]
        srt_path = out / "clips" / f"clip-{clip_id:02d}.srt"
        ffmpeg_path = out / "clips" / f"clip-{clip_id:02d}.ffmpeg.sh"
        write_srt(clip["srt_cues"], srt_path)
        write_ffmpeg_script(
            clip=clip,
            audio_path=args.audio,
            srt_path=str(srt_path),
            out_path=ffmpeg_path,
            mode=args.mode,
        )
        write_social_captions(clip, out / "social")

    print(f"Bundle written to {out}")
    print(f"  - {len(chapters)} chapters")
    print(f"  - {len(clips)} clips")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
