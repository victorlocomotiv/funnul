import flask

from api_v1 import v1
from control import ctl

app = flask.Flask(__name__)
app.register_blueprint(v1)
app.register_blueprint(ctl)

@app.route('/')
def homepage_control():
    return flask.redirect(ctl.url_prefix, 301)

if __name__ == '__main__':
    app.debug = True
    app.run()