from flask import Blueprint, jsonify, Response

from utils.auth import get_authorization

blueprint = Blueprint("auth", __name__, url_prefix="/api/auth")


@blueprint.route("/", methods=["POST"])
def post():
    auth = get_authorization()
    if not auth.valid:
        return Response(status=401)
    
    return Response(status=200)
