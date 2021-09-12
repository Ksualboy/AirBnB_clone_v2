#!/usr/bin/python3
''' starts a Flask web application '''

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)