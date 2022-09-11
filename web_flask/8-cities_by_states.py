#!/usr/bin/python3

"""
List all States through an end point
"""

from flask import Flask, render_template
from models import *
from models import storage
procFlask = Flask(__name__)


@procFlask.teardown_procFlaskcontext
def teardown_db(exception):
    """
    démonter la base de données, pour la réinitialiser.
    """
    storage.close()


@procFlask.route('/cities_by_states', strict_slashes=False)
def statesList():
    """
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    procFlask.run(host='0.0.0.0', port='5000')
