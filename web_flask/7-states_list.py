#!/usr/bin/python3
''' starts a Flask web application '''

from flask import Flask
from flask import render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def myfunction():
    ''' displays all the states in the html '''
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def closer(self):
    ''' removes the current SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
