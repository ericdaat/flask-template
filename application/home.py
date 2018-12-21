import flask

bp = flask.Blueprint("home", __name__)


@bp.route("/")
def home():
    return flask.render_template("home/home.html")