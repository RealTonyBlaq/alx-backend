#!/usr/bin/env python3
""" Simple Flask app """

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Renders a template """
    return render_template('index.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
