#!/usr/bin/env python3
""" Babel """

from flask import Flask, g, request, render_template
from flask_babel import Babel


app = Flask(__name__)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Defining the Babel config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Determines the best Language """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user() -> dict:
    """ Retrieves a user dictionary """
    try:
        user_id = int(request.args.get('login_as'))
    except (ValueError, TypeError):
        return None

    return users.get(user_id)


@app.before_request
def before_request():
    """
    Executed before other functions and sets user on global to flask.g.user
    """
    g.user = get_user()


@app.route('/', strict_slashes=False)
def home():
    """ Returns the 5-index.html template """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
