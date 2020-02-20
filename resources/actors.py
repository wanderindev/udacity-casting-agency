from flask import abort, Blueprint, jsonify, request
from auth import requires_auth
from models.actors import ActorModel

actors = Blueprint("actors", __name__)


@actors.route("/")
@requires_auth("get:actors")
def get_actors():
    _actors = ActorModel.find_all()

    if len(_actors) == 0:
        abort(404)

    return jsonify(
        {"success": True, "actors": [actor.json() for actor in _actors],}, 200
    )


@actors.route("/<str:actor_name>")
@requires_auth("get:actor")
def get_actor(actor_name):
    actor = ActorModel.find_by_name(actor_name)

    if actor is None:
        abort(404)

    return jsonify({"success": True, "actor": actor.json()}, 200)


@actors.route("/", methods=["POST"])
@requires_auth("post:actor")
def post_actor():
    data = request.get_json()
    actor = ActorModel(**data)
    result = actor.save_to_db()

    if result["error"]:
        abort(500)

    _id = result["id"]

    return jsonify(
        {"success": True, "actor": ActorModel.find_by_id(_id).json()}
    )


@actors.route("/<str:actor_name>", methods=["PATCH"])
@requires_auth("patch:actor")
def patch_actor(actor_name):
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


@actors.route("/<str:actor_name>", methods=["DELETE"])
@requires_auth("delete:movie")
def delete_actors(actor_name):
    actor = ActorModel.find_by_name(actor_name)

    if actor is None:
        abort(404)

    result = actor.delete_from_db()

    if result["error"]:
        abort(500)

    return jsonify({"success": True, "deleted": actor_name}, 200)
