#!/usr/bin/env python3
"""Plan content calendar for Israeli market.

Generates a content calendar with Jewish holidays,
Israeli national days, and optimal posting schedule.

Usage:
    python content_planner.py --month 9 --year 2026
    python content_planner.py --help

Note: holiday dates are hardcoded per year. 2025 and 2026 are included.
Extend JEWISH_HOLIDAYS for future years (Hebrew-calendar dates shift every
Gregorian year, so they cannot be computed without a Hebrew-calendar library).
"""

import argparse
from datetime import datetime, timedelta

JEWISH_HOLIDAYS_BY_YEAR = {
    2025: [
        ("2025-03-14", "פורים", "Purim"),
        ("2025-04-13", "פסח", "Pesach"),
        ("2025-04-25", "יום הזיכרון", "Yom HaZikaron"),
        ("2025-04-26", "יום העצמאות", "Yom Ha'atzmaut"),
        ("2025-06-02", "שבועות", "Shavuot"),
        ("2025-09-23", "ראש השנה", "Rosh Hashana"),
        ("2025-10-02", "יום כיפור", "Yom Kippur"),
        ("2025-10-07", "סוכות", "Sukkot"),
        ("2025-12-15", "חנוכה", "Hanukkah"),
    ],
    2026: [
        ("2026-03-03", "פורים", "Purim"),
        ("2026-04-02", "פסח", "Pesach"),
        ("2026-04-21", "יום הזיכרון", "Yom HaZikaron"),
        ("2026-04-22", "יום העצמאות", "Yom Ha'atzmaut"),
        ("2026-05-22", "שבועות", "Shavuot"),
        ("2026-09-12", "ראש השנה", "Rosh Hashana"),
        ("2026-09-21", "יום כיפור", "Yom Kippur"),
        ("2026-09-26", "סוכות", "Sukkot"),
        ("2026-12-05", "חנוכה", "Hanukkah"),
    ],
}

NO_COMMERCIAL_DAYS = ["יום כיפור", "יום הזיכרון"]

BEST_POSTING_TIMES = {
    "morning": "09:00-10:00",
    "lunch": "12:00-13:00",
    "evening": "19:00-21:00",
}

def main():
    parser = argparse.ArgumentParser(description="Israeli content calendar planner")
    parser.add_argument("--month", type=int, required=True, help="Month (1-12)")
    parser.add_argument("--year", type=int, default=2026, help="Year")
    args = parser.parse_args()

    print(f"Content Calendar: {args.month}/{args.year}")
    print("=" * 50)

    holidays_for_year = JEWISH_HOLIDAYS_BY_YEAR.get(args.year)
    if holidays_for_year is None:
        print(f"\nNote: no holiday data for {args.year}. "
              f"Available years: {', '.join(str(y) for y in sorted(JEWISH_HOLIDAYS_BY_YEAR))}. "
              "Extend JEWISH_HOLIDAYS_BY_YEAR with verified Hebrew-calendar dates.")
        holidays_for_year = []

    holidays_in_month = [
        (d, h, e) for d, h, e in holidays_for_year
        if datetime.strptime(d, "%Y-%m-%d").month == args.month
    ]

    if holidays_in_month:
        print("\nHolidays this month:")
        for date, he_name, en_name in holidays_in_month:
            no_ads = " [NO COMMERCIAL CONTENT]" if he_name in NO_COMMERCIAL_DAYS else ""
            print(f"  {date}: {he_name} ({en_name}){no_ads}")

    print(f"\nBest posting times (Israel, Sun-Thu):")
    for period, time in BEST_POSTING_TIMES.items():
        print(f"  {period}: {time}")

    print("\nWeekly rhythm:")
    print("  Sunday: New week kickoff content")
    print("  Mon-Wed: Core content (articles, guides)")
    print("  Thursday: Community engagement")
    print("  Friday: Light/Shabbat-related content (before 14:00)")
    print("  Saturday: No posting (Shabbat)")

if __name__ == "__main__":
    main()
