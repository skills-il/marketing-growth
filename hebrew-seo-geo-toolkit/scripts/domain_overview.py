#!/usr/bin/env python3
"""
Organic footprint of a domain (DataForSEO Labs, paid).
Endpoint: dataforseo_labs/google/ranked_keywords/live

Defaults to Israel (2376) and Hebrew (he). Labs holds only Hebrew and Arabic
data for Israel, so English for Israel is refused before any call is made.

Usage: python3 scripts/domain_overview.py "example.co.il"
"""
import argparse
from dataforseo_api import add_market_args, api_post, check_labs_market, format_count, get_result


def main():
    parser = argparse.ArgumentParser(description="Domain overview (paid)")
    parser.add_argument("domain", help="Target domain, without https:// or www.")
    add_market_args(parser)
    args = parser.parse_args()
    check_labs_market(args.location, args.language)

    domain = args.domain.split("://")[-1].removeprefix("www.").strip("/")
    data = [{
        "target": domain,
        "location_code": args.location,
        "language_code": args.language,
        "limit": 1,  # only the summary metrics are needed
    }]
    response = api_post("dataforseo_labs/google/ranked_keywords/live", data)
    results = get_result(response)

    print(f"domain: {domain}")
    print(f"location: {args.location} language: {args.language}")
    if not results:
        print("No results found")
        return
    for result in results:
        organic = (result.get("metrics") or {}).get("organic") or {}
        if not organic:
            continue
        print(f"organic_keywords: {format_count(organic.get('count', 0))}")
        print(f"estimated_organic_traffic: {format_count(organic.get('etv', 0))}")
        print(f"top_3_positions: {(organic.get('pos_1') or 0) + (organic.get('pos_2_3') or 0)}")


if __name__ == "__main__":
    main()
