#!/usr/bin/env python3
"""
Creating a user login system is outside the scope of this project.
To emulate a similar behavior, I copied the
following user table in this file.

I defined the get_user function that returns a user dictionary or None
if the ID cannot be found or if login_as was not passed.

I defined a before_request function and used the app.before_request
decorator to make it be executed before all other functions. before_request
uses get_user to find a user if any, and sets it as a global on flask.g.user.
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

@app.route('/')
def index() -> str:
    """
    Renders the index.html template with the appropriate welcome message.

    Returns:
        str: The rendered template.
    """
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run()

