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


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def dynamic2(text='is cool'):
    """ dynamic text"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if type(n) is int:
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
