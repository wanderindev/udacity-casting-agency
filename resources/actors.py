from flask import abort, Blueprint, jsonify, request
from typing import Dict, List, Union
from auth import requires_auth
from models.actors import ActorModel

actors = Blueprint("actors", __name__)
ActorJSON = Dict[str, Union[int, str, List[str]]]
ResourceJSON = Dict[str, Union[bool, str, ActorJSON, List[ActorJSON]]]
PayloadJSON = Dict[str, Union[str, List[str]]]


# noinspection PyUnusedLocal
@actors.route("/")
@requires_auth("get:actors")
def get_actors(payload: PayloadJSON) -> ResourceJSON:
    _actors = ActorModel.find_all()

    if len(_actors) == 0:
        abort(404)

    return jsonify(
        {"success": True, "actors": [actor.json() for actor in _actors],}, 200
    )


# noinspection PyUnusedLocal
@actors.route("/actors/<string:actor_name>")
@requires_auth("get:actor")
def get_actor(payload: PayloadJSON, actor_name: str) -> ResourceJSON:
    actor = ActorModel.find_by_name(actor_name)

    if actor is None:
        abort(404)

    return jsonify({"success": True, "actor": actor.json()}, 200)


# noinspection PyUnusedLocal
@actors.route("/actors", methods=["POST"])
@requires_auth("post:actor")
def post_actor(payload: PayloadJSON) -> ResourceJSON:
    data = request.get_json()
    actor = ActorModel(**data)
    result = actor.save_to_db()

    if result["error"]:
        abort(500)

    _id = result["id"]

    return jsonify(
        {"success": True, "actor": ActorModel.find_by_id(_id).json()}
    )


# noinspection PyUnusedLocal
@actors.route("/actors/<string:actor_name>", methods=["PATCH"])
@requires_auth("patch:actor")
def patch_actor(payload: PayloadJSON, actor_name: str) -> ResourceJSON:
    actor = ActorModel.find_by_name(actor_name)

    if actor is None:
        abort(404)

    data = request.get_json()
    name = data.get("name", None)
    date_of_birth = data.get("date_of_birth", None)
    gender = data.get("gender", None)

    if name is None or date_of_birth is None or gender is None:
        abort(400)

    actor.name = name
    actor.date_of_birth = date_of_birth
    actor.gender = gender
    result = actor.save_to_db()

    if result["error"]:
        abort(500)

    result = actor.save_to_db()

    if result["error"]:
        abort(500)

    _id = result["id"]

    return jsonify(
        {"success": True, "actor": ActorModel.find_by_id(_id).json()}
    )


# noinspection PyUnusedLocal
@actors.route("/actors/<string:actor_name>", methods=["DELETE"])
@requires_auth("delete:movie")
def delete_actors(payload: PayloadJSON, actor_name: str) -> ResourceJSON:
    actor = ActorModel.find_by_name(actor_name)

    if actor is None:
        abort(404)

    result = actor.delete_from_db()

    if result["error"]:
        abort(500)

    return jsonify({"success": True, "deleted": actor_name}, 200)
