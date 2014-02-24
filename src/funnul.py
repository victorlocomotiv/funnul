import flask

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('applications.html')

if __name__ == '__main__':
    app.debug = True
    app.run()