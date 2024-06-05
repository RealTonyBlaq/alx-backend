#!/usr/bin/env python3
""" Babel """

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Defining the Babel config class """
    LANGUAGES = ["en", "fr"]

    @babel.default_locale
    def default_locale(self):
        """ Sets Babel's default locale """
        return "en"

    @babel.default_timezone
    def timezone(self):
        """ sets the default timezone """
        return "UTC"


@app.route('/', strict_slashes=False)
def home():
    """ Returns the 1-index.html template """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
