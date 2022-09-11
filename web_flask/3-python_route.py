#!/usr/bin/python3

"""
Create a route for our website
"""

from flask import Flask
procFlask = Flask(__name__)

def defaultTxt(persistantTxt, text):
    return persistantTxt + text.replace('_', ' ')

@procFlask.route('/', strict_slashes=False)
def index():
    """
    Display Hello HBNB to the root
    """
    return 'Hello HBNB!'


@procFlask.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display HBNB to the according route
    """
    return 'HBNB'


@procFlask.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    """
    Display c with the parameter
    """
    return defaultTxt('C ', text)


@procFlask.route('/python', strict_slashes=False)
@procFlask.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """
    Display python with the parameter, that got a default value
    """
    return defaultTxt('Python ', text)


if __name__ == '__main__':
    procFlask.run(host='0.0.0.0', port='5000')