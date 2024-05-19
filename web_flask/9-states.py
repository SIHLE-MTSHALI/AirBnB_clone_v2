#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Displays a HTML page with a list of states or cities by state"""
    states = storage.all(State).values()
    if id is None:
        states = sorted(states, key=lambda state: state.name)
        return render_template('9-states.html', states=states)
    else:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', state=state)
        return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
