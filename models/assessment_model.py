
from database.db import get_db


def save_assessment_result(
    user_id,
    assessment_name,
    score,
    total_questions,
):
    """Save an assessment result and return its database ID."""

    if user_id is None:
        raise ValueError("A valid user ID is required.")

    if not isinstance(assessment_name, str) or not assessment_name.strip():
        raise ValueError("Assessment name is required.")

    if isinstance(score, bool) or not isinstance(score, int):
        raise ValueError("Score must be an integer.")

    if isinstance(total_questions, bool) or not isinstance(total_questions, int):
        raise ValueError("Total questions must be an integer.")

    if total_questions < 0:
        raise ValueError("Total questions cannot be negative.")

    if score < 0 or score > total_questions:
        raise ValueError(
            "Score must be between zero and the total number of questions."
        )

    percentage = (
        round((score / total_questions) * 100, 2)
        if total_questions > 0
        else 0.0
    )

    db = get_db()

    cursor = db.execute(
        """
        INSERT INTO assessment_results (
            user_id,
            assessment_name,
            score,
            total_questions,
            percentage
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            user_id,
            assessment_name.strip(),
            score,
            total_questions,
            percentage,
        ),
    )

    db.commit()

    return cursor.lastrowid


def get_assessment_result(result_id):
    """Retrieve one assessment result by its ID."""

    db = get_db()

    return db.execute(
        """
        SELECT *
        FROM assessment_results
        WHERE id = ?
        """,
        (result_id,),
    ).fetchone()


def get_user_assessment_results(user_id):
    """Retrieve assessment history for a specific user."""

    db = get_db()

    return db.execute(
        """
        SELECT *
        FROM assessment_results
        WHERE user_id = ?
        ORDER BY completed_at DESC, id DESC
        """,
        (user_id,),
    ).fetchall()


def get_user_assessment_summary(user_id):
    """Return assessment totals and performance statistics."""

    db = get_db()

    return db.execute(
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


def delete_assessment_result(result_id):
    """Delete an assessment result by its ID."""

    db = get_db()

    db.execute(
        """
        DELETE FROM assessment_results
        WHERE id = ?
        """,
        (result_id,),
    )

    db.commit()