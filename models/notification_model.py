from database.db import get_db


def create_notification(user_id, title, message):
    db = get_db()

    cursor = db.execute(
        """
        INSERT INTO notifications (user_id, title, message)
        VALUES (?, ?, ?)
        """,
        (user_id, title, message)
    )

    db.commit()

    return cursor.lastrowid


def get_user_notifications(user_id):
    db = get_db()

    return db.execute(
        """
        SELECT *
        FROM notifications
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,)
    ).fetchall()


def get_unread_notification_count(user_id):
    db = get_db()

    result = db.execute(
        """
        SELECT COUNT(*) AS unread_count
        FROM notifications
        WHERE user_id = ? AND is_read = 0
        """,
        (user_id,)
    ).fetchone()

    return result["unread_count"]


def mark_notification_as_read(notification_id, user_id):
    db = get_db()

    db.execute(
        """
        UPDATE notifications
        SET is_read = 1
        WHERE id = ? AND user_id = ?
        """,
        (notification_id, user_id)
    )

    db.commit()


def mark_all_notifications_as_read(user_id):
    db = get_db()

    db.execute(
        """
        UPDATE notifications
        SET is_read = 1
        WHERE user_id = ?
        """,
        (user_id,)
    )

    db.commit()


def delete_notification(notification_id, user_id):
    db = get_db()

    db.execute(
        """
        DELETE FROM notifications
        WHERE id = ? AND user_id = ?
        """,
        (notification_id, user_id)
    )

    db.commit()