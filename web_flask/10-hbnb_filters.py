#!/usr/bin/python3

"""
List all States through an end point
"""

from flask import Flask, render_template
from models import *
from models import storage
procFlask = Flask(__name__)


@procFlask.teardown_appcontext
def teardown_db(exception):
    """
    démonter la base de données, pour la réinitialiser.
    """
    storage.close()


@procFlask.route('/states', strict_slashes=False)
def statesList():
    """
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('9-states.html', states=states, choice=True)


@procFlask.route('/states/<id>', strict_slashes=False)
def statesCityList(id):
    """
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    for state in states:
        if state.id == id:
            return render_template('9-states.html', states=state, choice=False)
    return render_template('9-states.html', states=False, choice=False)


@procFlask.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    cities = []
    for state in states:
        cities.extend(iter(state.cities))

    return render_template('10-hbnb_filters.html',
                            states=states, state_cities=cities,
                            amenities=amenities)

if __name__ == '__main__':
    procFlask.run(host='0.0.0.0', port='5000')
