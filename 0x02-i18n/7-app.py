#!/usr/bin/env python3
"""
In this task, I defined the get_timezone function and used the
babel.timezoneselector decorator.

The logic is the same as get_locale:
    - Find the timezone parameter in URL parameters (if present and valid).
    - Find the time zone from user settings (if available and valid).
    - Default to UTC.

Before returning a URL-provided or user time zone, I validated that it is a
valid time zone using pytz.timezone and caught
the pytz.exceptions.UnknownTimeZoneError exception.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz

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
    Before each request, look for the 'login_as' parameter in the request URL
    and set the user as a global on flask.g.user.
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
    # ... (same as before)

@babel.timezoneselector
def get_timezone() -> str:
    """
    Determines the best-matching time zone based on the following priority:
    1. Time zone from URL parameters (if present and valid).
    2. Time zone from user settings (if available and valid).
    3. Default to UTC.

    Returns:
        str: The selected time zone name (e.g., "Europe/Paris" or "UTC").
    """
    # Check if timezone is set in URL parameters and is valid
    timezone_param = request.args.get('timezone')
    if timezone_param:
        try:
            pytz.timezone(timezone_param)
            return timezone_param
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Check if user is logged in and the user's timezone is valid
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Fallback to UTC if timezone is not set or not valid
    return 'UTC'

@app.route('/')
def index() -> str:
    """
    Renders the index.html template with the appropriate welcome message.

    Returns:
        str: The rendered template.
    """
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run()

