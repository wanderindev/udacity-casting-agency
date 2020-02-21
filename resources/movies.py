from flask import abort, Blueprint, jsonify, request
from typing import Dict, List, Union
from auth import requires_auth
from models.movies import MovieModel

movies = Blueprint("movies", __name__)
MovieJSON = Dict[str, Union[int, str, List[str]]]
ResourceJSON = Dict[str, Union[bool, str, MovieJSON, List[MovieJSON]]]
PayloadJSON = Dict[str, Union[str, List[str]]]


# noinspection PyUnusedLocal
@movies.route("/movies")
@requires_auth("get:movies")
def get_movies(payload: PayloadJSON) -> ResourceJSON:
    _movies = MovieModel.find_all()

    if len(_movies) == 0:
        abort(404)

    return jsonify(
        {"success": True, "movies": [movie.json() for movie in _movies],}, 200
    )


# noinspection PyUnusedLocal
@movies.route("/movies/<string:movie_title>")
@requires_auth("get:movie")
def get_movie(payload: PayloadJSON, movie_title: str) -> ResourceJSON:
    movie = MovieModel.find_by_title(movie_title)

    if movie is None:
        abort(404)

    return jsonify({"success": True, "movie": movie.json()}, 200)


# noinspection PyUnusedLocal
@movies.route("/movies", methods=["POST"])
@requires_auth("post:movie")
def post_movie(payload: PayloadJSON) -> ResourceJSON:
    data = request.get_json()
    movie = MovieModel(**data)
    result = movie.save_to_db()

    if result["error"]:
        abort(500)

    _id = result["id"]

    return jsonify(
        {"success": True, "movie": MovieModel.find_by_id(_id).json()}
    )


# noinspection PyUnusedLocal
@movies.route("/movies/<string:movie_title>", methods=["PATCH"])
@requires_auth("patch:movie")
def patch_movie(payload: PayloadJSON, movie_title: str) -> ResourceJSON:
    movie = MovieModel.find_by_title(movie_title)

    if movie is None:
        abort(404)

    data = request.get_json()
    title = data.get("title", None)
    release_date = data.get("release_date", None)

    if title is None or release_date is None:
        abort(400)

    movie.title = title
    movie.release_date = release_date
    result = movie.save_to_db()

    if result["error"]:
        abort(500)

    result = movie.save_to_db()

    if result["error"]:
        abort(500)

    _id = result["id"]

    return jsonify(
        {"success": True, "movie": MovieModel.find_by_id(_id).json()}
    )


# noinspection PyUnusedLocal
@movies.route("/movies/<string:movie_title>", methods=["DELETE"])
@requires_auth("delete:movie")
def delete_movie(payload: PayloadJSON, movie_title: str) -> ResourceJSON:
    movie = MovieModel.find_by_title(movie_title)

    if movie is None:
        abort(404)

    result = movie.delete_from_db()

    if result["error"]:
        abort(500)

    return jsonify({"success": True, "deleted": movie_title}, 200)
