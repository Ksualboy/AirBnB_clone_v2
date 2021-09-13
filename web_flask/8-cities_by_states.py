#!/usr/bin/python3
'''starts a Flask web application'''

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''AAAAAAAAAAAAAA'''
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())


@app.teardown_appcontext
def teardown(self):
    '''closes the session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
