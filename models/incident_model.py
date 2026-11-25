from database.db import get_db


def create_incident(
    user_id,
    title,
    description,
    category=None,
    severity="Medium"
):
    db = get_db()

    cursor = db.execute(
        """
        INSERT INTO incidents (
            user_id,
            title,
            description,
            category,
            severity
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            user_id,
            title,
            description,
            category,
            severity
        )
    )

    db.commit()

    return cursor.lastrowid


def get_incident_by_id(incident_id):
    db = get_db()

    return db.execute(
        "SELECT * FROM incidents WHERE id = ?",
        (incident_id,)
    ).fetchone()


def get_user_incidents(user_id):
    db = get_db()

    return db.execute(
        """
        SELECT *
        FROM incidents
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,)
    ).fetchall()


def get_all_incidents():
    db = get_db()

    return db.execute(
        """
        SELECT incidents.*, users.username
        FROM incidents
        LEFT JOIN users ON incidents.user_id = users.id
        ORDER BY incidents.created_at DESC
        """
    ).fetchall()


def update_incident_status(incident_id, status):
    db = get_db()

    db.execute(
        """
        UPDATE incidents
        SET status = ?
        WHERE id = ?
        """,
        (status, incident_id)
    )

    db.commit()


def update_incident_severity(incident_id, severity):
    db = get_db()

    db.execute(
        """
        UPDATE incidents
        SET severity = ?
        WHERE id = ?
        """,
        (severity, incident_id)
    )

    db.commit()


def delete_incident(incident_id):
    db = get_db()

    db.execute(
        "DELETE FROM incidents WHERE id = ?",
        (incident_id,)
    )

    db.commit()