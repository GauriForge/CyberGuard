
import os


class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY")

    if not SECRET_KEY:
        SECRET_KEY = "cyberguard-development-key-change-before-deployment"

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    DATABASE_PATH = os.path.join(
        BASE_DIR,
        "database",
        "cyberguard.db"
    )

    DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"

    # Enable secure cookies when deployed over HTTPS.
    SESSION_COOKIE_SECURE = (
        os.environ.get("FLASK_ENV", "development") == "production"
    )
