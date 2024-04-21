#!/usr/bin/python3
"""start flask app"""
from flask import Flask
app = Flask(__name__)


@app.route = "/"
"""Landing page"""
def hello():
	return '<h1>Hello HBNB!'


if __name__ = '__main__':
	app.run(host='0.0.0.0', port=5000)
