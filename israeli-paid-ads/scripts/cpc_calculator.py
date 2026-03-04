#!/usr/bin/env python3
"""Calculate Israeli PPC campaign budgets and estimates.

Provides CPC benchmarks by vertical and estimates campaign costs
for the Israeli market.

Usage:
    python cpc_calculator.py --vertical ecommerce --budget 5000 --cpc 5
    python cpc_calculator.py --benchmarks
    python cpc_calculator.py --help
"""

import argparse

# Israeli CPC benchmarks by vertical (NIS)
CPC_BENCHMARKS = {
    "legal": {"min": 15, "max": 40, "avg": 25, "name_he": "משפטי"},
    "insurance": {"min": 10, "max": 30, "avg": 18, "name_he": "ביטוח"},
    "real-estate": {"min": 8, "max": 25, "avg": 15, "name_he": "נדל\"ן"},
    "finance": {"min": 10, "max": 35, "avg": 20, "name_he": "פיננסים"},
    "ecommerce": {"min": 2, "max": 8, "avg": 4, "name_he": "מסחר אלקטרוני"},
    "saas": {"min": 5, "max": 20, "avg": 12, "name_he": "SaaS"},
    "education": {"min": 3, "max": 12, "avg": 7, "name_he": "חינוך"},
    "health": {"min": 5, "max": 18, "avg": 10, "name_he": "בריאות"},
    "travel": {"min": 3, "max": 15, "avg": 8, "name_he": "תיירות"},
    "food": {"min": 2, "max": 6, "avg": 3, "name_he": "מזון"},
}

VAT_RATE = 0.17

def show_benchmarks():
    print("Israeli Google Ads CPC Benchmarks (NIS)")
    print("=" * 55)
    print(f"{'Vertical':<20} {'Min':<8} {'Avg':<8} {'Max':<8} {'Hebrew'}")
    print("-" * 55)
    for vertical, data in sorted(CPC_BENCHMARKS.items(), key=lambda x: x[1]["avg"], reverse=True):
        print(f"{vertical:<20} {data['min']:<8} {data['avg']:<8} {data['max']:<8} {data['name_he']}")

def calculate_campaign(vertical, budget, cpc=None):
    if vertical not in CPC_BENCHMARKS:
        print(f"Unknown vertical: {vertical}")
        return

    bench = CPC_BENCHMARKS[vertical]
    if cpc is None:
        cpc = bench["avg"]

    budget_ex_vat = budget / (1 + VAT_RATE)
    clicks = int(budget_ex_vat / cpc)

    print(f"\nCampaign Estimate: {bench['name_he']} ({vertical})")
    print("=" * 40)
    print(f"Monthly budget: {budget:,.0f} NIS (inc. VAT)")
    print(f"Budget ex-VAT: {budget_ex_vat:,.0f} NIS")
    print(f"CPC: {cpc:.1f} NIS")
    print(f"Estimated clicks: {clicks:,}")

    for conv_rate in [1, 2, 3, 5]:
        conversions = int(clicks * conv_rate / 100)
        cpa = budget / conversions if conversions > 0 else 0
        print(f"  At {conv_rate}% CVR: {conversions} conversions (CPA: {cpa:.0f} NIS)")

def main():
    parser = argparse.ArgumentParser(description="Israeli PPC campaign calculator")
    parser.add_argument("--benchmarks", action="store_true", help="Show CPC benchmarks")
    parser.add_argument("--vertical", choices=list(CPC_BENCHMARKS.keys()))
    parser.add_argument("--budget", type=float, help="Monthly budget in NIS")
    parser.add_argument("--cpc", type=float, help="Custom CPC (default: vertical average)")
    args = parser.parse_args()

    if args.benchmarks:
        show_benchmarks()
    elif args.vertical and args.budget:
        calculate_campaign(args.vertical, args.budget, args.cpc)
    else:
        show_benchmarks()

if __name__ == "__main__":
    main()
