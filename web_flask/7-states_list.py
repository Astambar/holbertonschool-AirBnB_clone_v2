#!/usr/bin/python3
""" Module that start a Flask Webb app"""
from flask import Flask, render_template
from ..models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    démonter la base de données, pour la réinitialiser.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def index():
    """display a HTML page"""
    data = storage.all("State")
    return render_template('7-states_list.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
