
"""
CyberGuard Data Adapter
-----------------------
Normalizes different attack-data structures without modifying
the original data files.

Supports:
- Nested category/type dictionaries
- Human-based and computer-based attack groups
- Flat attack dictionaries and lists
- Legacy attack field aliases
- Simulations, practical labs, assessments, and case studies
- Dictionary- and list-based collections

Original data records are copied before normalization.
"""

import re
from collections.abc import Mapping


ATTACK_CONTENT_FIELDS = {
    "summary",
    "description",
    "overview",
    "introduction",
    "details",
    "example",
    "examples",
    "real_world_example",
    "real_world_examples",
    "how_it_works",
    "attack_process",
    "working",
    "steps",
    "warning_signs",
    "indicators",
    "impact",
    "consequences",
    "prevention",
    "mitigation",
    "protection",
    "detection",
    "defense",
    "defences",
    "countermeasures",
    "scenario",
    "explanation",
    "symptoms",
    "remediation",
    "learning_objectives",
    "objectives",
    "difficulty",
    "case_studies",
    "case_study",
    "simulation",
    "simulations",
    "practical_lab",
    "practical_labs",
    "assessment",
    "assessments",
    "learning_resources",
}

METADATA_KEYS = {
    "id",
    "name",
    "title",
    "label",
    "description",
    "types",
    "attacks",
    "theory",
    "labs",
    "practical_lab",
    "practical_labs",
    "simulations",
    "simulation",
    "assessments",
    "assessment",
    "quiz",
    "quizzes",
    "case_studies",
    "case_study",
    "real_world_examples",
    "examples",
    "resources",
    "learning_resources",
    "count",
    "attacks_list",
}

CONTENT_KEYS = {
    "labs": (
        "labs",
        "practical_lab",
        "practical_labs",
    ),
    "simulations": (
        "simulations",
        "simulation",
    ),
    "assessments": (
        "assessments",
        "assessment",
        "quiz",
        "quizzes",
    ),
    "case_studies": (
        "case_studies",
        "case_study",
        "real_world_examples",
    ),
}


def make_slug(value):
    """Convert a name or identifier into a URL-friendly slug."""
    value = str(value or "").strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def _get_name(data, fallback=None):
    """Get a display name from a record."""
    return str(
        data.get("name")
        or data.get("title")
        or data.get("attack_name")
        or data.get("label")
        or fallback
        or "Unnamed Attack"
    )


def is_attack_record(data):
    """Identify an individual attack record."""
    if not isinstance(data, Mapping):
        return False

    # Nodes containing child types are category/group containers.
    if "types" in data:
        return False

    name = (
        data.get("name")
        or data.get("title")
        or data.get("attack_name")
    )

    if not name:
        return False

    return any(
        key in data and data[key] not in (None, "", [], {})
        for key in ATTACK_CONTENT_FIELDS
    )


def normalize_attack(record, fallback_id=None):
    """
    Return a shallow copy with consistent name and ID fields.

    Does not mutate the original record.
    """
    if not isinstance(record, Mapping):
        return None

    attack = dict(record)
    attack["name"] = _get_name(record)

    attack["id"] = str(
        record.get("id")
        or make_slug(fallback_id or attack["name"])
    )

    return attack


def _type_entries(types):
    """Convert dictionary- or list-based types into key/value pairs."""
    if isinstance(types, Mapping):
        return list(types.items())

    if isinstance(types, (list, tuple)):
        entries = []

        for index, item in enumerate(types):
            if isinstance(item, Mapping):
                key = item.get("id") or item.get("name") or str(index)
            else:
                key = str(index)

            entries.append((str(key), item))

        return entries

    return []


def extract_attacks(collection):
    """
    Recursively extract attack records from dictionaries and lists.

    Handles named attack dictionaries, lists of records, and nested
    category/type containers. Does not deduplicate entries.
    """
    results = []

    if isinstance(collection, (list, tuple)):
        for item in collection:
            if is_attack_record(item):
                attack = normalize_attack(item)

                if attack is not None:
                    results.append(attack)

            elif isinstance(item, (Mapping, list, tuple)):
                results.extend(extract_attacks(item))

        return results

    if not isinstance(collection, Mapping):
        return results

    if is_attack_record(collection):
        attack = normalize_attack(collection)
        return [attack] if attack is not None else []

    # Explicit attack collections take priority as a collection source.
    if "attacks" in collection:
        results.extend(extract_attacks(collection["attacks"]))

    for key, value in collection.items():
        if key == "attacks":
            continue

        if not isinstance(value, (Mapping, list, tuple)):
            continue

        if is_attack_record(value):
            attack = normalize_attack(value, key)

            if attack is not None:
                results.append(attack)
        else:
            results.extend(extract_attacks(value))

    return results


def get_subcategories(category_data):
    """
    Return normalized direct subcategories and their attack counts.

    The attacks_list contains attack records found within each direct
    subcategory. Nested attack groups are recursively extracted.
    """
    if not isinstance(category_data, Mapping):
        return []

    results = []

    for key, value in _type_entries(category_data.get("types", {})):
        if not isinstance(value, Mapping):
            continue

        subcategory = dict(value)
        subcategory["id"] = str(
            value.get("id") or make_slug(key)
        )
        subcategory["name"] = _get_name(value, key)

        if "attacks" in value:
            attacks = extract_attacks(value["attacks"])

        elif "types" in value:
            attacks = extract_attacks(value["types"])

        else:
            attacks = []

            for attack_key, attack_value in value.items():
                if attack_key in METADATA_KEYS:
                    continue

                if is_attack_record(attack_value):
                    attack = normalize_attack(
                        attack_value,
                        attack_key,
                    )

                    if attack is not None:
                        attacks.append(attack)

                elif isinstance(attack_value, (list, tuple)):
                    attacks.extend(extract_attacks(attack_value))

        subcategory["attacks_list"] = attacks
        subcategory["count"] = len(attacks)
        results.append(subcategory)

    return results


def get_category_attacks(category_data):
    """Return all attack records belonging to a category."""
    if not isinstance(category_data, Mapping):
        return extract_attacks(category_data)

    if "types" in category_data:
        attacks = []

        for subcategory in get_subcategories(category_data):
            attacks.extend(subcategory["attacks_list"])

        return attacks

    if "attacks" in category_data:
        return extract_attacks(category_data["attacks"])

    return extract_attacks(category_data)


def _matches_attack(attack, target):
    """Match an attack using its ID, name, or slug."""
    target = str(target)

    return (
        str(attack.get("id", "")) == target
        or str(attack.get("name", "")).casefold() == target.casefold()
        or make_slug(attack.get("name")) == make_slug(target)
        or make_slug(attack.get("id")) == make_slug(target)
    )


def find_attack(category_data, attack_id, subcategory_id=None):
    """
    Find an attack by ID, name, or slug.

    Returns:
        (subcategory, attack)

    Returns (None, None) if no matching attack exists.
    """
    subcategories = get_subcategories(category_data)

    if subcategory_id is not None:
        target_subcategory = str(subcategory_id)

        subcategory = next(
            (
                item
                for item in subcategories
                if (
                    item["id"] == target_subcategory
                    or make_slug(item["name"])
                    == make_slug(target_subcategory)
                )
            ),
            None,
        )

        if subcategory is None:
            return None, None

        for attack in subcategory["attacks_list"]:
            if _matches_attack(attack, attack_id):
                return subcategory, attack

        return subcategory, None

    for subcategory in subcategories:
        for attack in subcategory["attacks_list"]:
            if _matches_attack(attack, attack_id):
                return subcategory, attack

    for attack in get_category_attacks(category_data):
        if _matches_attack(attack, attack_id):
            return None, attack

    return None, None


def get_content(data, content_type):
    """
    Retrieve content using common field aliases.

    Supported types:
        labs, simulations, assessments, case_studies

    Returns a list or dictionary, preserving structured content.
    """
    if not isinstance(data, Mapping):
        return []

    aliases = CONTENT_KEYS.get(content_type, (content_type,))

    for key in aliases:
        value = data.get(key)

        if value is None or value == "":
            continue

        if isinstance(value, (list, tuple)):
            return list(value)

        if isinstance(value, Mapping):
            return dict(value)

        return [value]

    return []


def get_attack_content(
    category_data,
    attack_id,
    content_type,
    subcategory_id=None,
):
    """
    Retrieve content attached to a particular attack.

    Returns an empty list when the attack or content is unavailable.
    """
    _, attack = find_attack(
        category_data,
        attack_id,
        subcategory_id=subcategory_id,
    )

    if attack is None:
        return []

    return get_content(attack, content_type)


def get_category_content(category_data, content_type):
    """Retrieve category-level content for the global content area."""
    return get_content(category_data, content_type)