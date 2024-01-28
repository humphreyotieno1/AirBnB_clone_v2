#!/usr/bin/python3
"""starting a flask web server"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """home section"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb section"""
    return "HBNB"

@app.route("/c/<text>/", strict_slashes=False)
def myvar(text="is cool"):
    """the c section"""
    return "C {}".format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
