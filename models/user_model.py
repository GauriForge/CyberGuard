import sqlite3

from werkzeug.security import generate_password_hash, check_password_hash
from database.db import get_db


def create_user(username, email, password, role="user"):
    db = get_db()
    password_hash = generate_password_hash(password)

    try:
        cursor = db.execute(
            """
            INSERT INTO users (username, email, password_hash, role)
            VALUES (?, ?, ?, ?)
            """,
            (username.strip(), email.strip().lower(), password_hash, role)
        )
        db.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        db.rollback()
        raise


def get_user_by_id(user_id):
    db = get_db()
    return db.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()


def get_user_by_email(email):
    db = get_db()
    return db.execute(
        "SELECT * FROM users WHERE email = ?",
        (email.strip().lower(),)
    ).fetchone()


def get_user_by_username(username):
    db = get_db()
    return db.execute(
        "SELECT * FROM users WHERE username = ?",
        (username.strip(),)
    ).fetchone()


def verify_password(user, password):
    if user is None:
        return False

    return check_password_hash(user["password_hash"], password)


def update_user_profile(user_id, username, email):
    db = get_db()

    try:
        db.execute(
            """
            UPDATE users
            SET username = ?, email = ?
            WHERE id = ?
            """,
            (username.strip(), email.strip().lower(), user_id)
        )
        db.commit()
        return True
    except sqlite3.IntegrityError:
        db.rollback()
        raise


def update_user_password(user_id, new_password):
    db = get_db()
    password_hash = generate_password_hash(new_password)

    db.execute(
        """
        UPDATE users
        SET password_hash = ?
        WHERE id = ?
        """,
        (password_hash, user_id)
    )
    db.commit()


def delete_user(user_id):
    db = get_db()

    db.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )
    db.commit()