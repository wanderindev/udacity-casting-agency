from flask import Blueprint, jsonify

movies = Blueprint("movies", __name__)


@movies.route("/")
def get_movies():
    return jsonify(
        {
            "success": True,
            "movies": [
                {
                    "id": 1,
                    "title": "A great movie",
                    "release_date": "2020-02-18",
                }
            ],
        }
    )
