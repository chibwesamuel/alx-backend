#!/usr/bin/env python3
"""
First, I install the Babel Flask extension and instantiate the Babel
object in my app. I store it in a module-level variable named babel.

I create a Config class that has a LANGUAGES class attribute equal to
["en", "fr"]. I use Config to set Babel’s default locale ("en") and
timezone ("UTC") for the Flask app.
"""

from flask import Flask, render_template
from flask_babel import Babel

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

@app.route('/')
def index() -> str:
    """
    Renders the index.html template.

    Returns:
        str: The rendered template.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run()

