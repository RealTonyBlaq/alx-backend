#!/usr/bin/env python3
""" Babel """

from flask import Flask
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
