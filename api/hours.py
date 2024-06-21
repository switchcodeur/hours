from flask import Blueprint, jsonify, request, Response
from logging import getLogger

from db import addHours, getHours
from utils.authorization import getUser

logger = getLogger()
blueprint = Blueprint("hours", __name__, url_prefix="/api/hours")

@blueprint.route("/<string:username>", methods=["POST"])
def _addHours(username: str):
    user = getUser()
    if user.name != username and not user.valid:
        return Response(status=401)
    
    json = request.get_json()
    addHours(username, json["place"], json["day"], json["start"], json["end"], json["fees"], json["break"])
    return Response(status=200)

@blueprint.route("/<string:username>", methods=["GET"])
def _getHours(username: str):
    user = getUser()
    if not user.valid or not any([user.name == username, user.administrator]):
        return Response(status=401)

    return jsonify(getHours(username))