#!/usr/bin/python3
"""start flask app"""

from flask import Flask, render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def html_num(n):
    """ display html if n is int. """
    n = str(n)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
	""" if else """
	@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
	def numbersandevenness(n):
	"""display a HTML page only if n is an integer"""
	if n % 2 == 0:
		evenness = 'even'
	else:
        	evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
