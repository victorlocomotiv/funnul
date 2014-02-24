import flask

v1 = flask.Blueprint('v1', __name__, url_prefix='/api/v1')

@v1.route('/')
def list_applications():
    return 'hello world'
    pass