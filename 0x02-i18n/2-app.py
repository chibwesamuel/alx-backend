#!/usr/bin/env python3
"""
First, I install the Babel Flask extension and instantiate the Babel object
in my app. I store it in a module-level variable named babel.

I create a Config class that has a LANGUAGES class attribute equal
to ["en", "fr"]. I use Config to set Babel’s default locale ("en") and
timezone ("UTC") for the Flask app.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, Locale

app = Flask(__name__)
babel = Babel(app)

class Config:
    """
    Configuration class with LANGUAGES, BABEL_DEFAULT_LOCALE, and
    BABEL_DEFAULT_TIMEZONE attributes.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale() -> str:
    """
    Get the best-matching language based on the user's Accept-Language header and supported languages.

    Returns:
        str: The best-matching language code (e.g., 'en' or 'fr').
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

