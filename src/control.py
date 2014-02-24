import flask

ctl = flask.Blueprint('control', __name__, url_prefix='/control')

@ctl.route('/')
def homepage():
    return flask.render_template('applications.html')
