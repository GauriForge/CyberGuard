
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session,
    request,
    abort,
)

labs_bp = Blueprint("labs", __name__)


# --------------------------------------------------
# GENERAL PRACTICE LEVELS
# --------------------------------------------------

PRACTICE_LEVELS = [
    {
        "id": "beginner",
        "name": "Beginner Practice",
        "title": "Beginner Practice",
        "difficulty": "Beginner",
        "description": (
            "Practice basic cybersecurity awareness and "
            "defensive decisions."
        ),
        "duration": "15–20 minutes",
    },
    {
        "id": "intermediate",
        "name": "Intermediate Practice",
        "title": "Intermediate Practice",
        "difficulty": "Intermediate",
        "description": (
            "Apply security knowledge to scenarios involving "
            "different threats."
        ),
        "duration": "20–30 minutes",
    },
    {
        "id": "advanced",
        "name": "Advanced Practice",
        "title": "Advanced Practice",
        "difficulty": "Advanced",
        "description": (
            "Analyze complex scenarios and select appropriate "
            "security controls."
        ),
        "duration": "30–40 minutes",
    },
    {
        "id": "high-level",
        "name": "High-Level Practice",
        "title": "High-Level Practice",
        "difficulty": "High Level",
        "description": (
            "Make security decisions across multi-stage "
            "simulated incidents."
        ),
        "duration": "40–45 minutes",
    },
]


# --------------------------------------------------
# EXISTING GUIDED LABS
# --------------------------------------------------

INTERACTIVE_LABS = [
    {
        "id": "password-security",
        "title": "Password Security Lab",
        "category": "Authentication",
        "difficulty": "Beginner",
        "description": (
            "Evaluate a sample password using basic security checks."
        ),
        "duration": "10 minutes",
    },
    {
        "id": "phishing-awareness",
        "title": "Phishing Awareness Lab",
        "category": "Social Engineering",
        "difficulty": "Beginner",
        "description": (
            "Identify warning signs in a suspicious message."
        ),
        "duration": "15 minutes",
    },
    {
        "id": "network-security",
        "title": "Network Security Lab",
        "category": "Network Security",
        "difficulty": "Intermediate",
        "description": (
            "Choose suitable defensive controls for a network scenario."
        ),
        "duration": "15 minutes",
    },
    {
        "id": "web-security",
        "title": "Web Application Security Lab",
        "category": "Web Security",
        "difficulty": "Intermediate",
        "description": (
            "Identify secure practices for protecting web applications."
        ),
        "duration": "20 minutes",
    },
    {
        "id": "incident-response",
        "title": "Incident Response Lab",
        "category": "Incident Management",
        "difficulty": "Intermediate",
        "description": (
            "Choose appropriate actions when a security incident "
            "is reported."
        ),
        "duration": "15 minutes",
    },
]


LAB_ACTIVITIES = {
    "password-security": {
        "title": "Password Security",
        "instructions": (
            "Enter a sample password to review its basic characteristics. "
            "Do not enter a real password."
        ),
        "type": "password",
    },
    "phishing-awareness": {
        "title": "Phishing Awareness",
        "instructions": (
            "Review the message and select the safest response."
        ),
        "type": "quiz",
        "scenario": (
            "A message claims your account will be suspended unless "
            "you immediately open an unfamiliar link."
        ),
        "options": [
            "Open the link immediately",
            "Verify the message through the official website",
            "Reply with your account credentials",
            "Forward the message to friends",
        ],
        "correct_answer": (
            "Verify the message through the official website"
        ),
        "explanation": (
            "Access the official website independently and verify "
            "unexpected requests before taking action."
        ),
    },
    "network-security": {
        "title": "Network Security",
        "instructions": (
            "Choose the most appropriate defensive measure."
        ),
        "type": "quiz",
        "scenario": (
            "An organization wants to limit unauthorized access "
            "between its internal network segments."
        ),
        "options": [
            "Disable security updates",
            "Use network segmentation and access controls",
            "Share administrator credentials",
            "Allow unrestricted access to every device",
        ],
        "correct_answer": (
            "Use network segmentation and access controls"
        ),
        "explanation": (
            "Segmentation and access controls limit unnecessary "
            "communication and help contain the impact of a "
            "compromised device."
        ),
    },
    "web-security": {
        "title": "Web Application Security",
        "instructions": "Select the best defensive practice.",
        "type": "quiz",
        "scenario": (
            "A web application uses user input in a database query. "
            "Which practice best helps prevent SQL injection?"
        ),
        "options": [
            "Use parameterized queries",
            "Trust all user input",
            "Expose database errors to visitors",
            "Store database credentials in browser code",
        ],
        "correct_answer": "Use parameterized queries",
        "explanation": (
            "Parameterized queries separate SQL instructions from "
            "supplied values, helping prevent input from altering "
            "query structure."
        ),
    },
    "incident-response": {
        "title": "Incident Response",
        "instructions": "Choose the most appropriate response.",
        "type": "quiz",
        "scenario": (
            "An employee reports a suspicious file on a company computer."
        ),
        "options": [
            "Ignore the report",
            "Share the file publicly",
            "Follow the incident reporting procedure",
            "Delete all relevant logs immediately",
        ],
        "correct_answer": (
            "Follow the incident reporting procedure"
        ),
        "explanation": (
            "Prompt reporting allows authorized responders to assess "
            "the incident and preserve relevant evidence."
        ),
    },
}


# --------------------------------------------------
# DATA ACCESS
# --------------------------------------------------

def _get_attack_modules():
    from routes.attacks import (
        ATTACK_CATEGORIES,
        _get_category,
        _find_attack,
    )
    from data.data_adapter import get_content

    return ATTACK_CATEGORIES, _get_category, _find_attack, get_content


def _get_category_cards():
    """Provide both category name aliases for template compatibility."""
    ATTACK_CATEGORIES, _, _, _ = _get_attack_modules()

    cards = []

    for category in ATTACK_CATEGORIES:
        name = category.get("name") or category.get("title") or "Uncategorized"

        cards.append({
            "id": category["id"],
            "name": name,
            "title": name,
            "description": category.get("description", ""),
            "icon": category.get("icon", "shield"),
        })

    return cards


def _get_attack_record(category_id, attack_id):
    ATTACK_CATEGORIES, _get_category, _find_attack, _ = (
        _get_attack_modules()
    )

    category_info = next(
        (
            item for item in ATTACK_CATEGORIES
            if str(item["id"]) == str(category_id)
        ),
        None,
    )

    if category_info is None:
        return None, None, None

    category, _ = _get_category(category_id)

    if category is None:
        return None, None, None

    subcategory, attack = _find_attack(category, attack_id)

    if attack is None:
        return None, None, None

    return category, subcategory, attack


# --------------------------------------------------
# CONTENT EXTRACTION
# --------------------------------------------------

def _content_items(attack, content_type):
    """
    Return content records from the shared data adapter.

    A content type may be one record, a list of records, or a
    dictionary containing named records.
    """
    _, _, _, get_content = _get_attack_modules()

    content = get_content(attack, content_type)

    if isinstance(content, dict):
        record_fields = {
            "title", "name", "instructions", "scenario",
            "options", "choices", "question", "content",
            "steps", "tasks", "discussion", "expected_outcome",
        }

        if record_fields.intersection(content):
            return [content]

        return [
            value for value in content.values()
            if isinstance(value, dict)
        ]

    if isinstance(content, (list, tuple)):
        return [
            item if isinstance(item, dict) else {"content": str(item)}
            for item in content
            if isinstance(item, (dict, str))
        ]

    if isinstance(content, str) and content.strip():
        return [{"content": content.strip()}]

    return []


def _get_attack_content_records(attack):
    """
    Combine practical labs, simulations, and case studies.

    The data adapter handles aliases such as practical_lab,
    practical_labs, simulation, and case_study.
    """
    records = []
    seen = set()

    for content_type in ("labs", "simulations", "case_studies"):
        for record in _content_items(attack, content_type):
            # Prevent the same source object from being added twice
            # when a data record exposes the same content via aliases.
            signature = (
                content_type,
                str(record.get("id", "")),
                str(record.get("title", "")),
                str(record.get("name", "")),
            )

            if signature in seen:
                continue

            seen.add(signature)
            records.append({
                "content_type": content_type,
                "record": record,
            })

    return records


# --------------------------------------------------
# CONTENT NORMALIZATION
# --------------------------------------------------

def _first_text(data, keys, default=""):
    """Return the first usable text value from a list of field names."""
    for key in keys:
        value = data.get(key)

        if isinstance(value, str) and value.strip():
            return value.strip()

        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return str(value)

    return default


def _as_text_list(value):
    """Convert strings, lists, and dictionaries into readable text items."""
    if isinstance(value, str):
        return [value.strip()] if value.strip() else []

    if isinstance(value, dict):
        result = []

        for key, item in value.items():
            if isinstance(item, dict):
                text = _first_text(
                    item,
                    ("text", "title", "name", "content", "description"),
                )
                if text:
                    result.append(text)
            elif isinstance(item, (str, int, float)):
                result.append(str(item).strip())

        return [item for item in result if item]

    if isinstance(value, (list, tuple)):
        result = []

        for item in value:
            if isinstance(item, dict):
                text = _first_text(
                    item,
                    ("text", "title", "name", "content", "description"),
                )
                if text:
                    result.append(text)
            elif isinstance(item, (str, int, float)):
                text = str(item).strip()
                if text:
                    result.append(text)

        return result

    return []


def _normalize_options(raw_options):
    """Normalize option lists and keyed option dictionaries."""
    if isinstance(raw_options, dict):
        values = list(raw_options.values())
    elif isinstance(raw_options, (list, tuple)):
        values = list(raw_options)
    else:
        return []

    options = []

    for option in values:
        if isinstance(option, dict):
            text = (
                option.get("text")
                or option.get("option")
                or option.get("label")
                or option.get("answer")
            )
        else:
            text = option

        if text is None:
            continue

        text = str(text).strip()

        if text:
            options.append(text)

    return options


def _normalize_correct_answer(item, options):
    """Resolve common answer formats to the matching option text."""
    correct = None

    for key in (
        "correct_answer",
        "correct_option",
        "expected_answer",
        "correct",
        "answer",
    ):
        if key in item and item[key] not in (None, ""):
            correct = item[key]
            break

    if isinstance(correct, bool):
        return ""

    if isinstance(correct, int):
        if 0 <= correct < len(options):
            return options[correct]
        if 1 <= correct <= len(options):
            return options[correct - 1]
        return ""

    if isinstance(correct, dict):
        correct = (
            correct.get("text")
            or correct.get("option")
            or correct.get("label")
            or correct.get("answer")
        )

    if correct is None:
        return ""

    correct = str(correct).strip()

    if not correct:
        return ""

    if len(correct) == 1 and correct.isalpha():
        option_index = ord(correct.upper()) - ord("A")

        if 0 <= option_index < len(options):
            return options[option_index]

    return correct


def _normalize_lab_content(item, attack_title, content_type="labs"):
    """
    Normalize labs, simulations, and case studies into the fields
    already used by practical_labs.html.

    Structured tasks, steps, discussion prompts, and expected outcomes
    are retained as readable text rather than discarded.
    """
    if not isinstance(item, dict):
        item = {"content": str(item)}

    title = _first_text(
        item,
        (
            "title", "name", "lab_title",
            "simulation_title", "case_study_title",
        ),
        f"{attack_title} Practical Activity",
    )

    instructions = _first_text(
        item,
        (
            "instructions", "description", "objective",
            "task", "details",
        ),
        "",
    )

    scenario = _first_text(
        item,
        (
            "scenario", "case", "situation", "sample",
            "message", "problem",
        ),
        "",
    )

    # Case studies commonly store their main narrative in "content".
    if content_type == "case_studies" and not scenario:
        scenario = _first_text(item, ("content", "overview", "summary"))

    if not instructions:
        instructions = (
            "Review the material and identify appropriate "
            "cybersecurity actions."
        )

    # Keep structured activity steps and tasks visible in the existing
    # instructions field, including for reading-only activities.
    steps = _as_text_list(item.get("steps"))
    tasks = _as_text_list(item.get("tasks"))

    activity_steps = tasks or steps

    if activity_steps:
        instructions += "\n\nActivity tasks:\n" + "\n".join(
            f"{index}. {step}"
            for index, step in enumerate(activity_steps, start=1)
        )

    discussion = _as_text_list(item.get("discussion"))

    if discussion:
        instructions += "\n\nDiscussion questions:\n" + "\n".join(
            f"{index}. {question}"
            for index, question in enumerate(discussion, start=1)
        )

    raw_options = (
        item.get("options")
        or item.get("choices")
        or item.get("answer_options")
        or item.get("possible_answers")
        or item.get("answers")
        or []
    )

    options = _normalize_options(raw_options)
    correct_answer = _normalize_correct_answer(item, options)

    explanation = _first_text(
        item,
        (
            "explanation", "feedback", "solution",
            "rationale", "reason", "expected_outcome",
            "expected_result", "conclusion",
        ),
        "Review the security implications of your findings.",
    )

    return {
        "title": title,
        "instructions": instructions,
        "type": "quiz" if options else "reading",
        "scenario": scenario,
        "options": options,
        "correct_answer": correct_answer,
        "explanation": explanation,
        "content_type": content_type,
    }


# --------------------------------------------------
# ATTACK LAB CATALOG
# --------------------------------------------------

def _get_attack_lab_items():
    """Build one catalog entry for each attack with practical content."""
    ATTACK_CATEGORIES, _get_category, _, _ = _get_attack_modules()
    items = []

    for category_info in ATTACK_CATEGORIES:
        category, attacks = _get_category(category_info["id"])

        if category is None:
            continue

        for attack in attacks:
            attack_id = str(attack.get("id", "")).strip()
            title = (
                attack.get("name")
                or attack.get("title")
                or attack.get("attack_name")
            )

            if not attack_id or not title:
                continue

            records = _get_attack_content_records(attack)

            # Do not advertise links that have no available activity.
            if not records:
                continue

            category_name = (
                category.get("name")
                or category.get("title")
                or category_info.get("name")
                or "Uncategorized"
            )

            items.append({
                "id": f"attack-{category_info['id']}-{attack_id}",
                "title": f"{title} Lab",
                "name": f"{title} Lab",
                "category": category_name,
                "difficulty": attack.get("difficulty", "Beginner"),
                "description": (
                    attack.get("description")
                    or attack.get("overview")
                    or f"Explore defensive measures for {title}."
                ),
                "duration": "10–15 minutes",
                "category_id": category_info["id"],
                "attack_id": attack_id,
                "activity_count": len(records),
                "content_types": sorted({
                    record["content_type"] for record in records
                }),
            })

    return items


def _get_all_labs():
    return {
        "categories": _get_category_cards(),
        "levels": PRACTICE_LEVELS,
        "interactive_labs": INTERACTIVE_LABS,
        "attack_labs": _get_attack_lab_items(),
    }


# --------------------------------------------------
# GENERAL PRACTICE BUILDER
# --------------------------------------------------

def _build_general_practice():
    """Build general practice activities from all supported content types."""
    ATTACK_CATEGORIES, _get_category, _, _ = _get_attack_modules()

    levels = {
        level["id"]: [] for level in PRACTICE_LEVELS
    }

    difficulty_map = {
        "beginner": "beginner",
        "easy": "beginner",
        "basic": "beginner",
        "intermediate": "intermediate",
        "medium": "intermediate",
        "advanced": "advanced",
        "hard": "advanced",
        "high-level": "high-level",
        "high level": "high-level",
        "expert": "high-level",
    }

    for category_info in ATTACK_CATEGORIES:
        category, attacks = _get_category(category_info["id"])

        if category is None:
            continue

        category_name = (
            category.get("name")
            or category.get("title")
            or category_info.get("name")
            or "Uncategorized"
        )

        for attack in attacks:
            attack_id = str(attack.get("id", "")).strip()
            attack_title = (
                attack.get("name")
                or attack.get("title")
                or attack.get("attack_name")
                or attack_id
            )

            if not attack_id:
                continue

            records = _get_attack_content_records(attack)

            for record_index, record_entry in enumerate(records):
                activity = _normalize_lab_content(
                    record_entry["record"],
                    attack_title,
                    record_entry["content_type"],
                )

                raw_difficulty = str(
                    record_entry["record"].get("difficulty")
                    or attack.get("difficulty")
                    or "beginner"
                ).strip().lower().replace("_", "-")

                level_id = difficulty_map.get(raw_difficulty, "beginner")

                if len(levels[level_id]) >= 3:
                    continue

                levels[level_id].append({
                    "id": (
                        f"{level_id}-{category_info['id']}-"
                        f"{attack_id}-{record_index}"
                    ),
                    "title": activity["title"],
                    "name": activity["title"],
                    "category": category_name,
                    "attack_title": attack_title,
                    "description": activity["instructions"],
                    "category_id": category_info["id"],
                    "attack_id": attack_id,
                    "content_type": record_entry["content_type"],
                    "content": activity,
                })

    return levels


# --------------------------------------------------
# SHARED TEMPLATE CONTEXT
# --------------------------------------------------

def _render_labs(**context):
    """Provide consistent defaults to the practical labs template."""
    defaults = {
        "labs": INTERACTIVE_LABS,
        "attack_labs": _get_attack_lab_items(),
        "categories": _get_category_cards(),
        "practice_levels": PRACTICE_LEVELS,
        "selected_lab": None,
        "selected_level": None,
        "selected_general_activity": None,
        "selected_attack": None,
        "selected_subcategory": None,
        "selected_category": None,
        "category_attack_labs": [],
        "activity": None,
        "result": None,
        "level_activities": [],
        "attack_lab_count": 0,
        "current_attack_lab_index": 0,
    }

    defaults.update(context)

    return render_template("practical_labs.html", **defaults)


def _login_required():
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    return None


# --------------------------------------------------
# LAB OVERVIEW
# --------------------------------------------------

@labs_bp.route("/labs")
def practical_labs():
    response = _login_required()

    if response is not None:
        return response

    return _render_labs()


@labs_bp.route("/labs/category/<category_id>")
def category_labs(category_id):
    """Show only practical labs associated with the selected attack category."""
    response = _login_required()

    if response is not None:
        return response

    categories = _get_category_cards()
    selected_category = next(
        (
            category for category in categories
            if str(category["id"]) == str(category_id)
        ),
        None,
    )

    if selected_category is None:
        abort(404)

    category_attack_labs = [
        lab for lab in _get_attack_lab_items()
        if str(lab.get("category_id")) == str(category_id)
    ]

    return _render_labs(
        selected_category=selected_category,
        category_attack_labs=category_attack_labs,
    )


# --------------------------------------------------
# GENERAL PRACTICE LEVELS
# --------------------------------------------------

@labs_bp.route("/labs/level/<level_id>", methods=["GET"])
def general_practice(level_id):
    response = _login_required()

    if response is not None:
        return response

    level = next(
        (item for item in PRACTICE_LEVELS if item["id"] == level_id),
        None,
    )

    if level is None:
        abort(404)

    activities = _build_general_practice().get(level_id, [])

    return _render_labs(
        selected_level=level,
        level_activities=activities,
    )


@labs_bp.route(
    "/labs/level/<level_id>/<activity_id>",
    methods=["GET", "POST"],
)
def general_practice_activity(level_id, activity_id):
    response = _login_required()

    if response is not None:
        return response

    level = next(
        (item for item in PRACTICE_LEVELS if item["id"] == level_id),
        None,
    )

    if level is None:
        abort(404)

    activities = _build_general_practice().get(level_id, [])

    selected = next(
        (item for item in activities if item["id"] == activity_id),
        None,
    )

    if selected is None:
        abort(404)

    activity = selected["content"]
    result = None

    if request.method == "POST":
        selected_answer = request.form.get("answer", "")
        options = activity.get("options", [])
        correct_answer = activity.get("correct_answer", "")

        if not options:
            result = {
                "status": "error",
                "message": (
                    "This activity has no answer choices. "
                    "Review the activity instructions."
                ),
            }
        elif selected_answer not in options:
            result = {
                "status": "error",
                "message": "Select one of the available answers.",
            }
        elif not correct_answer:
            result = {
                "status": "success",
                "is_correct": None,
                "score": "Not graded",
                "message": (
                    "This activity has no defined correct answer "
                    "and cannot be automatically graded."
                ),
                "explanation": activity.get("explanation", ""),
            }
        else:
            is_correct = (
                selected_answer.casefold()
                == correct_answer.casefold()
            )

            result = {
                "status": "success",
                "is_correct": is_correct,
                "score": "1/1" if is_correct else "0/1",
                "message": (
                    "Correct answer."
                    if is_correct
                    else "Incorrect answer. Review the explanation."
                ),
                "explanation": activity.get("explanation", ""),
            }

    return _render_labs(
        selected_level=level,
        selected_general_activity=selected,
        selected_lab=selected,
        activity=activity,
        result=result,
        level_activities=activities,
    )


# --------------------------------------------------
# EXISTING GUIDED LABS
# --------------------------------------------------

@labs_bp.route("/labs/<lab_id>", methods=["GET", "POST"])
def lab_activity(lab_id):
    response = _login_required()

    if response is not None:
        return response

    lab = next(
        (item for item in INTERACTIVE_LABS if item["id"] == lab_id),
        None,
    )

    if lab is None:
        abort(404)

    activity = LAB_ACTIVITIES.get(lab_id)

    if activity is None:
        abort(404)

    result = None

    if request.method == "POST":
        if activity["type"] == "password":
            sample_password = request.form.get(
                "sample_password",
                request.form.get("password", ""),
            )

            if not sample_password:
                result = {
                    "status": "error",
                    "message": "Enter a sample password to evaluate.",
                    "feedback": [],
                }
            else:
                score = 0
                feedback = []

                if len(sample_password) >= 12:
                    score += 1
                else:
                    feedback.append("Use at least 12 characters.")

                if (
                    any(char.islower() for char in sample_password)
                    and any(char.isupper() for char in sample_password)
                ):
                    score += 1
                else:
                    feedback.append(
                        "Use both uppercase and lowercase letters."
                    )

                if any(char.isdigit() for char in sample_password):
                    score += 1
                else:
                    feedback.append("Consider including numbers.")

                if any(not char.isalnum() for char in sample_password):
                    score += 1
                else:
                    feedback.append(
                        "Consider including special characters."
                    )

                feedback.append(
                    "This is a basic educational check, not a guarantee "
                    "that a password is secure or unique. Use a unique "
                    "password and consider a password manager."
                )

                result = {
                    "status": "success",
                    "score": f"{(score / 4) * 100:.0f}%",
                    "message": "Sample password evaluation completed.",
                    "feedback": feedback,
                }

        else:
            selected_answer = request.form.get("answer", "")
            options = activity.get("options", [])

            if selected_answer not in options:
                result = {
                    "status": "error",
                    "message": "Select one of the available answers.",
                    "feedback": [],
                }
            else:
                is_correct = (
                    selected_answer.casefold()
                    == activity["correct_answer"].casefold()
                )

                result = {
                    "status": "success",
                    "is_correct": is_correct,
                    "score": "1/1" if is_correct else "0/1",
                    "message": (
                        "Correct choice."
                        if is_correct
                        else "That is not the best defensive response."
                    ),
                    "feedback": [],
                    "explanation": activity["explanation"],
                }

    return _render_labs(
        selected_lab=lab,
        activity=activity,
        result=result,
    )


# --------------------------------------------------
# INDIVIDUAL ATTACK LABS
# --------------------------------------------------

@labs_bp.route(
    "/labs/attack/<category_id>/<attack_id>",
    methods=["GET", "POST"],
)
def attack_lab(category_id, attack_id):
    response = _login_required()

    if response is not None:
        return response

    category, subcategory, attack = _get_attack_record(
        category_id,
        attack_id,
    )

    if attack is None:
        abort(404)

    attack_title = (
        attack.get("name")
        or attack.get("title")
        or attack.get("attack_name")
        or attack_id
    )

    lab_records = _get_attack_content_records(attack)

    if not lab_records:
        abort(404)

    try:
        index = int(request.args.get("activity", "0"))
    except (TypeError, ValueError):
        abort(404)

    if index < 0 or index >= len(lab_records):
        abort(404)

    record_entry = lab_records[index]

    activity = _normalize_lab_content(
        record_entry["record"],
        attack_title,
        record_entry["content_type"],
    )

    category_name = (
        category.get("name")
        or category.get("title")
        or "Uncategorized"
    )

    selected_lab = {
        "id": f"attack-{category_id}-{attack_id}",
        "title": activity["title"],
        "name": activity["title"],
        "description": (
            attack.get("description")
            or attack.get("overview")
            or f"Practical learning activity for {attack_title}."
        ),
        "difficulty": attack.get("difficulty", "Beginner"),
        "category": category_name,
        "duration": "10–15 minutes",
        "category_id": category_id,
        "attack_id": attack_id,
        "content_type": record_entry["content_type"],
    }

    result = None

    if request.method == "POST":
        selected_answer = request.form.get("answer", "")
        options = activity.get("options", [])
        correct_answer = activity.get("correct_answer", "")

        if not options:
            result = {
                "status": "error",
                "message": (
                    "This activity has no answer choices. "
                    "Review its instructions and learning material."
                ),
                "feedback": [],
            }

        elif selected_answer not in options:
            result = {
                "status": "error",
                "message": "Select one of the available answers.",
                "feedback": [],
            }

        elif not correct_answer:
            result = {
                "status": "success",
                "is_correct": None,
                "score": "Not graded",
                "message": (
                    "This activity has no defined correct answer, "
                    "so it cannot be automatically graded."
                ),
                "feedback": [],
                "explanation": activity.get("explanation", ""),
            }

        else:
            is_correct = (
                selected_answer.casefold()
                == correct_answer.casefold()
            )

            result = {
                "status": "success",
                "is_correct": is_correct,
                "score": "1/1" if is_correct else "0/1",
                "message": (
                    "Correct answer."
                    if is_correct
                    else "Incorrect answer. Review the explanation."
                ),
                "feedback": [],
                "explanation": activity.get("explanation", ""),
            }

    return _render_labs(
        selected_lab=selected_lab,
        selected_attack=attack,
        selected_subcategory=subcategory,
        activity=activity,
        result=result,
        attack_lab_count=len(lab_records),
        current_attack_lab_index=index,
    )
