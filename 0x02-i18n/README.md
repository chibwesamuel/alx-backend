# 0x02. i18n
###Flask Internationalization and Localization

In this repository, I demonstrate the implementation of internationalization and localization features in a Flask web application. The project is divided into multiple tasks, each building upon the previous one to achieve a fully internationalized web application.

## Task 0: Basic Flask app

In the first task, I have set up a basic Flask app in `0-app.py`. The app contains a single route `/`, and the `index.html` template displays "Welcome to Holberton" as the page title (`<title>`) and "Hello world" as the header (`<h1>`).

### Repository and Files:

- GitHub repository: [alx-backend](https://github.com/chibwesamuel/alx-backend)
- Directory: `0x02-i18n`
- Files: `0-app.py`, `templates/0-index.html`

## Task 1: Basic Babel setup

In this task, I installed the Babel Flask extension and instantiated the Babel object in the app. The available languages in the app are configured using the `Config` class, which has a `LANGUAGES` class attribute equal to `["en", "fr"]`. Babel's default locale is set to "en", and the timezone is set to "UTC".

### Repository and Files:

- GitHub repository: [alx-backend](https://github.com/chibwesamuel/alx-backend)
- Directory: `0x02-i18n`
- Files: `1-app.py`, `templates/1-index.html`

## Task 2: Get locale from request

In the third task, I created a `get_locale` function using the `babel.localeselector` decorator. The function uses `request.accept_languages` to determine the best match with the supported languages.

### Repository and Files:

- GitHub repository: [alx-backend](https://github.com/chibwesamuel/alx-backend)
- Directory: `0x02-i18n`
- Files: `2-app.py`, `templates/2-index.html`

## Task 3: Parametrize templates

The fourth task involves parametrizing the templates using the `_` or `gettext` function. I also created a `babel.cfg` file to configure the translations. The translations for the message IDs `home_title` and `home_header` have been provided for English and French languages.

### Repository and Files:

- GitHub repository: [alx-backend](https://github.com/chibwesamuel/alx-backend)
- Directory: `0x02-i18n`
- Files: `3-app.py`, `babel.cfg`, `templates/3-index.html`, `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`, `translations/en/LC_MESSAGES/messages.mo`, `translations/fr/LC_MESSAGES/messages.mo`

## Task 4: Force locale with URL parameter

In the fifth task, I implemented a way to force a particular locale by passing the `locale=fr` parameter to the app's URLs. The `get_locale` function detects the incoming request for the `locale` argument and returns it if it is a supported locale; otherwise, it resorts to the default behavior.

### Repository and Files:

- GitHub repository: [alx-backend](https://github.com/chibwesamuel/alx-backend)
- Directory: `0x02-i18n`
- Files: `4-app.py`, `templates/4-index.html`

## Task 5: Mock logging in

The sixth task involves mocking a user login system by using a user table in `5-app.py`. The login is mocked by passing a `login_as` URL parameter containing the user ID to log in as. The `get_user` function returns the user dictionary based on the provided user ID, and the `before_request` function sets the user as a global on `flask.g.user`.

The HTML template displays a welcome message if a user is logged in, otherwise, it displays a default message.

### Repository and Files:

- GitHub repository: [alx-backend](https://github.com/chibwesamuel/alx-backend)
- Directory: `0x02-i18n`
- Files: `5-app.py`, `templates/5-index.html`

## Task 6: Use user locale

In the seventh task, I modified the `get_locale` function to use a user's preferred locale if it is supported. The order of priority for finding the locale is as follows:
1. Locale from URL parameters
2. Locale from user settings
3. Locale from request header
4. Default locale

### Repository and Files:

- GitHub repository: [alx-backend](https://github.com/chibwesamuel/alx-backend)
- Directory: `0x02-i18n`
- Files: `6-app.py`, `templates/6-index.html`

## Task 7: Infer appropriate time zone

The eighth task involves defining a `get_timezone` function and using the `babel.timezoneselector` decorator. The function infers the time zone using the following priority:
1. Timezone parameter from URL
2. Time zone from user settings
3. Default to UTC

Before returning the inferred time zone, the function validates that it is a valid time zone using `pytz.timezone` and catching the `pytz.exceptions.UnknownTimeZoneError` exception.

### Repository and Files:

- GitHub repository: [alx-backend](https://github.com/chibwesamuel/alx-backend)
- Directory: `0x02-i18n`
- Files: `7-app.py`, `templates/7-index.html`

## Task 8: Display the current time

In the final task, I display the current time on the home page in the default format based on the inferred time zone. The translations for displaying the time in English and French are provided.

### Repository and Files:

- GitHub repository: [alx-backend](https://github.com/chibwesamuel/alx-backend)
- Directory: `0x02-i18n`
- Files: `app.py`, `templates/index.html`, `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`

Please feel free to explore the code in each task file to see the implementation details. If you have any questions or suggestions, please let me know! Thanks for checking out my repo! 🚀
