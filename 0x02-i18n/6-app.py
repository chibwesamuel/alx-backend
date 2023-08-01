#!/usr/bin/env python3
"""
6. Use user locale
In this task, I change my get_locale function to use a user’s preferred
local if it is supported.

The order of priority is as follows:
    - Locale from URL parameters
    - Locale from user settings
    - Locale from request header
    - Default locale
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

# Mocked user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id: int) -> dict or None:
    """
    Returns a user dictionary based on the provided user_id.

    Args:
        user_id (int): The ID of the user.

    Returns:
        dict or None: The user dictionary if found, otherwise None.
    """
    return users.get(user_id)

@app.before_request
def before_request():
    """
    Before each request, look for the 'login_as' parameter in the request
    URL and set the user as a global on flask.g.user.
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id and user_id.isdigit() else None

@babel.localeselector
def get_locale() -> str:
    """
    Determines the best-matching language based on the following priority:
    1. Locale from URL parameters (if present and supported).
    2. Locale from user settings (if available and supported).
    3. Locale from request header (fallback if user setting is not available
    or not supported).
    4. Default locale.

    Returns:
        str: The selected language code (e.g., "en" or "fr").
    """
    # Check if locale is set in URL parameters and is supported
    locale_param = request.args.get('locale')
    if locale_param and locale_param in app.config['LANGUAGES']:
        return locale_param

    # Check if user is logged in and the user's locale is supported
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Fallback to request header if the user's locale is not supported
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Renders the index.html template with the appropriate welcome message.

    Returns:
        str: The rendered template.
    """
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run()

