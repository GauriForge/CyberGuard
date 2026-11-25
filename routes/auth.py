
import sqlite3

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from models.user_model import (
    create_user,
    get_user_by_email,
    verify_password
)


auth_bp = Blueprint("auth", __name__)

# Authorized CyberGuard administrator email
ADMIN_EMAIL = "ag.gauri7@gmail.com"


@auth_bp.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = get_user_by_email(email)

        if user and verify_password(user, password):

            session.clear()

            session["user_id"] = user["id"]
            session["username"] = user["username"]

            # Grant admin access only to the authorized email.
            if email == ADMIN_EMAIL:
                session["role"] = "admin"
            else:
                session["role"] = "user"

            flash("Login successful.", "success")

            return redirect(url_for("dashboard.dashboard"))

        flash("Invalid email or password.", "error")

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not username or not email or not password:

            flash("Please fill in all required fields.", "error")

        elif len(username) < 3:

            flash("Username must contain at least 3 characters.", "error")

        elif len(password) < 8:

            flash("Password must contain at least 8 characters.", "error")

        elif password != confirm_password:

            flash("Passwords do not match.", "error")

        elif get_user_by_email(email):

            flash("An account with this email already exists.", "error")

        else:

            try:

                create_user(username, email, password)

                flash(
                    "Registration successful. Please log in.",
                    "success"
                )

                return redirect(url_for("auth.login"))

            except sqlite3.IntegrityError:

                flash(
                    "That username or email is already registered.",
                    "error"
                )

    return render_template("register.html")


@auth_bp.route("/logout")
def logout():

    session.clear()

    flash("You have been logged out.", "success")

    return redirect(url_for("auth.login"))
