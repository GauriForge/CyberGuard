from flask import Blueprint, render_template, redirect, url_for, session

from database.db import get_db

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():
    # Redirect users who are not logged in.
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    db = get_db()
    user_id = session["user_id"]

    # --------------------------------------------------
    # ATTACK CATEGORIES
    # --------------------------------------------------
    # Count the actual categories defined in routes/attacks.py.
    try:
        from routes.attacks import ATTACK_CATEGORIES

        total_categories = len(ATTACK_CATEGORIES)
    except (ImportError, AttributeError, TypeError):
        total_categories = 14

    # --------------------------------------------------
    # INCIDENT STATISTICS
    # --------------------------------------------------
    total_incidents = db.execute(
        """
        SELECT COUNT(*) AS total
        FROM incidents
        WHERE user_id = ?
        """,
        (user_id,),
    ).fetchone()["total"]

    open_incidents = db.execute(
        """
        SELECT COUNT(*) AS total
        FROM incidents
        WHERE user_id = ?
          AND LOWER(status) = 'open'
        """,
        (user_id,),
    ).fetchone()["total"]

    # --------------------------------------------------
    # ASSESSMENT STATISTICS
    # --------------------------------------------------
    assessment_summary = db.execute(
        """
        SELECT
            COUNT(*) AS total_attempts,
            COALESCE(AVG(percentage), 0) AS average_percentage,
            COALESCE(MAX(percentage), 0) AS highest_percentage
        FROM assessment_results
        WHERE user_id = ?
        """,
        (user_id,),
    ).fetchone()

    total_assessments = assessment_summary["total_attempts"]
    average_score = round(
        float(assessment_summary["average_percentage"] or 0), 1
    )
    highest_score = round(
        float(assessment_summary["highest_percentage"] or 0), 1
    )

    # --------------------------------------------------
    # NOTIFICATIONS
    # --------------------------------------------------
    unread_notifications = db.execute(
        """
        SELECT COUNT(*) AS total
        FROM notifications
        WHERE user_id = ?
          AND is_read = 0
        """,
        (user_id,),
    ).fetchone()["total"]

    # --------------------------------------------------
    # RECENT ASSESSMENT RESULTS
    # --------------------------------------------------
    recent_results = db.execute(
        """
        SELECT *
        FROM assessment_results
        WHERE user_id = ?
        ORDER BY completed_at DESC, id DESC
        LIMIT 5
        """,
        (user_id,),
    ).fetchall()

    # --------------------------------------------------
    # RECENT INCIDENTS
    # --------------------------------------------------
    recent_incidents = db.execute(
        """
        SELECT *
        FROM incidents
        WHERE user_id = ?
        ORDER BY created_at DESC, id DESC
        LIMIT 5
        """,
        (user_id,),
    ).fetchall()

    # --------------------------------------------------
    # RENDER DASHBOARD
    # --------------------------------------------------
    return render_template(
        "dashboard.html",
        username=session.get("username", "User"),
        total_categories=total_categories,
        total_incidents=total_incidents,
        open_incidents=open_incidents,
        assessment_summary=assessment_summary,
        total_assessments=total_assessments,
        average_score=average_score,
        highest_score=highest_score,
        unread_notifications=unread_notifications,
        recent_results=recent_results,
        recent_incidents=recent_incidents,
    )