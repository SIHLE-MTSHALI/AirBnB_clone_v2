#!/usr/bin/python3
"""Starts a Flask web application."""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Close the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with the list of all State objects"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=sorted(
        states, key=lambda s: s.name))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
