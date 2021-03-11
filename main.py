import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def greeting():
    return "hello there", 200

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=8081, debug=True)