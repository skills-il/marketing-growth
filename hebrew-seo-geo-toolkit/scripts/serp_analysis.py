#!/usr/bin/env python3
"""
Top Google organic results for a keyword (DataForSEO, paid).
Endpoint: serp/google/organic/live/advanced

Defaults to Israel (2376) and Hebrew (he). Billed per SERP page of up to 10
results, so --depth 20 is billed as two pages.

Usage: python3 scripts/serp_analysis.py "רואה חשבון בתל אביב" --depth 10
"""
import argparse
from dataforseo_api import add_market_args, api_post, format_count, get_result, print_serp_list


def main():
    parser = argparse.ArgumentParser(description="SERP analysis (paid)")
    parser.add_argument("keyword", help="Search keyword")
    add_market_args(parser)
    parser.add_argument("--depth", "-d", type=int, default=10,
                        help="Number of results, max 200 (default 10 = one billed page)")
    args = parser.parse_args()

    data = [{
        "keyword": args.keyword,
        "location_code": args.location,
        "language_code": args.language,
        "depth": args.depth,
    }]
    response = api_post("serp/google/organic/live/advanced", data)
    results = get_result(response)

    print(f"keyword: {args.keyword}")
    print(f"location: {args.location} language: {args.language}")
    if not results:
        print("No results found")
        return
    result = results[0]
    print(f"total_results: {format_count(result.get('se_results_count'))}")
    print_serp_list(result.get("items") or [])


if __name__ == "__main__":
    main()
