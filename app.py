
from flask import Flask

from database.db import init_app as init_database


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize the database and register connection cleanup.
    init_database(app)

    # Import blueprints inside the factory to avoid circular imports.
    from routes.auth import auth_bp
    from routes.dashboard import dashboard_bp
    from routes.attacks import attacks_bp
    from routes.labs import labs_bp
    from routes.assessments import assessments_bp
    from routes.incidents import incidents_bp
    from routes.help_centre import help_centre_bp
    from routes.resources import resources_bp
    from routes.roadmap import roadmap_bp
    from routes.profile import profile_bp
    from routes.notifications import notifications_bp
    from routes.admin import admin_bp
    from routes.learning import learning_bp
    from routes.careers import careers_bp

    blueprints = (
        auth_bp,
        dashboard_bp,
        attacks_bp,
        labs_bp,
        assessments_bp,
        incidents_bp,
        help_centre_bp,
        resources_bp,
        roadmap_bp,
        profile_bp,
        notifications_bp,
        admin_bp,
        learning_bp,
        careers_bp,
    )

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)