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

from database.db import get_db
from models.incident_model import (
    create_incident,
    get_user_incidents,
    get_all_incidents,
    update_incident_status,
    update_incident_severity,
)

incidents_bp = Blueprint("incidents", __name__)

VALID_CATEGORIES = {
    "Phishing",
    "Malware",
    "Unauthorized Access",
    "Data Breach",
    "Suspicious Activity",
    "Other",
}

VALID_SEVERITIES = {"Low", "Medium", "High", "Critical"}
VALID_STATUSES = {"Open", "In Progress", "Resolved", "Closed"}


def is_admin():
    return session.get("role") == "admin"


def require_login():
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))
    return None


def get_incident_by_id(incident_id):
    db = get_db()

    return db.execute(
        """
        SELECT incidents.*, users.username
        FROM incidents
        LEFT JOIN users ON incidents.user_id = users.id
        WHERE incidents.id = ?
        """,
        (incident_id,),
    ).fetchone()


def can_access_incident(incident):
    if is_admin():
        return True

    return str(incident["user_id"]) == str(session.get("user_id"))


@incidents_bp.route("/incidents/report", methods=["GET", "POST"])
def report_incident():
    login_redirect = require_login()
    if login_redirect:
        return login_redirect

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        category = request.form.get("category", "").strip()
        severity = request.form.get("severity", "Medium").strip()

        if not title or not description:
            flash(
                "Please provide an incident title and description.",
                "error",
            )

        elif len(title) > 150:
            flash(
                "The title must be 150 characters or fewer.",
                "error",
            )

        elif len(description) > 5000:
            flash(
                "The description must be 5000 characters or fewer.",
                "error",
            )

        elif category not in VALID_CATEGORIES:
            flash("Please select a valid incident category.", "error")

        elif severity not in VALID_SEVERITIES:
            flash("Please select a valid severity level.", "error")

        else:
            create_incident(
                user_id=session["user_id"],
                title=title,
                description=description,
                category=category,
                severity=severity,
            )

            flash(
                "Your incident report has been submitted.",
                "success",
            )
            return redirect(url_for("incidents.my_incidents"))

    return render_template(
        "incident_reporting.html",
        categories=sorted(VALID_CATEGORIES),
        severities=["Low", "Medium", "High", "Critical"],
    )


@incidents_bp.route("/incidents", methods=["GET"])
def my_incidents():
    login_redirect = require_login()
    if login_redirect:
        return login_redirect

    admin = is_admin()

    incidents = (
        get_all_incidents()
        if admin
        else get_user_incidents(session["user_id"])
    )

    return render_template(
        "incident_management.html",
        incidents=incidents,
        incident=None,
        is_admin=admin,
        statuses=sorted(VALID_STATUSES),
        severities=["Low", "Medium", "High", "Critical"],
    )


@incidents_bp.route("/incidents/<int:incident_id>", methods=["GET"])
def incident_detail(incident_id):
    login_redirect = require_login()
    if login_redirect:
        return login_redirect

    incident = get_incident_by_id(incident_id)

    if incident is None:
        abort(404)

    if not can_access_incident(incident):
        abort(403)

    return render_template(
        "incident_management.html",
        incident=incident,
        incidents=[incident],
        is_admin=is_admin(),
        statuses=sorted(VALID_STATUSES),
        severities=["Low", "Medium", "High", "Critical"],
    )


@incidents_bp.route(
    "/incidents/<int:incident_id>/update",
    methods=["POST"],
)
def update_incident(incident_id):
    login_redirect = require_login()
    if login_redirect:
        return login_redirect

    if not is_admin():
        abort(403)

    incident = get_incident_by_id(incident_id)

    if incident is None:
        abort(404)

    status = request.form.get("status", "").strip()
    severity = request.form.get("severity", "").strip()

    if status not in VALID_STATUSES:
        flash("Please select a valid incident status.", "error")

    elif severity not in VALID_SEVERITIES:
        flash("Please select a valid severity level.", "error")

    else:
        update_incident_status(incident_id, status)
        update_incident_severity(incident_id, severity)

        flash(
            "Incident details updated successfully.",
            "success",
        )

    return redirect(url_for("incidents.my_incidents"))