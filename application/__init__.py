import os
from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix
from application import db, errors


def create_app(test_config=None):
    """ Flask app factory that creates and configure the app.

    Args:
        test_config (str): python configuration filepath

    Returns: Flask application

    """
    app = Flask(__name__,
                instance_relative_config=True,
                instance_path=os.path.abspath("./instance"))

    app.config.from_mapping(SECRET_KEY="dev")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # proxy fix
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # register the database commands
    app.cli.add_command(db.init)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    # HTTP errors
    app.register_error_handler(404, errors.page_not_found)

    # blueprints
    from application import home
    app.register_blueprint(home.bp)

    return app