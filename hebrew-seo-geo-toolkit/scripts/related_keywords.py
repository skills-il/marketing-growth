#!/usr/bin/env python3
"""
Related keywords from Google "searches related to" (DataForSEO Labs, paid).
Endpoint: dataforseo_labs/google/related_keywords/live

Defaults to Israel (2376) and Hebrew (he). Volume is read from
keyword_data.keyword_info.search_volume and organic difficulty (0-100) from
keyword_data.keyword_properties.keyword_difficulty. Billed per task plus per
returned item, so --limit is sent to the API rather than trimmed locally.

Usage: python3 scripts/related_keywords.py "ביטוח רכב" --depth 2 --limit 50
"""
import argparse
from dataforseo_api import add_market_args, api_post, check_labs_market, format_count, get_result

# Maximum keywords per depth level, as published in the DataForSEO docs.
DEPTH_MAX = {0: 1, 1: 8, 2: 72, 3: 584, 4: 4680}


def main():
    parser = argparse.ArgumentParser(description="Related keywords (paid)")
    parser.add_argument("keyword", help="Seed keyword")
    add_market_args(parser)
    parser.add_argument("--depth", "-d", type=int, default=1, choices=range(0, 5),
                        help="Depth 0-4 (default 1)")
    parser.add_argument("--limit", "-l", type=int, default=50, help="Max items, 1-1000 (default 50)")
    args = parser.parse_args()
    check_labs_market(args.location, args.language)

    data = [{
        "keyword": args.keyword,
        "location_code": args.location,
        "language_code": args.language,
        "depth": args.depth,
        "limit": max(1, min(args.limit, 1000)),
    }]
    response = api_post("dataforseo_labs/google/related_keywords/live", data)
    results = get_result(response)

    print(f"keyword: {args.keyword}")
    print(f"location: {args.location} language: {args.language} depth: {args.depth}"
          f" (up to {DEPTH_MAX[args.depth]} keywords)")
    rows = []
    for result in results:
        for item in result.get("items") or []:
            kd = item.get("keyword_data") or {}
            info = kd.get("keyword_info") or {}
            props = kd.get("keyword_properties") or {}
            if kd.get("keyword"):
                rows.append((kd["keyword"], info.get("search_volume") or 0,
                             props.get("keyword_difficulty", "N/A")))
    if not rows:
        print("No related keywords found")
        return
    rows.sort(key=lambda r: r[1], reverse=True)
    print(f"related_keywords[{len(rows)}]{{keyword,volume,difficulty_0_100}}:")
    for keyword, volume, difficulty in rows:
        print(f"  {keyword},{format_count(volume)},{difficulty}")


if __name__ == "__main__":
    main()
