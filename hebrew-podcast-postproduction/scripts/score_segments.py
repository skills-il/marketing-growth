#!/usr/bin/env python3
"""
Score transcript segments for podcast clip shareability.

Reads a Whisper / ElevenLabs Scribe JSON transcript on stdin or from a file
and emits a ranked list of candidate clip windows (start, end, score, reason).

Usage:
    python score_segments.py transcript.json
    cat transcript.json | python score_segments.py -

Input format (Whisper JSON):
    {
      "language": "he",
      "segments": [
        {"start": 0.0, "end": 3.2, "text": "..."},
        ...
      ]
    }
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from typing import Iterable


HEBREW_FILLER = {"אה", "אמ", "כאילו", "בעצם", "אוקיי", "או קיי", "נו", "אז"}
STRONG_OPENERS_HE = (
    "הטעות", "השיעור", "הרגע", "הסיפור", "אף פעם", "תמיד", "אף אחד",
    "כולם", "בכלל לא", "הדבר הכי", "הפעם הראשונה", "האמת היא",
)
PRONOUN_REFS_HE = {"זה", "זאת", "הוא", "היא", "הם", "הן", "שם", "ההוא", "ההיא"}
LAUGHTER_MARKERS = ("[צחוק]", "(צחוק)", "[laughter]", "(laughter)", "ha ha", "חחח")


@dataclass
class Window:
    start: float
    end: float
    text: str
    score: float
    reasons: list[str]

    @property
    def duration(self) -> float:
        return self.end - self.start


def load_transcript(path: str) -> dict:
    if path == "-":
        return json.load(sys.stdin)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_windows(segments: list[dict], min_sec: float = 30.0, max_sec: float = 90.0) -> Iterable[Window]:
    """Slide a variable window over consecutive segments, emitting candidate clips."""
    n = len(segments)
    for i in range(n):
        start = segments[i]["start"]
        text_parts: list[str] = []
        for j in range(i, n):
            text_parts.append(segments[j]["text"].strip())
            end = segments[j]["end"]
            duration = end - start
            if duration >= min_sec:
                if duration > max_sec:
                    break
                yield Window(start=start, end=end, text=" ".join(text_parts), score=0.0, reasons=[])
                break


def score_quotable_density(text: str) -> tuple[float, list[str]]:
    words = re.findall(r"\S+", text)
    if not words:
        return 0.0, []
    filler_count = sum(1 for w in words if w in HEBREW_FILLER)
    ratio = 1.0 - (filler_count / len(words))
    reasons = [f"filler ratio {filler_count}/{len(words)}"]
    return ratio * 40.0, reasons


def score_emotional_peaks(text: str) -> tuple[float, list[str]]:
    exclaim = text.count("!")
    questions = text.count("?")
    laughs = sum(1 for m in LAUGHTER_MARKERS if m in text)
    score = min((exclaim * 4) + (questions * 2) + (laughs * 5), 25)
    reasons = []
    if exclaim:
        reasons.append(f"{exclaim} exclamations")
    if laughs:
        reasons.append(f"{laughs} laugh markers")
    if questions:
        reasons.append(f"{questions} questions")
    return float(score), reasons


def score_standalone(text: str) -> tuple[float, list[str]]:
    first_20_words = text.split()[:20]
    pronoun_hits = sum(1 for w in first_20_words if w in PRONOUN_REFS_HE)
    if pronoun_hits >= 3:
        return 0.0, [f"{pronoun_hits} orphan pronouns in opener"]
    penalty = pronoun_hits * 5
    return max(20.0 - penalty, 0.0), [f"{pronoun_hits} pronouns in first 20 words"]


def score_topic_hook(text: str) -> tuple[float, list[str]]:
    opener = text.strip()[:80]
    for trigger in STRONG_OPENERS_HE:
        if trigger in opener:
            return 15.0, [f"strong opener: '{trigger}'"]
    if re.search(r"\d", opener):
        return 10.0, ["numerical hook in opener"]
    if opener.lstrip().startswith(("איך", "למה", "מה", "האם")):
        return 12.0, ["question hook"]
    return 3.0, []


def score_window(w: Window) -> Window:
    q_score, q_reasons = score_quotable_density(w.text)
    e_score, e_reasons = score_emotional_peaks(w.text)
    s_score, s_reasons = score_standalone(w.text)
    h_score, h_reasons = score_topic_hook(w.text)
    w.score = q_score + e_score + s_score + h_score
    w.reasons = q_reasons + e_reasons + s_reasons + h_reasons
    return w


def select_top_non_overlapping(windows: list[Window], k: int = 5, min_gap: float = 60.0) -> list[Window]:
    sorted_windows = sorted(windows, key=lambda w: w.score, reverse=True)
    selected: list[Window] = []
    for w in sorted_windows:
        if len(selected) >= k:
            break
        if all(abs(w.start - s.start) >= min_gap for s in selected):
            selected.append(w)
    return sorted(selected, key=lambda w: w.start)


def format_ts(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("transcript", help="Path to Whisper/Scribe JSON, or '-' for stdin")
    parser.add_argument("--top", type=int, default=5, help="Number of clips to select")
    parser.add_argument("--min-gap", type=float, default=60.0, help="Minimum seconds between clips")
    parser.add_argument("--min-sec", type=float, default=30.0, help="Minimum clip length")
    parser.add_argument("--max-sec", type=float, default=90.0, help="Maximum clip length")
    args = parser.parse_args()

    data = load_transcript(args.transcript)
    segments = data.get("segments", [])
    if not segments:
        print("error: no segments found in transcript", file=sys.stderr)
        return 1

    windows = list(build_windows(segments, min_sec=args.min_sec, max_sec=args.max_sec))
    scored = [score_window(w) for w in windows]
    top = select_top_non_overlapping(scored, k=args.top, min_gap=args.min_gap)

    print(f"# Top {len(top)} clip candidates\n")
    for idx, w in enumerate(top, start=1):
        print(f"## Clip {idx:02d}")
        print(f"- Start: {format_ts(w.start)}")
        print(f"- End:   {format_ts(w.end)}")
        print(f"- Duration: {w.duration:.1f}s")
        print(f"- Score: {w.score:.1f}")
        print(f"- Reasons: {'; '.join(w.reasons)}")
        preview = w.text[:120] + ("..." if len(w.text) > 120 else "")
        print(f"- Preview: {preview}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
