
import os
import sqlite3

from flask import current_app, g


def get_db():
    """Return the SQLite connection for the current Flask context."""

    if "db" not in g:
        database_path = current_app.config.get("DATABASE_PATH")

        if not database_path:
            raise RuntimeError(
                "DATABASE_PATH is not configured in the Flask application."
            )

        database_path = os.path.abspath(database_path)
        database_directory = os.path.dirname(database_path)

        os.makedirs(database_directory, exist_ok=True)

        g.db = sqlite3.connect(
            database_path,
            timeout=10,
        )

        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")

    return g.db


def close_db(error=None):
    """Close the database connection at the end of the app context."""

    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Create the application tables if they do not already exist."""

    db = get_db()

    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT,
            severity TEXT NOT NULL DEFAULT 'Medium',
            status TEXT NOT NULL DEFAULT 'Open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
                ON DELETE SET NULL
        );

        CREATE TABLE IF NOT EXISTS assessment_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            assessment_name TEXT NOT NULL,
            score INTEGER NOT NULL DEFAULT 0,
            total_questions INTEGER NOT NULL DEFAULT 0,
            percentage REAL NOT NULL DEFAULT 0,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
                ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            message TEXT NOT NULL,
            is_read INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
                ON DELETE CASCADE
        );
        """
    )

    db.commit()


def init_app(app):
    """Register database cleanup and initialize database tables."""

    app.teardown_appcontext(close_db)

    with app.app_context():
        init_db()