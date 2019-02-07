import flask
from application.model import User

bp = flask.Blueprint("home", __name__)


@bp.route("/")
def home():
    users = User.query.all()
    flask.current_app.logger.info("{0} user(s) in the db".format(len(users)))

    return flask.render_template("home/home.html")
