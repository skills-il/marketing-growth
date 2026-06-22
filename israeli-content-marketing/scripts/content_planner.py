#!/usr/bin/env python3
"""Plan content calendar for Israeli market.

Generates a content calendar with Jewish holidays,
Israeli national/memorial days, and an optimal posting schedule.

Usage:
    python content_planner.py --month 9 --year 2026
    python content_planner.py --help

Note: holiday dates are hardcoded per year. 2025, 2026, and 2027 are included.
Extend JEWISH_HOLIDAYS_BY_YEAR for future years (Hebrew-calendar dates shift every
Gregorian year, so they cannot be computed without a Hebrew-calendar library).
Verify any new rows against hebcal.com before encoding them.

Each row is (first_day, hebrew_name, english_name, duration_days). Multi-day
holidays (Pesach, Sukkot, Hanukkah, Rosh Hashana) carry their real span so the
planner blocks the whole low-engagement window, not just day one.
"""

import argparse
from datetime import datetime, timedelta

# (first_day, hebrew, english, duration_days)
JEWISH_HOLIDAYS_BY_YEAR = {
    2025: [
        ("2025-03-14", "פורים", "Purim", 1),
        ("2025-04-13", "פסח", "Pesach", 7),
        ("2025-04-24", "יום השואה", "Yom HaShoah", 1),
        ("2025-04-30", "יום הזיכרון", "Yom HaZikaron", 1),
        ("2025-05-01", "יום העצמאות", "Yom Ha'atzmaut", 1),
        ("2025-06-02", "שבועות", "Shavuot", 1),
        ("2025-09-23", "ראש השנה", "Rosh Hashana", 2),
        ("2025-10-02", "יום כיפור", "Yom Kippur", 1),
        ("2025-10-07", "סוכות", "Sukkot", 7),
        ("2025-12-15", "חנוכה", "Hanukkah", 8),
    ],
    2026: [
        ("2026-03-03", "פורים", "Purim", 1),
        ("2026-04-02", "פסח", "Pesach", 7),
        ("2026-04-14", "יום השואה", "Yom HaShoah", 1),
        ("2026-04-21", "יום הזיכרון", "Yom HaZikaron", 1),
        ("2026-04-22", "יום העצמאות", "Yom Ha'atzmaut", 1),
        ("2026-05-22", "שבועות", "Shavuot", 1),
        ("2026-09-12", "ראש השנה", "Rosh Hashana", 2),
        ("2026-09-21", "יום כיפור", "Yom Kippur", 1),
        ("2026-09-26", "סוכות", "Sukkot", 7),
        ("2026-12-05", "חנוכה", "Hanukkah", 8),
    ],
    2027: [
        ("2027-03-23", "פורים", "Purim", 1),
        ("2027-04-22", "פסח", "Pesach", 7),
        ("2027-05-04", "יום השואה", "Yom HaShoah", 1),
        ("2027-05-11", "יום הזיכרון", "Yom HaZikaron", 1),
        ("2027-05-12", "יום העצמאות", "Yom Ha'atzmaut", 1),
        ("2027-06-11", "שבועות", "Shavuot", 1),
        ("2027-10-02", "ראש השנה", "Rosh Hashana", 2),
        ("2027-10-11", "יום כיפור", "Yom Kippur", 1),
        ("2027-10-16", "סוכות", "Sukkot", 7),
        ("2027-12-25", "חנוכה", "Hanukkah", 8),
    ],
}

# Absolute no-commercial / no-advertising solemn days: Yom Kippur, plus the two
# siren days (advertising suspended, venues closed) Yom HaShoah and Yom HaZikaron.
NO_COMMERCIAL_DAYS = ["יום כיפור", "יום השואה", "יום הזיכרון"]

BEST_POSTING_TIMES = {
    "morning": "09:00-10:00",
    "lunch": "12:00-13:00",
    "evening": "19:00-21:00",
}


def window(first_day, duration):
    start = datetime.strptime(first_day, "%Y-%m-%d")
    if duration <= 1:
        return first_day
    end = start + timedelta(days=duration - 1)
    return f"{first_day} to {end.strftime('%Y-%m-%d')}"


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

    # A multi-day holiday that STARTS in a prior month but runs into this month
    # still matters, so include any holiday whose window touches the month.
    holidays_in_month = []
    for d, he, en, days in holidays_for_year:
        start = datetime.strptime(d, "%Y-%m-%d")
        end = start + timedelta(days=days - 1)
        if start.month == args.month or end.month == args.month:
            holidays_in_month.append((d, he, en, days))

    if holidays_in_month:
        print("\nHolidays this month (avoid-window):")
        for d, he_name, en_name, days in holidays_in_month:
            no_ads = " [NO COMMERCIAL CONTENT]" if he_name in NO_COMMERCIAL_DAYS else ""
            print(f"  {window(d, days)}: {he_name} ({en_name}){no_ads}")

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
