from flask import Blueprint, redirect, url_for, session

learning_bp = Blueprint("learning", __name__, url_prefix="/learning")


@learning_bp.route("/")
def learning_home():
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    return redirect(url_for("attacks.attack_categories"))


@learning_bp.route("/<category_id>")
def learning_category(category_id):
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    return redirect(
        url_for(
            "attacks.attack_overview",
            category_id=category_id
        )
    )


@learning_bp.route("/<category_id>/<attack_id>")
def learning_attack(category_id, attack_id):
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    return redirect(
        url_for(
            "attacks.attack_learning",
            category_id=category_id,
            attack_id=attack_id
        )
    )