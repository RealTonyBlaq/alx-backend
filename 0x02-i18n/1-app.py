#!/usr/bin/env python3
""" Babel """

from flask import Flask
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Defining the Babel config class """
    LANGUAGES = ["en", "fr"]

    @babel.default_locale
    def default_locale(self):
        """ Sets Babel's default """
