#!/usr/bin/python3
"""start flask app"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ landing page """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello2():
    """display HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_dynamic(text):
    """Display dynamic text """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
