from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session,
    flash,
    abort,
)

from models.notification_model import (
    get_user_notifications,
    get_unread_notification_count,
    mark_notification_as_read,
    mark_all_notifications_as_read,
    delete_notification,
)

notifications_bp = Blueprint("notifications", __name__)


@notifications_bp.route("/notifications", methods=["GET"])
def notifications():
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]

    notification_list = get_user_notifications(user_id)
    unread_count = get_unread_notification_count(user_id)

    return render_template(
        "notification.html",
        notifications=notification_list,
        unread_count=unread_count,
    )


@notifications_bp.route(
    "/notifications/<int:notification_id>/read",
    methods=["POST"],
)
def mark_read(notification_id):
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]
    notification_list = get_user_notifications(user_id)

    if not any(
        int(item["id"]) == notification_id
        for item in notification_list
    ):
        abort(404)

    mark_notification_as_read(notification_id, user_id)

    flash("Notification marked as read.", "success")
    return redirect(url_for("notifications.notifications"))


@notifications_bp.route(
    "/notifications/read-all",
    methods=["POST"],
)
def mark_all_read():
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    mark_all_notifications_as_read(session["user_id"])

    flash("All notifications marked as read.", "success")
    return redirect(url_for("notifications.notifications"))


@notifications_bp.route(
    "/notifications/<int:notification_id>/delete",
    methods=["POST"],
)
def remove_notification(notification_id):
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    user_id = session["user_id"]
    notification_list = get_user_notifications(user_id)

    if not any(
        int(item["id"]) == notification_id
        for item in notification_list
    ):
        abort(404)

    delete_notification(notification_id, user_id)

    flash("Notification deleted.", "success")
    return redirect(url_for("notifications.notifications"))