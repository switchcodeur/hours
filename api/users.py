from flask import Blueprint, jsonify, Response, request
from logging import getLogger

from db import getUsernames, isAdministrator, User, delUser
from utils.authorization import getUser
from utils.password import generate

logger = getLogger()
blueprint = Blueprint("users", __name__, url_prefix="/api/users")

@blueprint.route("/", methods=["GET"])
def _getUsernames():
    return jsonify(getUsernames())

@blueprint.route("/auth", methods=["POST"])
def isValid():
    user = getUser(not request.get_json().get("encrypted"))
    return jsonify({"valid": user.valid, "password": user.password})

@blueprint.route("/<string:username>", methods=["GET"])
def getInformations(username: str):
    return jsonify({"administrator": isAdministrator(username)})

@blueprint.route("/<string:username>", methods=["PUT"])
def addUser(username):
    user = getUser()
    if not user.valid and not user.administrator:
        return Response(status=401)

    password = generate(12)

    json = request.get_json()
    if json and json.get("password"):
        password = json.get("password")

    new = User(username, password)
    new.save()

    return jsonify({"password": password})

@blueprint.route("/<string:username>", methods=["DELETE"])
def rmUser(username: str):
    user = getUser()
    if not user.valid and not user.administrator:
        return Response(status=401)
    
    delUser(username)
    return Response(status=200)