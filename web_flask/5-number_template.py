#!/usr/bin/python3

"""
Create a route for our website
"""

from flask import Flask, escape, render_template
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
    return 'C ' + text.replace('_', ' ')


@procFlask.route('/python', strict_slashes=False)
@procFlask.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """
    Display python with the parameter, that got a default value
    """
    return 'Python ' + text.replace('_', ' ')


@procFlask.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """
    Return value
    """
    return '{} is a number'.format(n)


@procFlask.route('/number_template/<int:n>', strict_slashes=False)
def templateNumber(n):
    """
    Return a template with the value of the int
    """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    procFlask.run(host='0.0.0.0', port='5000')
