#!/usr/bin/env python3
"""
Backlink list for a domain (DataForSEO, paid).
Endpoint: backlinks/backlinks/live

The target is a domain without https:// or www. Rank is on DataForSEO's
default 0-1000 scale. Billed per task plus per returned row.

Usage: python3 scripts/backlinks.py "example.co.il" --limit 20
"""
import argparse
from dataforseo_api import api_post, format_count, get_result, print_backlinks_list


def main():
    parser = argparse.ArgumentParser(description="Backlinks analysis (paid)")
    parser.add_argument("target", help="Target domain, without https:// or www.")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max rows (max 1000)")
    args = parser.parse_args()

    target = args.target.split("://")[-1].removeprefix("www.").strip("/")
    data = [{"target": target, "limit": args.limit, "order_by": ["rank,desc"]}]
    response = api_post("backlinks/backlinks/live", data)
    results = get_result(response)

    print(f"target: {target}")
    if not results:
        print("No results found")
        return
    result = results[0]
    print(f"total_backlinks: {format_count(result.get('total_count'))}")
    print_backlinks_list((result.get("items") or [])[:args.limit])


if __name__ == "__main__":
    main()
