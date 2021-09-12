#!/usr/bin/python3
''' starts a Flask web application '''

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    ''' puts something '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' same but for hbnb'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    '''same but with a variable'''
    new_text = text.replace("_", " ")
    return ("C " + new_text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    ''' same but with python '''
    new_text = text.replace("_", " ")
    return ("Python " + new_text)


@app.route("/number/<int:n>", strict_slashes=False)
def int_check(n):
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_int_check(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
