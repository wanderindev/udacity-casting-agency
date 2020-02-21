from flask import Flask
from flask_cors import CORS

from config import config
from db import db
from resources.actors import actors
from resources.errors import errors
from resources.movies import movies

cors = CORS()


def create_app(config_name: str = "development") -> Flask:
    """
    Factory for the creation of a Flask app.
    :param config_name: the key for the config setting to use
    :type config_name: str
    :return: app: a Flask app instance
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    cors.init_app(app)
    db.init_app(app)

    app.register_blueprint(actors)
    app.register_blueprint(errors)
    app.register_blueprint(movies)

    return app
