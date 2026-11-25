
"""
CyberGuard General Labs
-----------------------
Provides reusable cybersecurity practical labs that are not tied
to one specific attack category.

Responsibilities:
- Define general cybersecurity lab exercises.
- Retrieve general labs in a consistent format.
- Include labs derived from existing attack data when requested.
- Work with data normalized by data_adapter.py.
- Avoid modifying original data files.

This module does not load data files automatically. The application
can pass its existing data structures to the public helper functions.
"""

from copy import deepcopy
from typing import Any, Dict, List, Optional

try:
    from data_adapter import (
        extract_attacks,
        get_category_attacks,
        get_subcategories,
        get_content,
        normalize_attack,
    )
except ImportError:
    from .data_adapter import (
        extract_attacks,
        get_category_attacks,
        get_subcategories,
        get_content,
        normalize_attack,
    )


# ---------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------

MODULE_ID = "general-labs"
MODULE_NAME = "General Cybersecurity Labs"

SUPPORTED_DIFFICULTIES = {
    "beginner",
    "intermediate",
    "advanced",
}

LAB_FIELDS = (
    "id",
    "title",
    "name",
    "description",
    "objective",
    "scenario",
    "tasks",
    "expected_outcome",
    "difficulty",
    "category",
    "tags",
)


# ---------------------------------------------------------------------
# General lab definitions
# ---------------------------------------------------------------------

GENERAL_LABS: List[Dict[str, Any]] = [
    {
        "id": "security-baseline-review",
        "title": "Security Baseline Review",
        "name": "Security Baseline Review",
        "description": (
            "Review a fictional workstation against basic cybersecurity "
            "requirements and identify missing safeguards."
        ),
        "objective": (
            "Recognise common security weaknesses and recommend "
            "appropriate defensive controls."
        ),
        "scenario": (
            "You are reviewing a fictional employee workstation. "
            "The device has pending updates, an unlocked screen, "
            "and no documented backup status."
        ),
        "tasks": [
            "Identify the security weaknesses described in the scenario.",
            "Prioritise the weaknesses according to their potential impact.",
            "Recommend suitable protective controls.",
            "Prepare a short remediation checklist.",
        ],
        "expected_outcome": (
            "The learner identifies the main weaknesses and produces "
            "a prioritised, practical remediation plan."
        ),
        "difficulty": "Beginner",
        "category": "General Cybersecurity",
        "tags": ["security-basics", "workstation", "defence"],
    },
    {
        "id": "password-security-review",
        "title": "Password and Authentication Review",
        "name": "Password and Authentication Review",
        "description": (
            "Evaluate account-security practices using fictional "
            "examples without collecting real credentials."
        ),
        "objective": (
            "Understand unique passwords, password managers, "
            "multi-factor authentication, and secure account recovery."
        ),
        "scenario": (
            "A fictional employee reuses one password across several "
            "services and has not enabled multi-factor authentication "
            "on an important account."
        ),
        "tasks": [
            "Identify the risks associated with password reuse.",
            "Recommend a password manager and unique passwords.",
            "Explain where multi-factor authentication should be enabled.",
            "Describe the steps for responding to a suspected account compromise.",
        ],
        "expected_outcome": (
            "The learner creates an account-protection plan without "
            "sharing or recording actual passwords."
        ),
        "difficulty": "Beginner",
        "category": "General Cybersecurity",
        "tags": ["passwords", "authentication", "account-security"],
    },
    {
        "id": "data-classification-exercise",
        "title": "Data Classification Exercise",
        "name": "Data Classification Exercise",
        "description": (
            "Classify fictional information and determine how it "
            "should be stored, shared, and protected."
        ),
        "objective": (
            "Apply data-classification principles to personal, "
            "internal, confidential, and public information."
        ),
        "scenario": (
            "A team needs to handle a public brochure, an internal "
            "meeting note, customer contact details, and a confidential "
            "business document."
        ),
        "tasks": [
            "Assign an appropriate classification to each fictional item.",
            "Identify who should be authorised to access each item.",
            "Recommend suitable storage and sharing controls.",
            "Explain how to report accidental disclosure.",
        ],
        "expected_outcome": (
            "The learner classifies information consistently and "
            "recommends proportionate access and handling controls."
        ),
        "difficulty": "Beginner",
        "category": "General Cybersecurity",
        "tags": ["data-protection", "privacy", "access-control"],
    },
    {
        "id": "incident-response-tabletop",
        "title": "Incident Response Tabletop",
        "name": "Incident Response Tabletop",
        "description": (
            "Practise the initial response to a fictional cybersecurity "
            "incident without interacting with production systems."
        ),
        "objective": (
            "Understand incident reporting, evidence preservation, "
            "containment decisions, and escalation."
        ),
        "scenario": (
            "An employee reports an unexpected security alert and "
            "suspects that a work account may have been compromised."
        ),
        "tasks": [
            "Identify the information needed for an initial incident report.",
            "Determine which internal team should be notified.",
            "Describe safe containment actions that follow organisational policy.",
            "Explain why logs and relevant evidence should be preserved.",
            "List follow-up actions for recovery and lessons learned.",
        ],
        "expected_outcome": (
            "The learner follows a documented response process and "
            "avoids unauthorised investigation or evidence destruction."
        ),
        "difficulty": "Intermediate",
        "category": "Incident Response",
        "tags": ["incident-response", "reporting", "recovery"],
    },
    {
        "id": "backup-and-recovery-planning",
        "title": "Backup and Recovery Planning",
        "name": "Backup and Recovery Planning",
        "description": (
            "Develop a basic backup and recovery plan for a fictional "
            "small organisation."
        ),
        "objective": (
            "Understand backup frequency, protected copies, recovery "
            "priorities, and restoration testing."
        ),
        "scenario": (
            "A small organisation stores important business files on "
            "a shared server but has not tested its backups recently."
        ),
        "tasks": [
            "Identify the most important data and services.",
            "Recommend a suitable backup schedule.",
            "Explain why backup copies should be protected from unauthorised changes.",
            "Create a simple restoration test plan.",
            "Describe how recovery success should be documented.",
        ],
        "expected_outcome": (
            "The learner develops a practical backup and restoration "
            "plan and recognises the need to test recovery."
        ),
        "difficulty": "Intermediate",
        "category": "Business Continuity",
        "tags": ["backups", "recovery", "resilience"],
    },
    {
        "id": "access-control-review",
        "title": "Access Control and Least Privilege",
        "name": "Access Control and Least Privilege",
        "description": (
            "Review fictional employee permissions and identify "
            "unnecessary access."
        ),
        "objective": (
            "Apply least privilege, role-based access, and periodic "
            "permission reviews."
        ),
        "scenario": (
            "A fictional organisation gives every employee administrator "
            "privileges, including staff who only need to read documents."
        ),
        "tasks": [
            "Identify permissions that exceed each role's requirements.",
            "Map common job responsibilities to appropriate access.",
            "Recommend an approval process for privileged access.",
            "Explain how access should be reviewed when employees change roles or leave.",
        ],
        "expected_outcome": (
            "The learner proposes role-appropriate permissions and "
            "a repeatable access-review process."
        ),
        "difficulty": "Intermediate",
        "category": "Identity and Access Management",
        "tags": ["least-privilege", "permissions", "access-control"],
    },
    {
        "id": "security-awareness-review",
        "title": "Security Awareness Review",
        "name": "Security Awareness Review",
        "description": (
            "Assess everyday security decisions involving unexpected "
            "messages, sensitive requests, and physical access."
        ),
        "objective": (
            "Practise pausing, independently verifying requests, "
            "and reporting suspicious activity."
        ),
        "scenario": (
            "During one working day, an employee receives an unexpected "
            "account alert, encounters an unfamiliar visitor, and is "
            "asked to disclose confidential information."
        ),
        "tasks": [
            "Identify the risk in each situation.",
            "Choose an independent verification method for each request.",
            "Explain how to refuse unsafe requests professionally.",
            "Identify the appropriate reporting channel.",
        ],
        "expected_outcome": (
            "The learner consistently verifies identities and requests "
            "before disclosing information or granting access."
        ),
        "difficulty": "Beginner",
        "category": "Security Awareness",
        "tags": ["awareness", "verification", "social-engineering"],
    },
    {
        "id": "secure-device-handling",
        "title": "Secure Device Handling",
        "name": "Secure Device Handling",
        "description": (
            "Review device-handling practices for offices, remote work, "
            "and public environments."
        ),
        "objective": (
            "Reduce risks from unattended devices, unknown removable "
            "media, exposed screens, and untrusted software."
        ),
        "scenario": (
            "An employee works remotely, leaves a laptop unattended "
            "in a shared area, and finds an unknown removable drive."
        ),
        "tasks": [
            "Identify the risks in the scenario.",
            "Recommend appropriate screen-locking and physical-security measures.",
            "Explain how unknown removable media should be handled.",
            "Describe how to obtain approved software and security updates.",
        ],
        "expected_outcome": (
            "The learner applies safe device-handling procedures "
            "without connecting unknown media or installing untrusted software."
        ),
        "difficulty": "Beginner",
        "category": "Endpoint Security",
        "tags": ["devices", "removable-media", "physical-security"],
    },
]


# ---------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------

def _as_text(value: Any, default: str = "") -> str:
    """Convert a value to readable text without exposing complex objects."""
    if value is None:
        return default

    if isinstance(value, str):
        return value.strip() or default

    if isinstance(value, (int, float, bool)):
        return str(value)

    return default


def _as_list(value: Any) -> List[Any]:
    """Normalize a value to a list without splitting strings into characters."""
    if value is None:
        return []

    if isinstance(value, list):
        return list(value)

    if isinstance(value, tuple):
        return list(value)

    if isinstance(value, (str, dict)):
        return [value]

    return []


def _normalise_difficulty(value: Any) -> str:
    """Return a consistently capitalised difficulty label."""
    text = _as_text(value, "Beginner")
    normalised = text.lower()

    if normalised in SUPPORTED_DIFFICULTIES:
        return normalised.title()

    return text


def _normalise_lab(
    lab: Dict[str, Any],
    fallback_id: Optional[str] = None,
    category: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Return a predictable lab structure.

    Unknown source fields are preserved so existing data is not lost.
    The input dictionary is never modified.
    """
    if not isinstance(lab, dict):
        return {}

    result = deepcopy(lab)

    title = _as_text(
        result.get("title")
        or result.get("name")
        or result.get("id"),
        "Untitled Lab",
    )

    lab_id = _as_text(
        result.get("id"),
        fallback_id or title.lower().replace(" ", "-"),
    )

    result["id"] = lab_id
    result["title"] = title
    result["name"] = _as_text(result.get("name"), title)
    result["description"] = _as_text(
        result.get("description")
        or result.get("summary"),
        "No description provided.",
    )
    result["objective"] = _as_text(
        result.get("objective")
        or result.get("learning_objectives"),
        "",
    )
    result["scenario"] = _as_text(result.get("scenario"), "")
    result["tasks"] = _as_list(
        result.get("tasks")
        or result.get("steps")
    )
    result["expected_outcome"] = _as_text(
        result.get("expected_outcome"),
        "",
    )
    result["difficulty"] = _normalise_difficulty(
        result.get("difficulty")
    )
    result["category"] = _as_text(
        result.get("category"),
        category or "General Cybersecurity",
    )
    result["tags"] = _as_list(result.get("tags"))

    return result


def _extract_lab_items(value: Any) -> List[Dict[str, Any]]:
    """
    Extract lab dictionaries from common list and dictionary layouts.

    Supports:
    - A single lab dictionary.
    - A list of lab dictionaries.
    - A mapping of lab IDs to lab dictionaries.
    - Nested collections containing labs.
    """
    results: List[Dict[str, Any]] = []

    if isinstance(value, (list, tuple)):
        for item in value:
            results.extend(_extract_lab_items(item))
        return results

    if not isinstance(value, dict):
        return results

    if any(
        key in value
        for key in ("title", "name", "objective", "tasks", "scenario")
    ):
        results.append(deepcopy(value))
        return results

    for key, item in value.items():
        if isinstance(item, dict):
            extracted = _extract_lab_items(item)

            for lab in extracted:
                if not lab.get("id"):
                    lab["id"] = str(key)
                results.append(lab)

        elif isinstance(item, (list, tuple)):
            results.extend(_extract_lab_items(item))

    return results


# ---------------------------------------------------------------------
# Public API: general labs
# ---------------------------------------------------------------------

def get_general_labs(
    difficulty: Optional[str] = None,
    category: Optional[str] = None,
    search: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Return copies of general lab definitions.

    Optional filters:
        difficulty: Beginner, Intermediate, or Advanced.
        category: Exact category name, case-insensitive.
        search: Text to search in the title, description, objective,
                scenario, and tags.

    The original GENERAL_LABS definitions are never modified.
    """
    labs = [_normalise_lab(lab) for lab in GENERAL_LABS]

    if difficulty:
        target = difficulty.strip().lower()
        labs = [
            lab for lab in labs
            if lab["difficulty"].lower() == target
        ]

    if category:
        target = category.strip().lower()
        labs = [
            lab for lab in labs
            if lab["category"].lower() == target
        ]

    if search:
        target = search.strip().lower()

        def matches(lab: Dict[str, Any]) -> bool:
            searchable = " ".join(
                [
                    lab["title"],
                    lab["description"],
                    lab["objective"],
                    lab["scenario"],
                    " ".join(str(tag) for tag in lab["tags"]),
                ]
            ).lower()

            return target in searchable

        labs = [lab for lab in labs if matches(lab)]

    return labs


def get_general_lab(lab_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve one general lab by its ID."""
    target = str(lab_id).strip().lower()

    for lab in get_general_labs():
        if lab["id"].lower() == target:
            return lab

    return None


def get_general_lab_categories() -> List[str]:
    """Return the distinct categories used by general labs."""
    return sorted({
        lab["category"]
        for lab in get_general_labs()
    })


def get_general_lab_count() -> int:
    """Return the number of predefined general labs."""
    return len(GENERAL_LABS)


# ---------------------------------------------------------------------
# Public API: labs from existing attack data
# ---------------------------------------------------------------------

def get_attack_labs(
    category_data: Any,
    attack_id: Optional[str] = None,
    subcategory_id: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Retrieve practical labs attached to existing attack records.

    This function supports the data_adapter.py interface and preserves
    the source's lab content.

    If attack_id is provided, only that attack is considered.
    Otherwise, labs are collected from the supplied category.

    The function does not invent attack-specific labs when none exist.
    """
    selected_attacks: List[Dict[str, Any]] = []

    if attack_id is not None:
        try:
            from data_adapter import find_attack
        except ImportError:
            from .data_adapter import find_attack

        _, attack = find_attack(
            category_data,
            attack_id,
            subcategory_id=subcategory_id,
        )

        if attack is None:
            return []

        selected_attacks = [attack]

    elif isinstance(category_data, dict) and "types" in category_data:
        if subcategory_id is not None:
            subcategory = next(
                (
                    item for item in get_subcategories(category_data)
                    if item["id"] == str(subcategory_id)
                ),
                None,
            )

            if subcategory is None:
                return []

            selected_attacks = subcategory["attacks_list"]
        else:
            selected_attacks = get_category_attacks(category_data)

    else:
        selected_attacks = extract_attacks(category_data)

    results: List[Dict[str, Any]] = []

    for attack in selected_attacks:
        if not isinstance(attack, dict):
            continue

        attack_name = _as_text(
            attack.get("name") or attack.get("title"),
            "Unknown Attack",
        )
        source_id = _as_text(
            attack.get("id"),
            attack_name.lower().replace(" ", "-"),
        )

        raw_labs = get_content(attack, "labs")

        for index, lab in enumerate(_extract_lab_items(raw_labs), start=1):
            normalised = _normalise_lab(
                lab,
                fallback_id=f"{source_id}-lab-{index}",
                category=attack_name,
            )

            if normalised:
                normalised["source_attack_id"] = source_id
                normalised["source_attack_name"] = attack_name
                results.append(normalised)

    return results


def get_all_labs(
    category_data: Any = None,
    include_general: bool = True,
) -> List[Dict[str, Any]]:
    """
    Combine predefined general labs with labs from supplied attack data.

    If category_data is omitted, only general labs are returned.

    This function intentionally does not load or guess the locations
    of the project's 14 data files. The calling application remains
    responsible for loading those files.
    """
    results: List[Dict[str, Any]] = []

    if include_general:
        results.extend(get_general_labs())

    if category_data is None:
        return results

    results.extend(get_attack_labs(category_data))
    return results


# ---------------------------------------------------------------------
# Public API: lab summaries and validation
# ---------------------------------------------------------------------

def get_lab_summary(lab: Dict[str, Any]) -> Dict[str, Any]:
    """Return a compact summary suitable for a lab listing page."""
    if not isinstance(lab, dict):
        return {}

    normalised = _normalise_lab(lab)

    return {
        "id": normalised["id"],
        "title": normalised["title"],
        "description": normalised["description"],
        "difficulty": normalised["difficulty"],
        "category": normalised["category"],
        "task_count": len(normalised["tasks"]),
    }


def validate_lab(lab: Any) -> Dict[str, Any]:
    """
    Check whether a lab has the minimum fields needed by the UI.

    Returns:
        {
            "valid": bool,
            "missing_fields": list[str],
            "errors": list[str]
        }
    """
    errors: List[str] = []
    missing_fields: List[str] = []

    if not isinstance(lab, dict):
        return {
            "valid": False,
            "missing_fields": list(LAB_FIELDS),
            "errors": ["Lab must be a dictionary."],
        }

    for field in ("id", "title"):
        if not _as_text(lab.get(field)):
            missing_fields.append(field)

    if not _as_text(lab.get("objective")):
        missing_fields.append("objective")

    if not _as_text(lab.get("scenario")):
        missing_fields.append("scenario")

    tasks = _as_list(lab.get("tasks"))

    if not tasks:
        missing_fields.append("tasks")

    if missing_fields:
        errors.append(
            "Required lab information is missing: "
            + ", ".join(missing_fields)
        )

    return {
        "valid": not errors,
        "missing_fields": missing_fields,
        "errors": errors,
    }


def search_labs(
    query: str,
    category_data: Any = None,
    include_general: bool = True,
) -> List[Dict[str, Any]]:
    """Search general and optionally supplied attack-specific labs."""
    query = str(query or "").strip().lower()

    if not query:
        return get_all_labs(
            category_data=category_data,
            include_general=include_general,
        )

    labs = get_all_labs(
        category_data=category_data,
        include_general=include_general,
    )

    results = []

    for lab in labs:
        searchable_fields = [
            lab.get("id", ""),
            lab.get("title", ""),
            lab.get("name", ""),
            lab.get("description", ""),
            lab.get("objective", ""),
            lab.get("scenario", ""),
            lab.get("category", ""),
        ]

        searchable_text = " ".join(
            str(value) for value in searchable_fields
        ).lower()

        searchable_text += " " + " ".join(
            str(task) for task in _as_list(lab.get("tasks"))
        ).lower()

        if query in searchable_text:
            results.append(lab)

    return results


# ---------------------------------------------------------------------
# Compatibility aliases
# ---------------------------------------------------------------------

# Convenient aliases for applications using simpler naming conventions.
get_labs = get_general_labs
get_lab_by_id = get_general_lab
get_lab_categories = get_general_lab_categories