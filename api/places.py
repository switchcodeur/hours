from flask import Blueprint, jsonify, request, Response

from db import getPlaces, addPlace, rmPlace
from utils.authorization import getUser

blueprint = Blueprint("places", __name__, url_prefix="/api/places")

@blueprint.route("/", methods=["GET"])
def _getPlaces():
    user = getUser()
    if not user.valid:
        return jsonify({"message": "401 Unauthorized"})

    return jsonify(getPlaces())

@blueprint.route("/", methods=["POST"])
def _addPlace():
    user = getUser()
    if not user.valid and not user.administrator:
        return Response(status=401)
    
    json = request.get_json()
    if not json.get("name"):
        return Response(status=400)

    addPlace(json.get("name"))
    return Response(status=200)

@blueprint.route("/", methods=["DELETE"])
def _rmPlace():
    user = getUser()
    if not user.valid and not user.administrator:
        return Response(status=401)
    
    json = request.get_json()
    if not json.get("place"):
        return Response(status=400)
    print(json)
    rmPlace(json.get("place"))
    return Response(status=200)