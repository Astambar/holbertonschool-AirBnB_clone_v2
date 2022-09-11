#!/usr/bin/python3

"""
Créer un itinéraire pour notre site Web
"""

from flask import Flask
procFlask = Flask(__name__)


@procFlask.route('/', strict_slashes=False)
def index():
    """
        Afficher Hello HBNB à la racine
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    procFlask.run(host='0.0.0.0', port='5000')
