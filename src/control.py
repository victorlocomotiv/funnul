import flask

ctl = flask.Blueprint('control', __name__, url_prefix='/control')

@ctl.route('/')
def homepage():
    return flask.render_template('app_list.html')

@ctl.route('/app/<name>')
def application(name):
    return flask.render_template('app_config.html', name=name)
