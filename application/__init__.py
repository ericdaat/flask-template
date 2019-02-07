import os
import logging
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from application import errors
from application.model import db, init_db_command


def create_app():
    """ Flask app factory that creates and configure the app.

    Args:
        test_config (str): python configuration filepath

    Returns: Flask application

    """
    app = Flask(__name__, instance_relative_config=True)
    app.logger.setLevel(logging.DEBUG)
    app.config.from_object('application.config.DefaultConfig')
    db.init_app(app)

    # instance dir
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register cli commands
    app.cli.add_command(init_db_command)

    # proxy fix
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # HTTP errors
    app.register_error_handler(404, errors.page_not_found)

    # blueprints
    from application import home
    app.register_blueprint(home.bp)

    return app
