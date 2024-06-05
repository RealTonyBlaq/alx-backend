#!/usr/bin/env python3
""" Simple Flask app """

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strick_slashes=False)
def home():
    """ Renders a template """
    
