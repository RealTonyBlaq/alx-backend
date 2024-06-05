#!/usr/bin/env python3
""" Babel """

from flask import Flask, request, render_template
from flask_babel import Babel, _


app = Flask(__name__)


class Config:
    """ Defining the Babel config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determines the best Language """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', strict_slashes=False)
def home():
    """ Returns the 1-index.html template """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
