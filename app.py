from flask import Flask, jsonify
from flask_cors import CORS
from auth import AuthError
from config import config
from db import db
from resources.actors import actors
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
    app.register_blueprint(movies)

    # noinspection PyUnusedLocal
    @app.errorhandler(400)
    def bad_request(error):
        return (
            jsonify(
                {"success": False, "error": 400, "message": "Bad request"}),
            400,
        )

    # noinspection PyUnusedLocal
    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "Not found."}),
            404,
        )

    # noinspection PyUnusedLocal
    @app.errorhandler(422)
    def unprocessable(error):  # pragma: no cover
        return (
            jsonify(
                {"success": False, "error": 422, "message": "Unprocessable"}),
            422,
        )

    # noinspection PyUnusedLocal
    @app.errorhandler(500)
    def internal_error(error):
        return (
            jsonify(
                {
                    "success": False,
                    "error": 500,
                    "message": "Internal server error",
                }
            ),
            500,
        )

    # noinspection PyUnusedLocal
    @app.errorhandler(AuthError)
    def auth_error(error):
        return (
            jsonify(
                {
                    "success": False,
                    "error": error.status_code,
                    "message": error.error,
                }
            ),
            error.status_code,
        )

    return app
