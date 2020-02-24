from flask import abort, Blueprint, jsonify, request
from typing import Dict, List, Union
from auth import requires_auth
from models.actors import ActorModel
from models.movies import MovieModel

movies = Blueprint("movies", __name__)
MovieJSON = Dict[str, Union[int, str, List[str]]]
ResourceJSON = Dict[str, Union[bool, str, MovieJSON, List[MovieJSON]]]
PayloadJSON = Dict[str, Union[str, List[str]]]


# noinspection PyUnusedLocal
@movies.route("/movies")
@requires_auth("get:movies")
def get_movies(payload: PayloadJSON) -> ResourceJSON:
    """Return a list of movies"""
    _movies = MovieModel.find_all()

    if len(_movies) == 0:
        abort(404)

    return jsonify(
        {"success": True, "movies": [movie.json() for movie in _movies],}
    )


# noinspection PyUnusedLocal
@movies.route("/movies/<int:movie_id>")
@requires_auth("get:movie")
def get_movie(payload: PayloadJSON, movie_id: int) -> ResourceJSON:
    """Return a movie by movie_id"""
    movie = MovieModel.find_by_id(movie_id)

    if movie is None:
        abort(404)

    return jsonify({"success": True, "movie": movie.json()},)


# noinspection PyUnusedLocal
@movies.route("/movies", methods=["POST"])
@requires_auth("post:movie")
def post_movie(payload: PayloadJSON) -> ResourceJSON:
    """Create a new movie"""
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
@movies.route("/movies/<int:movie_id>", methods=["PATCH"])
@requires_auth("patch:movie")
def patch_movie(payload: PayloadJSON, movie_id: int) -> ResourceJSON:
    """Update a movie by movie_id"""
    movie = MovieModel.find_by_id(movie_id)

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

    _id = result["id"]

    return jsonify(
        {"success": True, "movie": MovieModel.find_by_id(_id).json()}
    )


# noinspection PyUnusedLocal
@movies.route("/movies/<int:movie_id>/actor/<int:actor_id>", methods=["PATCH"])
@requires_auth("patch:movie")
def add_actor_to_movie(
    payload: PayloadJSON, movie_id: int, actor_id: int
) -> ResourceJSON:
    """Add an actor by actor_id to a movie by movie_id"""
    movie = MovieModel.find_by_id(movie_id)
    actor = ActorModel.find_by_id(actor_id)

    if movie is None or actor is None:
        abort(404)

    movie.actors.append(actor)
    result = movie.save_to_db()

    if result["error"]:
        abort(500)

    _id = result["id"]

    return jsonify(
        {"success": True, "movie": MovieModel.find_by_id(_id).json()}
    )


# noinspection PyUnusedLocal
@movies.route("/movies/<int:movie_id>", methods=["DELETE"])
@requires_auth("delete:movie")
def delete_movie(payload: PayloadJSON, movie_id: int) -> ResourceJSON:
    """Delete a movie by movie_id"""
    movie = MovieModel.find_by_id(movie_id)

    if movie is None:
        abort(404)

    result = movie.delete_from_db()

    if result["error"]:
        abort(500)

    return jsonify({"success": True, "deleted": movie_id},)
