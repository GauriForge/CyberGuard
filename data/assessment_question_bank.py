
"""CyberGuard Attack Assessment Question Bank.

Generates exactly 10 MCQ entries for every attack in ATTACK_CATEGORIES.
Uses existing assessment questions where valid and adds questions based
on the individual attack's learning content.

Simulation and practical-lab questions are excluded.
"""

import re
from collections.abc import Mapping

QUESTIONS_PER_ATTACK = 10

_EXCLUDED_KEYS = {
    "assessment", "assessments", "quiz", "quizzes",
    "simulation", "simulations", "practical_lab", "practical_labs",
    "lab", "labs",
}

_FIELD_GROUPS = {
    "overview": {
        "overview", "description", "summary", "introduction", "details",
        "conclusion", "definition",
    },
    "process": {
        "how_it_works", "attack_process", "process", "steps", "mechanism",
        "working", "method", "methods",
    },
    "indicators": {
        "warning_signs", "indicators", "symptoms", "signs",
        "detection_indicators",
    },
    "impact": {"impact", "consequences", "effects", "risks"},
    "prevention": {
        "prevention", "protection", "mitigation", "countermeasures",
        "security_measures", "best_practices", "defense", "defences",
    },
    "response": {
        "response", "remediation", "incident_response", "recovery",
        "detection",
    },
    "objectives": {"learning_objectives", "objectives"},
    "examples": {
        "examples", "real_world_examples", "real_world_example",
        "case_study", "case_studies", "scenario",
    },
}

_DISTRACTORS = (
    "A routine activity unrelated to this security threat.",
    "A harmless system operation with no security impact.",
    "A standard maintenance task unrelated to the attack.",
    "An ordinary user action that does not create this security risk.",
    "A routine backup operation that does not indicate this attack.",
    "A general hardware upgrade unrelated to the security issue.",
    "A normal interface change with no security consequence.",
    "An unrelated network activity requiring no incident response.",
)

_QUESTION_TEMPLATES = (
    ("overview", "Which statement best describes {name}?"),
    ("process", "Which statement explains how {name} works?"),
    ("indicators", "Which of the following may indicate {name}?"),
    ("impact", "Which outcome may be associated with {name}?"),
    ("prevention", "Which measure can help reduce the risk of {name}?"),
    ("response", "Which action is relevant when responding to {name}?"),
    ("objectives", "Which learning point is important when studying {name}?"),
    ("examples", "Which statement is relevant to a real-world example of {name}?"),
    ("prevention", "Which security practice helps protect against {name}?"),
    ("overview", "Which fact should a learner remember about {name}?"),
)


def _clean(value):
    if isinstance(value, str):
        return re.sub(r"\s+", " ", value).strip()
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)
    return ""


def _slug(value):
    value = str(value or "").strip().lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def _unique(values):
    result, seen = [], set()

    for value in values:
        value = _clean(value)
        key = value.casefold()

        if value and key not in seen:
            seen.add(key)
            result.append(value)

    return result


def _get_attack_name(record):
    return (
        _clean(record.get("name"))
        or _clean(record.get("title"))
        or _clean(record.get("attack_name"))
        or _clean(record.get("label"))
        or "Unnamed Attack"
    )


def _extract_facts(record):
    """Extract learning facts while excluding quiz, lab and simulation data."""
    facts = {group: [] for group in _FIELD_GROUPS}

    def add(group, value):
        if isinstance(value, str):
            facts[group].append(value)

        elif isinstance(value, (list, tuple)):
            for item in value:
                if isinstance(item, str):
                    facts[group].append(item)

                elif isinstance(item, Mapping):
                    for nested_key in (
                        "description", "summary", "title", "lesson", "detail",
                        "scenario", "problem", "response", "step", "text",
                    ):
                        nested = item.get(nested_key)
                        if isinstance(nested, str):
                            facts[group].append(nested)

        elif isinstance(value, Mapping):
            for nested_key in (
                "description", "summary", "title", "lesson", "detail",
                "scenario", "problem", "response", "step", "text",
            ):
                nested = value.get(nested_key)
                if isinstance(nested, str):
                    facts[group].append(nested)

    def walk(value):
        if isinstance(value, Mapping):
            for key, child in value.items():
                normalized_key = str(key).strip().lower()

                if normalized_key in _EXCLUDED_KEYS:
                    continue

                group = next(
                    (
                        name for name, aliases in _FIELD_GROUPS.items()
                        if normalized_key in aliases
                    ),
                    None,
                )

                if group:
                    add(group, child)

                elif isinstance(child, (Mapping, list, tuple)):
                    walk(child)

        elif isinstance(value, (list, tuple)):
            for child in value:
                if isinstance(child, (Mapping, list, tuple)):
                    walk(child)

    walk(record)

    return {
        group: _unique(values)
        for group, values in facts.items()
    }


def _find_assessment_questions(record):
    """Read only explicit assessment sections."""
    found = []

    def walk_assessment(value):
        if isinstance(value, Mapping):
            if any(
                key in value
                for key in ("question", "question_text", "prompt")
            ):
                found.append(value)

            else:
                for child in value.values():
                    if isinstance(child, (Mapping, list, tuple)):
                        walk_assessment(child)

        elif isinstance(value, (list, tuple)):
            for child in value:
                walk_assessment(child)

    def find_sections(value):
        if isinstance(value, Mapping):
            for key, child in value.items():
                key = str(key).lower()

                if key in {"assessment", "assessments", "quiz", "quizzes"}:
                    walk_assessment(child)

                elif key not in _EXCLUDED_KEYS and isinstance(
                    child, (Mapping, list, tuple)
                ):
                    find_sections(child)

        elif isinstance(value, (list, tuple)):
            for child in value:
                find_sections(child)

    find_sections(record)

    questions = []
    seen = set()

    for item in found:
        prompt = _clean(
            item.get("question")
            or item.get("question_text")
            or item.get("text")
            or item.get("prompt")
        )

        options = (
            item.get("options")
            or item.get("choices")
            or item.get("answer_options")
        )

        if (
            not prompt
            or not isinstance(options, (list, tuple))
            or len(options) < 2
        ):
            continue

        options = [_clean(option) for option in options]

        if any(not option for option in options):
            continue

        answer = item.get(
            "correct_answer",
            item.get(
                "correct_option",
                item.get(
                    "correct",
                    item.get("answer", item.get("answer_index")),
                ),
            ),
        )

        if isinstance(answer, bool):
            continue

        if isinstance(answer, int):
            answer_index = (
                answer if 0 <= answer < len(options) else None
            )

        else:
            answer_text = _clean(answer)

            if answer_text.isdigit() and 0 <= int(answer_text) < len(options):
                answer_index = int(answer_text)

            else:
                answer_index = next(
                    (
                        i for i, option in enumerate(options)
                        if option.casefold() == answer_text.casefold()
                    ),
                    None,
                )

        if answer_index is None:
            continue

        key = prompt.casefold()

        if key in seen:
            continue

        seen.add(key)

        questions.append({
            "question": prompt,
            "options": options,
            "correct_answer": answer_index,
            "explanation": _clean(
                item.get("explanation")
                or item.get("feedback")
                or item.get("rationale")
            ),
        })

    return questions


def _make_options(correct, number):
    wrong = []
    start = number % len(_DISTRACTORS)

    for offset in range(len(_DISTRACTORS)):
        option = _DISTRACTORS[
            (start + offset) % len(_DISTRACTORS)
        ]

        if option.casefold() != correct.casefold() and option not in wrong:
            wrong.append(option)

        if len(wrong) == 3:
            break

    options = [correct] + wrong

    shift = number % 4
    options = options[shift:] + options[:shift]

    return options, options.index(correct)


def _build_generated_question(
    name,
    prompt,
    answer,
    explanation,
    number,
):
    options, correct_index = _make_options(answer, number)

    return {
        "question": prompt,
        "options": options,
        "correct_answer": correct_index,
        "explanation": explanation,
    }


def _generate_questions(record):
    """Return exactly ten question entries for one attack."""
    name = _get_attack_name(record)
    facts = _extract_facts(record)

    questions = _find_assessment_questions(record)[
        :QUESTIONS_PER_ATTACK
    ]

    used_prompts = {
        question["question"].casefold()
        for question in questions
    }

    all_facts = _unique(
        fact
        for group in facts.values()
        for fact in group
    )

    if not all_facts:
        all_facts = [
            f"{name} is the cybersecurity attack being studied in this assessment."
        ]

    used_answers = set()

    for question in questions:
        index = question["correct_answer"]
        used_answers.add(
            _clean(question["options"][index]).casefold()
        )

    for number, (group, template) in enumerate(_QUESTION_TEMPLATES):
        if len(questions) >= QUESTIONS_PER_ATTACK:
            break

        candidates = facts.get(group) or all_facts

        answer = next(
            (
                fact for fact in candidates
                if fact.casefold() not in used_answers
            ),
            candidates[number % len(candidates)],
        )

        prompt = template.format(name=name)

        if prompt.casefold() in used_prompts:
            prompt = f"{prompt} (Question {number + 1})"

        explanation = (
            f"This answer is based on the available learning content for {name}."
        )

        questions.append(
            _build_generated_question(
                name,
                prompt,
                answer,
                explanation,
                len(questions),
            )
        )

        used_prompts.add(prompt.casefold())
        used_answers.add(answer.casefold())

    # Fill any remaining places using this attack's own learning information.
    fallback_templates = (
        "Which learning fact is associated with {name}?",
        "What should a learner remember when studying {name}?",
        "Which statement is relevant to understanding {name}?",
        "Which point belongs in a review of {name}?",
        "Which statement relates to the security topic {name}?",
    )

    fallback_number = 0

    while len(questions) < QUESTIONS_PER_ATTACK:
        answer = all_facts[
            fallback_number % len(all_facts)
        ]

        prompt = fallback_templates[
            fallback_number % len(fallback_templates)
        ].format(name=name)

        prompt = f"{prompt} (Question {len(questions) + 1})"

        questions.append(
            _build_generated_question(
                name,
                prompt,
                answer,
                f"This answer uses the available learning information for {name}.",
                len(questions),
            )
        )

        fallback_number += 1

    return questions[:QUESTIONS_PER_ATTACK]


def _extract_category_attacks(category_data):
    """Extract attack records from both types and subcategories layouts."""
    from data.data_adapter import is_attack_record, normalize_attack

    results = []

    def walk(value, fallback_id=None):
        if isinstance(value, Mapping):
            # Category and subcategory containers can also have a name
            # and description, so descend into their child records.
            is_container = any(
                key in value
                for key in ("types", "subcategories", "attacks")
            )

            if not is_container and is_attack_record(value):
                attack = normalize_attack(value, fallback_id)

                if attack is not None:
                    results.append(attack)

                return

            for child_key, child in value.items():
                if str(child_key).lower() in _EXCLUDED_KEYS:
                    continue

                if isinstance(child, (Mapping, list, tuple)):
                    walk(child, child_key)

        elif isinstance(value, (list, tuple)):
            for index, child in enumerate(value):
                if isinstance(child, (Mapping, list, tuple)):
                    walk(child, str(index))

    walk(category_data)

    return results


def build_attack_question_bank(attack_categories):
    """Build a question bank containing ten questions per attack.

    Input:
        ATTACK_CATEGORIES from routes.attacks.

    Output:
        A dictionary keyed by category ID and attack ID.
    """
    bank = {}

    for category in attack_categories:
        category_id = str(
            category.get("id") or "uncategorised"
        )

        attacks = _extract_category_attacks(
            category.get("attacks", {})
        )

        for attack in attacks:
            name = _get_attack_name(attack)

            attack_id = (
                _clean(attack.get("id"))
                or _slug(name)
            )

            key = f"{category_id}:{attack_id}"

            questions = _generate_questions(attack)

            bank[key] = {
                "attack_id": attack_id,
                "category_id": category_id,
                "attack_name": name,
                "questions": questions,
                "question_count": len(questions),
            }

    return bank


def get_attack_questions(question_bank, category_id, attack_id):
    """Return the questions for one attack."""
    record = question_bank.get(
        f"{category_id}:{attack_id}"
    )

    return record["questions"] if record else []


def get_attack_question_record(question_bank, category_id, attack_id):
    """Return the complete record for one attack."""
    return question_bank.get(
        f"{category_id}:{attack_id}"
    )


def validate_question_bank(question_bank):
    """Check the number of generated questions for every attack."""
    incomplete = []
    total_questions = 0
    complete = 0

    for key, record in question_bank.items():
        count = len(record.get("questions", []))
        total_questions += count

        if count == QUESTIONS_PER_ATTACK:
            complete += 1

        else:
            incomplete.append({
                "key": key,
                "attack": record.get("attack_name", key),
                "question_count": count,
            })

    return {
        "total_attacks": len(question_bank),
        "complete_attacks": complete,
        "total_questions": total_questions,
        "expected_questions_per_attack": QUESTIONS_PER_ATTACK,
        "incomplete_attacks": incomplete,
        "all_attacks_complete": (
            bool(question_bank)
            and complete == len(question_bank)
        ),
    }
