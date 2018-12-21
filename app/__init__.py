import os

from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix
from db import session
from .errors import page_not_found


def create_app(test_config=None):
    # create and configure the app
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

    # register index
    @app.route("/status")
    def status():
        return "So far so good"

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        session.remove()

    # HTTP errors
    app.register_error_handler(404, page_not_found)

    # blueprints

    app.add_url_rule("/", endpoint="index")

    return app