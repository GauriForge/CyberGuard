
from flask import Blueprint, render_template, redirect, url_for, session

from attacks import ATTACK_CATEGORIES
from data_adapter import (
    get_subcategories,
    get_category_attacks,
    get_attack_content,
)


attack_labs_bp = Blueprint("attack_labs", __name__)


def _login_required():
    """Check whether the user is authenticated."""
    return not session.get("user_id")


def _not_found(message):
    """Render the application's standard not-found page."""
    return render_template("404.html", message=message), 404


def _get_category(category_id):
    """Find a category by its URL identifier."""
    return next(
        (
            category
            for category in ATTACK_CATEGORIES
            if category["id"] == str(category_id)
        ),
        None,
    )


def _get_attack(category, attack_id, subcategory_id=None):
    """Find an attack and its optional subcategory."""
    category_data = category["attacks"]

    if subcategory_id is not None:
        subcategory = next(
            (
                item
                for item in get_subcategories(category_data)
                if item["id"] == str(subcategory_id)
            ),
            None,
        )

        if subcategory is None:
            return None, None

        attack = next(
            (
                item
                for item in subcategory["attacks_list"]
                if str(item.get("id")) == str(attack_id)
                or _slug(item.get("name")) == _slug(attack_id)
            ),
            None,
        )

        return subcategory, attack

    for subcategory in get_subcategories(category_data):
        for attack in subcategory["attacks_list"]:
            if (
                str(attack.get("id")) == str(attack_id)
                or _slug(attack.get("name")) == _slug(attack_id)
            ):
                return subcategory, attack

    for attack in get_category_attacks(category_data):
        if (
            str(attack.get("id")) == str(attack_id)
            or _slug(attack.get("name")) == _slug(attack_id)
        ):
            return None, attack

    return None, None


def _slug(value):
    """Normalize a name for URL matching."""
    import re

    value = str(value or "").strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def _build_lab_context(
    category,
    attack,
    subcategory=None,
):
    """Build the template context for an attack's labs."""
    labs = get_attack_content(
        category["attacks"],
        attack["id"],
        "labs",
        subcategory_id=(
            subcategory["id"] if subcategory else None
        ),
    )

    return {
        "category": category,
        "attack": attack,
        "subcategory": subcategory,
        "labs": labs,
        "lab_count": len(labs),
    }


@attack_labs_bp.route(
    "/attacks/<category_id>/topic/<attack_id>/labs"
)
def attack_labs(category_id, attack_id):
    """Display labs associated with an individual attack."""
    if _login_required():
        return redirect(url_for("auth.login"))

    category = _get_category(category_id)

    if category is None:
        return _not_found("Attack category not found.")

    subcategory, attack = _get_attack(category, attack_id)

    if attack is None:
        return _not_found("Attack topic not found.")

    context = _build_lab_context(
        category,
        attack,
        subcategory,
    )

    return render_template(
        "attack_labs.html",
        **context,
    )


@attack_labs_bp.route(
    "/attacks/<category_id>/<subcategory_id>/<attack_id>/labs"
)
def subcategory_attack_labs(
    category_id,
    subcategory_id,
    attack_id,
):
    """Display labs for an attack inside a subcategory."""
    if _login_required():
        return redirect(url_for("auth.login"))

    category = _get_category(category_id)

    if category is None:
        return _not_found("Attack category not found.")

    subcategory, attack = _get_attack(
        category,
        attack_id,
        subcategory_id=subcategory_id,
    )

    if subcategory is None:
        return _not_found("Attack subcategory not found.")

    if attack is None:
        return _not_found("Attack topic not found.")

    context = _build_lab_context(
        category,
        attack,
        subcategory,
    )

    return render_template(
        "attack_labs.html",
        **context,
    )