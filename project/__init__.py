"""
Welcome to the documentation for the Flask  API!

## Introduction

The Flask  API is an API (Application Programming Interface)

## Key Functionality

The Flask Journal API has the following functionality:

1. Work with journal entries:
  * ...................
2. <More to come!>

## Key Modules

This project is written using Python 3.11

The project utilizes the following modules:

* **Flask**: micro-framework for web application development which includes the following dependencies:
  * **click**: package for creating command-line interfaces (CLI)
  * **itsdangerous**: cryptographically sign data
  * **Jinja2**: templating engine
  * **MarkupSafe**: escapes characters so text is safe to use in HTML and XML
  * **Werkzeug**: set of utilities for creating a Python application that can talk to a WSGI server
* **APIFairy**: API framework for Flask which includes the following dependencies:
  * **Flask-Marshmallow** - Flask extension for using Marshmallow (object serialization/deserialization library)
  * **Flask-HTTPAuth** - Flask extension for HTTP authentication
  * **apispec** - API specification generator that supports the OpenAPI specification
* **pytest**: framework for testing Python projects
"""

import logging

from flask import Flask, redirect, request, url_for
from apifairy import APIFairy
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import Config


apifairy = APIFairy()
ma = Marshmallow()
db = SQLAlchemy()
cors = CORS()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


# ----------------
# Helper Functions
# ----------------


def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    apifairy.init_app(app)
    ma.init_app(app)


def register_blueprints(app):
    # Import the blueprints
    from .api import journal
    from .errors import errors

    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    app.register_blueprint(errors)
    app.register_blueprint(journal, url_prefix="/journal")


# ----------------------------
# Application Factory Function
# ----------------------------


def create_app(config_class=Config):
    # from app import models

    # Create the Flask application
    app = Flask(__name__)

    # Configure the API
    app.config.from_object(config_class)

    initialize_extensions(app)
    register_blueprints(app)
    if app.config["USE_CORS"]:  # pragma: no branch
        cors.init_app(app)

    # @app.shell_context_processor
    # def shell_context():  # pragma: no cover
    #     ctx = {"db": db}
    #     for attr in dir(models):
    #         model = getattr(models, attr)
    #         if hasattr(model, "__bases__") and db.Model in getattr(model, "__bases__"):
    #             ctx[attr] = model
    #     return ctx

    @app.route("/")
    def index():  # pragma: no cover
        return redirect(url_for("apifairy.docs"))

    @app.after_request
    def after_request(response):
        # Werkzeu sometimes does not flush the request body so we do it here
        request.get_data()
        return response

    return app
