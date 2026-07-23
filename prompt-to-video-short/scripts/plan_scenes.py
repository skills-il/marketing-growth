#!/usr/bin/env python3
"""
Compute a scene plan from real (measured) narration duration.
Usage: plan_scenes.py <narration_seconds> [--ceiling 10] [--floor 3] [--min-scenes 1]

No dependencies beyond the standard library. Does not call any API or store any credentials.
"""
import argparse
import math


def plan_scenes(narration_seconds: float, ceiling: float, floor: float, min_scenes: int) -> dict:
    if narration_seconds <= 0:
        raise ValueError("narration_seconds must be positive")

    scene_count = max(min_scenes, math.ceil(narration_seconds / ceiling))

    # Shrink scene_count if an even split would put any scene under the model's minimum
    while scene_count > min_scenes and (narration_seconds / scene_count) < floor:
        scene_count -= 1

    per_scene = narration_seconds / scene_count
    return {
        "narration_seconds": narration_seconds,
        "scene_count": scene_count,
        "seconds_per_scene": round(per_scene, 2),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("narration_seconds", type=float)
    parser.add_argument("--ceiling", type=float, default=10.0,
                         help="Practical per-clip coherence ceiling in seconds (default 10s, use ~5s for Shorts)")
    parser.add_argument("--floor", type=float, default=3.0,
                         help="Motion model's minimum clip duration in seconds (default 3s)")
    parser.add_argument("--min-scenes", type=int, default=1,
                         help="Never go below this many scenes even for very short narration")
    args = parser.parse_args()

    result = plan_scenes(args.narration_seconds, args.ceiling, args.floor, args.min_scenes)
    print(f"Narration: {result['narration_seconds']}s")
    print(f"Scene count: {result['scene_count']}")
    print(f"Seconds per scene: {result['seconds_per_scene']}")


if __name__ == "__main__":
    main()
