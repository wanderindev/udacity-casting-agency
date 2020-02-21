from flask import Blueprint, jsonify
from auth import AuthError

errors = Blueprint("errors", __name__)


@errors.errorhandler(400)
def bad_request():
    return (
        jsonify({"success": False, "error": 400, "message": "Bad request"}),
        400,
    )


@errors.errorhandler(404)
def not_found():
    return (
        jsonify({"success": False, "error": 404, "message": "Not found"}),
        404,
    )


@errors.errorhandler(422)
def unprocessable():  # pragma: no cover
    return (
        jsonify({"success": False, "error": 422, "message": "Unprocessable"}),
        422,
    )


@errors.errorhandler(500)
def internal_error():
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


@errors.errorhandler(AuthError)
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
