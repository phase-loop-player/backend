from flask import Flask

# pylint: disable=invalid-name
app = Flask(__name__)


@app.route("/healthz")
def health():
    return ("", 204)


@app.route("/")
def hello_world():
    return "hello world!"
