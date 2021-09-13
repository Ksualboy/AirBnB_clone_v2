#!/usr/bin/python3
'''starts a Flask web application'''

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def mystates(id=None):
    '''AAAAAAAAAAAAAA'''
    all_states = storage.all(State)
    if id:
        xd = '{}.{}'.format('State', id)
        if xd in all_states:
            all_states = all_states[xd]
        else:
            all_states = None
    else:
        all_states = storage.all(State).values()
    return render_template('10-hbnb_filters.html', states=all_states, id=id)


@app.teardown_appcontext
def teardown(self):
    '''closes the session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
