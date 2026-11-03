#!/usr/bin/env python3
"""
Competitor keyword gap (DataForSEO Labs, paid).
Endpoint: dataforseo_labs/google/domain_intersection/live

With intersections=false the API returns keywords where target1 ranks and
target2 does not, with SERP data for target1 only. So the COMPETITOR goes in
target1 and YOUR domain in target2, and the competitor's position is read from
first_domain_serp_element. Defaults to Israel (2376) and Hebrew (he).

Usage: python3 scripts/competitor_gap.py "my-site.co.il" "competitor.co.il" --limit 50
"""
import argparse
from dataforseo_api import add_market_args, api_post, check_labs_market, format_count, get_result


def bare(domain: str) -> str:
    return domain.split("://")[-1].removeprefix("www.").strip("/")


def main():
    parser = argparse.ArgumentParser(description="Competitor keyword gap (paid)")
    parser.add_argument("my_domain", help="Your domain, without https:// or www.")
    parser.add_argument("competitor_domain", help="Competitor domain, without https:// or www.")
    add_market_args(parser)
    parser.add_argument("--limit", "-l", type=int, default=50, help="Max items, 1-1000 (default 50)")
    args = parser.parse_args()
    check_labs_market(args.location, args.language)

    mine, competitor = bare(args.my_domain), bare(args.competitor_domain)
    data = [{
        "target1": competitor,   # ranks
        "target2": mine,         # does not rank
        "location_code": args.location,
        "language_code": args.language,
        "intersections": False,
        "limit": max(1, min(args.limit, 1000)),
    }]
    response = api_post("dataforseo_labs/google/domain_intersection/live", data)
    results = get_result(response)

    print(f"my_domain: {mine}")
    print(f"competitor_domain: {competitor}")
    print(f"location: {args.location} language: {args.language}")
    items = [it for result in results for it in (result.get("items") or [])]
    if not items:
        print("No keyword gaps found")
        return
    print(f"keyword_gaps[{len(items)}]{{keyword,volume,difficulty_0_100,competitor_position}}:")
    for item in items:
        kd = item.get("keyword_data") or {}
        volume = format_count((kd.get("keyword_info") or {}).get("search_volume"))
        difficulty = (kd.get("keyword_properties") or {}).get("keyword_difficulty", "N/A")
        el = item.get("first_domain_serp_element") or {}
        pos = el.get("rank_absolute", "N/A")
        print(f"  {kd.get('keyword', 'N/A')},{volume},{difficulty},{pos}")


if __name__ == "__main__":
    main()
