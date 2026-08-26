#!/usr/bin/env python3
"""Emit a ready-to-pipe JSON payload for `gws forms forms batchUpdate --json`.

Usage:
  python3 scripts/build_batchupdate_payload.py --template nps
  python3 scripts/build_batchupdate_payload.py --template csat
  python3 scripts/build_batchupdate_payload.py --template ces
  python3 scripts/build_batchupdate_payload.py --template event-feedback
  python3 scripts/build_batchupdate_payload.py --template product-discovery
  python3 scripts/build_batchupdate_payload.py --template market-research

The output is pretty-printed JSON to stdout. Pipe it straight to gws:

  python3 scripts/build_batchupdate_payload.py --template nps \
    | xargs -0 -I{} gws forms forms batchUpdate \
        --params '{"formId": "<FORM_ID>"}' --json '{}'

    Note the doubled "forms": the gws command shape is
    `gws <service> <resource> [sub-resource] <method>`, and both the service
    and the resource here are called forms. --params takes a JSON object, not
    key=value.

    Remember that a form created through the API after 2026-06-30 starts
    UNPUBLISHED and accepts no responses until you call
    `gws forms forms setPublishSettings`. See SKILL.md Step 5.
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
            ["המהירות", "היחס האישי", "הפתרון שקיבלתי", "משהו אחר", "כלום לא בלט במיוחד"],
            choice_type="CHECKBOX",
            required=False,
        ),
        paragraph("משהו שנוכל לשפר?", required=False),
    ]


def ces(task=None):
    # CES 2.0 attributes the effort to the ORGANISATION ("the company made it
    # easy for me"), which is what makes the score actionable against
    # something you control. "It was easy for me" measures self-efficacy and
    # is not comparable to CES benchmarks.
    action = task or "את מה שרצית לעשות"
    return [
        scale(
            f"הצוות שלנו הקל עליכם להשלים {action}",
            1, 7,
            "כלל לא מסכים/ה", "מסכים/ה לחלוטין",
            required=True,
        ),
        paragraph("אם משהו היה מסורבל, מה זה היה?", required=False),
    ]


def event_feedback(sessions=None):
    if not sessions:
        raise TemplateInputError(
            "event-feedback needs --sessions: a comma-separated list of the "
            "session titles as they appeared on the agenda, e.g. "
            "--sessions 'פתיחה,הרצאת אורח,פאנל'. Without them the question "
            "reads 'the first part / the second part', which respondents "
            "cannot map to anything and which yields uninterpretable answers."
        )
    options = list(sessions) + ["אף אחד במיוחד"]
    return [
        scale(
            "עד כמה האירוע ענה על הציפיות שלכם?",
            1, 5,
            "בכלל לא", "לגמרי",
            required=True,
        ),
        choice(
            "מאיזה חלק באירוע הפקתם הכי הרבה?",
            options,
            required=True,
        ),
        paragraph("מה היה יכול להפוך את האירוע הבא לטוב יותר?", required=False),
        choice("האם תחזרו למפגש הבא?", ["כן", "לא", "עוד לא יודע/ת"], required=True),
    ]


def product_discovery(topic=None):
    if not topic:
        raise TemplateInputError(
            "product-discovery needs --topic: the problem area in the "
            "respondent's own words, e.g. --topic 'ניהול הוצאות בעסק קטן'. "
            "Without it the first question asks about 'the problem we are "
            "researching', which names nothing."
        )
    return [
        paragraph(
            f"ספרו לנו על הפעם האחרונה שנתקלתם ב{topic}. מה קרה?",
            required=True,
        ),
        paragraph("מה ניסיתם לעשות כדי לפתור את זה?", required=False),
        paragraph("מה היה הכי מתסכל בתהליך?", required=False),
        paragraph("אם היה פתרון קסם, איך הוא היה נראה בעיניכם?", required=False),
    ]


def market_research():
    # The segment question is LAST and optional on purpose. SKILL.md Step 8
    # names "segment question + free text on a small list" as the canonical
    # way a nominally anonymous survey re-identifies people, so leading with
    # it, required, would make the default shape of this template violate the
    # skill's own privacy rule. Bands are also non-overlapping: shared
    # boundary values (a respondent whose answer is exactly 50) produce a
    # distribution that is uninterpretable exactly where pricing gets decided.
    return [
        paragraph(
            "יש משהו בתחום הזה שמציק לכם? אם כן, ספרו לנו מה",
            required=False,
        ),
        scale(
            "כמה זה משפיע עליכם יום-יום?",
            1, 5,
            "כמעט בכלל לא", "משפיע מאוד",
            required=True,
        ),
        choice(
            "אם היה קיים פתרון שפותר את זה, כמה הייתם מוכנים לשלם עליו בחודש?",
            ["לא הייתי משלם/ת", "עד 20 ₪", "21-50 ₪", "51-100 ₪", "מעל 100 ₪"],
            required=False,
        ),
        choice(
            "מה הכי מתאר אתכם?",
            ["עצמאי/ת", "שכיר/ה", "בעל/ת עסק קטן", "מנהל/ת בחברה", "אחר"],
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


CONSENT_ITEM_TITLE = "אני מאשר/ת שאפשר ליצור איתי קשר בעקבות התשובות"

ANON_INTRO = "התשובות בסקר הזה אנונימיות ולא נאספים בו פרטים מזהים."


def consent_item():
    """A leading required consent item, for identifiable surveys only.

    SKILL.md Step 8 requires this to sit BEFORE any identifying or segmenting
    field, and never pre-ticked. Emitting it at index 0 is the only way that
    ordering rule survives contact with the payload builder.
    """
    return choice(CONSENT_ITEM_TITLE, ["מאשר/ת"], required=True)


class TemplateInputError(ValueError):
    """A template was asked to emit respondent-facing text it has no value for."""


def build_payload(template_name, topic=None, sessions=None, task=None,
                  intro=None, notice=None):
    builder = TEMPLATES[template_name]
    if template_name == "product-discovery":
        items = builder(topic=topic)
    elif template_name == "event-feedback":
        items = builder(sessions=sessions)
    elif template_name == "ces":
        items = builder(task=task)
    else:
        items = builder()

    if intro == "identified":
        # Consent first, everything else shifts down by one.
        items = [consent_item()] + items

    requests = []

    # The form description is the only place the anonymity line or the
    # Amendment 13 notice can live, and `create` disallows it, so it has to be
    # set here. Without this the notice SKILL.md Step 8 requires has no
    # delivery path at all.
    description = notice or (ANON_INTRO if intro == "anonymous" else None)
    if description:
        requests.append({
            "updateFormInfo": {
                "info": {"description": description},
                "updateMask": "description",
            }
        })

    requests += [
        {"createItem": {"item": item, "location": {"index": i}}}
        for i, item in enumerate(items)
    ]
    return {"requests": requests}


def main():
    parser = argparse.ArgumentParser(
        description="Build a gws forms forms batchUpdate payload for a Hebrew survey template"
    )
    parser.add_argument(
        "--template",
        required=True,
        choices=sorted(TEMPLATES.keys()),
        help="Template name",
    )
    parser.add_argument(
        "--topic",
        help="product-discovery only: the problem area in the respondent's own "
             "words, e.g. 'ניהול הוצאות בעסק קטן'. Required for that template.",
    )
    parser.add_argument(
        "--sessions",
        help="event-feedback only: comma-separated session titles exactly as "
             "they appeared on the agenda. Required for that template.",
    )
    parser.add_argument(
        "--task",
        help="ces only: the task being rated, e.g. 'את ההרשמה'. Defaults to a "
             "generic phrasing, but naming the task makes the score usable.",
    )
    parser.add_argument(
        "--intro",
        choices=["anonymous", "identified"],
        help="Set the form description. 'anonymous' writes the anonymity line. "
             "'identified' additionally prepends a required consent item at "
             "index 0, per SKILL.md Step 8. Use --notice to supply the fuller "
             "Amendment 13 notice text for identifiable surveys.",
    )
    parser.add_argument(
        "--notice",
        help="Explicit form-description text. Overrides --intro's default line. "
             "For identifiable surveys this is where the Amendment 13 notice "
             "goes: who the controller is and how to reach them, what happens "
             "if the respondent refuses, and their right to access and correct.",
    )
    args = parser.parse_args()

    sessions = None
    if args.sessions:
        sessions = [t.strip() for t in args.sessions.split(",") if t.strip()]

    try:
        payload = build_payload(
            args.template,
            topic=args.topic,
            sessions=sessions,
            task=args.task,
            intro=args.intro,
            notice=args.notice,
        )
    except TemplateInputError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
