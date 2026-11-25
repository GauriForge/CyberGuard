
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    session,
    flash,
    abort,
)
import sqlite3

from models.user_model import (
    get_user_by_id,
    get_user_by_email,
    get_user_by_username,
    update_user_profile,
    update_user_password,
    verify_password,
)

profile_bp = Blueprint("profile", __name__)

# Reserved email for the CyberGuard administrator.
ADMIN_EMAIL = "ag.gauri7@gmail.com"


@profile_bp.route("/profile", methods=["GET", "POST"])
def profile():

    user_id = session.get("user_id")

    if not user_id:
        return redirect(url_for("auth.login"))

    user = get_user_by_id(user_id)

    if user is None:
        session.clear()
        flash("Please log in again to continue.", "error")
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        action = request.form.get("action", "update_profile")

        if action == "update_profile":

            username = request.form.get("username", "").strip()
            email = request.form.get("email", "").strip().lower()

            if not username or not email:

                flash("Username and email are required.", "error")

            elif len(username) < 3 or len(username) > 50:

                flash(
                    "Username must contain between 3 and 50 characters.",
                    "error",
                )

            elif (
                len(email) > 254
                or "@" not in email
                or email.startswith("@")
                or email.endswith("@")
                or "." not in email.rsplit("@", 1)[-1]
            ):

                flash("Please enter a valid email address.", "error")

            elif (
                email == ADMIN_EMAIL
                and user["email"].strip().lower() != ADMIN_EMAIL
            ):

                flash(
                    "This email address is reserved for the administrator.",
                    "error",
                )

            elif (
                user["email"].strip().lower() == ADMIN_EMAIL
                and email != ADMIN_EMAIL
            ):

                flash(
                    "The administrator email address cannot be changed.",
                    "error",
                )

            else:

                existing_email = get_user_by_email(email)
                existing_username = get_user_by_username(username)

                if (
                    existing_email
                    and existing_email["id"] != user["id"]
                ):

                    flash(
                        "That email address is already in use.",
                        "error",
                    )

                elif (
                    existing_username
                    and existing_username["id"] != user["id"]
                ):

                    flash(
                        "That username is already in use.",
                        "error",
                    )

                else:

                    try:

                        update_user_profile(
                            user["id"],
                            username,
                            email,
                        )

                        session["username"] = username

                        flash(
                            "Profile updated successfully.",
                            "success",
                        )

                        return redirect(url_for("profile.profile"))

                    except sqlite3.IntegrityError:

                        flash(
                            "The username or email address is already in use.",
                            "error",
                        )

        elif action == "change_password":

            current_password = request.form.get(
                "current_password", ""
            )

            new_password = request.form.get("new_password", "")

            confirm_password = request.form.get(
                "confirm_password", ""
            )

            if (
                not current_password
                or not new_password
                or not confirm_password
            ):

                flash(
                    "Please complete all password fields.",
                    "error",
                )

            elif not verify_password(user, current_password):

                flash(
                    "Your current password is incorrect.",
                    "error",
                )

            elif len(new_password) < 8:

                flash(
                    "Your new password must contain at least 8 characters.",
                    "error",
                )

            elif new_password != confirm_password:

                flash(
                    "The new passwords do not match.",
                    "error",
                )

            elif current_password == new_password:

                flash(
                    "Choose a different password from your current one.",
                    "error",
                )

            else:

                update_user_password(user["id"], new_password)

                flash(
                    "Password changed successfully.",
                    "success",
                )

                return redirect(url_for("profile.profile"))

        else:

            abort(400)

        user = get_user_by_id(user_id)

    return render_template(
        "profile.html",
        user=user,
        topics_completed=0,
        labs_completed=0,
        assessments_completed=0,
        overall_progress=0,
    )
