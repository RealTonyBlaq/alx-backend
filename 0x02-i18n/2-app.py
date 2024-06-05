#!/usr/bin/env python3
""" Babel """

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Defining the Babel config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Determines the best Language """
    return 


@app.route('/', strict_slashes=False)
def home():
    """ Returns the 1-index.html template """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
