#!/usr/bin/env python3
"""Generate optimal posting schedule for Israeli social media.

Creates a weekly posting calendar optimized for Israeli audience
engagement patterns across Facebook, Instagram, TikTok, and LinkedIn.

Usage:
    python posting_scheduler.py --platform facebook
    python posting_scheduler.py --all
    python posting_scheduler.py --help
"""

import argparse

PLATFORMS = {
    "facebook": {
        "name_he": "פייסבוק",
        "best_times": ["09:00", "12:30", "19:00"],
        "best_days": ["Sunday", "Tuesday", "Wednesday"],
        "post_types": ["Group post", "Page post", "Story", "Reel"],
        "frequency": "5-7 posts/week",
    },
    "instagram": {
        "name_he": "אינסטגרם",
        "best_times": ["08:00", "12:00", "20:00"],
        "best_days": ["Sunday", "Monday", "Wednesday"],
        "post_types": ["Reel", "Carousel", "Story", "Post"],
        "frequency": "4-7 posts/week + daily stories",
    },
    "tiktok": {
        "name_he": "טיקטוק",
        "best_times": ["12:00", "17:00", "21:00"],
        "best_days": ["Sunday", "Tuesday", "Thursday"],
        "post_types": ["Short video (15-60s)", "Duet", "Stitch"],
        "frequency": "3-5 videos/week",
    },
    "linkedin": {
        "name_he": "לינקדאין",
        "best_times": ["08:30", "12:00", "17:30"],
        "best_days": ["Sunday", "Tuesday", "Wednesday"],
        "post_types": ["Article", "Text post", "Carousel", "Poll"],
        "frequency": "3-5 posts/week",
    },
}

WEEK_DAYS_HE = {
    "Sunday": "ראשון", "Monday": "שני", "Tuesday": "שלישי",
    "Wednesday": "רביעי", "Thursday": "חמישי", "Friday": "שישי", "Saturday": "שבת",
}

def show_platform(name):
    p = PLATFORMS[name]
    print(f"\n{p['name_he']} ({name})")
    print("=" * 40)
    print(f"Frequency: {p['frequency']}")
    print(f"Best times: {', '.join(p['best_times'])}")
    print(f"Best days: {', '.join(f'{d} ({WEEK_DAYS_HE[d]})' for d in p['best_days'])}")
    print(f"Content types: {', '.join(p['post_types'])}")
    print("\nNote: No posting on Shabbat (Friday afternoon - Saturday night)")
    print("      Avoid posting on Yom Kippur and Yom HaZikaron")

def main():
    parser = argparse.ArgumentParser(description="Israeli social media posting scheduler")
    parser.add_argument("--platform", choices=list(PLATFORMS.keys()))
    parser.add_argument("--all", action="store_true", help="Show all platforms")
    args = parser.parse_args()

    if args.all:
        for name in PLATFORMS:
            show_platform(name)
    elif args.platform:
        show_platform(args.platform)
    else:
        for name in PLATFORMS:
            show_platform(name)

if __name__ == "__main__":
    main()
