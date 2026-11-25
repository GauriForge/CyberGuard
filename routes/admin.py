
from functools import wraps

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session,
    flash,
)

from database.db import get_db


admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


VALID_STATUSES = {"Open", "In Progress", "Resolved", "Closed"}
VALID_SEVERITIES = {"Low", "Medium", "High", "Critical"}


def admin_required(view):
    """Restrict access to logged-in users with admin privileges."""

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if not session.get("user_id"):
            return redirect(url_for("auth.login"))

        if session.get("role") != "admin":
            flash(
                "Access denied. Admin privileges are required.",
                "error",
            )
            return redirect(url_for("dashboard.dashboard"))

        return view(*args, **kwargs)

    return wrapped_view


@admin_bp.route("/")
@admin_required
def dashboard():

    db = get_db()

    total_users = db.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]

    total_incidents = db.execute(
        "SELECT COUNT(*) FROM incidents"
    ).fetchone()[0]

    open_incidents = db.execute(
        """
        SELECT COUNT(*)
        FROM incidents
        WHERE status NOT IN ('Resolved', 'Closed')
        """
    ).fetchone()[0]

    recent_incidents = db.execute(
        """
        SELECT *
        FROM incidents
        ORDER BY id DESC
        LIMIT 5
        """
    ).fetchall()

    return render_template(
        "admin_dashboard.html",
        is_admin=True,
        total_users=total_users,
        total_incidents=total_incidents,
        open_incidents=open_incidents,
        recent_incidents=recent_incidents,
    )


@admin_bp.route("/incidents")
@admin_required
def incidents():

    db = get_db()

    all_incidents = db.execute(
        """
        SELECT incidents.*, users.username
        FROM incidents
        LEFT JOIN users ON incidents.user_id = users.id
        ORDER BY incidents.id DESC
        """
    ).fetchall()

    under_investigation = sum(
        1 for incident in all_incidents
        if incident["status"] == "In Progress"
    )

    resolved_incidents = sum(
        1 for incident in all_incidents
        if incident["status"] == "Resolved"
    )

    return render_template(
        "incident_management.html",
        incidents=all_incidents,
        total_incidents=len(all_incidents),
        under_investigation=under_investigation,
        resolved_incidents=resolved_incidents,
        is_admin=True,
        statuses=sorted(VALID_STATUSES),
        severities=["Low", "Medium", "High", "Critical"],
    )
