from flask import Blueprint, jsonify, request, Response
from logging import getLogger

from db.database import Session, Hours
from utils.auth import get_authorization

logger = getLogger()
blueprint = Blueprint("hours", __name__, url_prefix="/api/hours")

@blueprint.route("/", methods=["POST"])
def post():
    auth = get_authorization()
    if not auth.valid:
        return Response(status=401)
    
    json = request.get_json()
    
    session = Session()
    hours = Hours(
        username=auth.user.name,
        place=json["place"],
        day=json["day"],
        start=json["start"],
        end=json["end"],
        fees=json["fees"],
        _break=json["break"]
    )
    session.add(hours)
    session.commit()
    
    return Response(status=200)

@blueprint.route("/<string:username>", methods=["GET"])
def get(username: str):
    auth = get_authorization()
    if not auth.valid or not auth.user.administrator:
        return Response(status=401)

    session = Session()
    hours = [
        {
            "start": _hours.start,
            "end": _hours.end,
            "break": _hours._break,
            "fees": _hours.fees
        } for _hours in session.query(Hours).where(Hours.username == username).all()
    ]
    session.close()

    return jsonify(hours)
