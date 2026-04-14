#!/usr/bin/env python3
"""Emit a ready-to-pipe JSON payload for `gws forms batchUpdate --json`.

Usage:
  python3 scripts/build_batchupdate_payload.py --template nps
  python3 scripts/build_batchupdate_payload.py --template csat
  python3 scripts/build_batchupdate_payload.py --template ces
  python3 scripts/build_batchupdate_payload.py --template event-feedback
  python3 scripts/build_batchupdate_payload.py --template product-discovery
  python3 scripts/build_batchupdate_payload.py --template market-research

The output is pretty-printed JSON to stdout. Pipe it straight to gws:

  python3 scripts/build_batchupdate_payload.py --template nps \
    | xargs -0 -I{} gws forms batchUpdate --params formId=<FORM_ID> --json '{}'
"""

import argparse
import json
import sys


def scale(title, low, high, low_label, high_label, required=True):
    return {
        "title": title,
        "questionItem": {
            "question": {
                "required": required,
                "scaleQuestion": {
                    "low": low,
                    "high": high,
                    "lowLabel": low_label,
                    "highLabel": high_label,
                },
            }
        },
    }


def paragraph(title, required=False):
    return {
        "title": title,
        "questionItem": {
            "question": {
                "required": required,
                "textQuestion": {"paragraph": True},
            }
        },
    }


def short_text(title, required=False):
    return {
        "title": title,
        "questionItem": {
            "question": {
                "required": required,
                "textQuestion": {},
            }
        },
    }


def choice(title, options, required=True, choice_type="RADIO"):
    return {
        "title": title,
        "questionItem": {
            "question": {
                "required": required,
                "choiceQuestion": {
                    "type": choice_type,
                    "options": [{"value": opt} for opt in options],
                },
            }
        },
    }


def nps():
    return [
        scale(
            "עד כמה סביר שתמליצו עלינו לחבר או קולגה?",
            0, 10,
            "בכלל לא סביר", "בהחלט סביר",
            required=True,
        ),
        paragraph("מה הסיבה המרכזית לציון שנתתם?", required=False),
    ]


def csat():
    return [
        scale(
            "עד כמה הייתם מרוצים מהחוויה?",
            1, 5,
            "ממש לא מרוצים", "ממש מרוצים",
            required=True,
        ),
        choice(
            "מה בלט לכם?",
            ["המהירות", "היחס האישי", "הפתרון שקיבלתי", "אף אחד מהאפשרויות", "משהו אחר"],
            required=False,
        ),
        paragraph("משהו שנוכל לשפר?", required=False),
    ]


def ces():
    return [
        scale(
            "עד כמה היה לכם קל להשלים את הפעולה?",
            1, 7,
            "קל מאוד", "קשה מאוד",
            required=True,
        ),
        paragraph("אם משהו היה מסורבל, מה זה היה?", required=False),
    ]


def event_feedback():
    return [
        scale(
            "עד כמה האירוע ענה על הציפיות שלכם?",
            1, 5,
            "בכלל לא", "לגמרי",
            required=True,
        ),
        choice(
            "מאיזה חלק באירוע הפקתם הכי הרבה?",
            ["החלק הראשון", "החלק השני", "החלק השלישי", "אף אחד במיוחד"],
            required=True,
        ),
        paragraph("מה היה יכול להפוך את האירוע הבא לטוב יותר?", required=False),
        choice("האם תחזרו למפגש הבא?", ["כן", "לא", "עוד לא יודע/ת"], required=True),
    ]


def product_discovery():
    return [
        paragraph(
            "ספרו לנו על פעם אחרונה שנתקלתם בבעיה שאנחנו חוקרים. מה קרה?",
            required=True,
        ),
        paragraph("מה ניסיתם לעשות כדי לפתור את זה?", required=True),
        paragraph("מה היה הכי מתסכל בתהליך?", required=False),
        paragraph("אם היה פתרון קסם, איך הוא היה נראה בעיניכם?", required=False),
    ]


def market_research():
    return [
        choice(
            "מה הכי מתאר אתכם?",
            ["עצמאי/ת", "שכיר/ה", "בעל/ת עסק קטן", "מנהל/ת בחברה", "אחר"],
            required=True,
        ),
        paragraph(
            "ספרו לנו על הבעיה שאתם הכי רוצים שמישהו יפתור עבורכם בתחום הזה",
            required=True,
        ),
        scale(
            "כמה הבעיה הזו משפיעה עליכם יום-יום?",
            1, 5,
            "כמעט בכלל לא", "מאוד, כל יום",
            required=True,
        ),
        choice(
            "אם היה קיים פתרון שפותר את זה, כמה הייתם מוכנים לשלם עליו בחודש?",
            ["לא הייתי משלם/ת", "עד 20 ₪", "20–50 ₪", "50–100 ₪", "100 ₪ ומעלה"],
            required=False,
        ),
    ]


TEMPLATES = {
    "nps": nps,
    "csat": csat,
    "ces": ces,
    "event-feedback": event_feedback,
    "product-discovery": product_discovery,
    "market-research": market_research,
}


def build_payload(template_name):
    items = TEMPLATES[template_name]()
    requests = [
        {"createItem": {"item": item, "location": {"index": i}}}
        for i, item in enumerate(items)
    ]
    return {"requests": requests}


def main():
    parser = argparse.ArgumentParser(
        description="Build a gws forms batchUpdate payload for a Hebrew survey template"
    )
    parser.add_argument(
        "--template",
        required=True,
        choices=sorted(TEMPLATES.keys()),
        help="Template name",
    )
    args = parser.parse_args()

    payload = build_payload(args.template)
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
