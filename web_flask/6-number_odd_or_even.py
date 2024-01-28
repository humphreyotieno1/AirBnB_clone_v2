#!/usr/bin/python3
"""script to start flask web server"""
from flask import Flask, render_template

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
@app.route("/c", strict_slashes=False)
def myvar(text="is cool"):
    """the c section"""
    return "C {}".format(text.replace("_", " "))

@app.route("/python/<text>/", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def myPythonText(text="is cool"):
    """python section"""
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """number section"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_two(n):
    """number_template section"""
    return render_template('5-number.html', content=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """odd or even section"""
    if n % 2 == 0:
        p = 'even'
    else:
        p = 'odd'
    return render_template('6-number_odd_or_even.html', content=n, even_odd=p)
  
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
