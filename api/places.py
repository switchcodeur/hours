from flask import Blueprint, jsonify, request, Response

from db.database import Session, Place
from utils.auth import get_authorization


blueprint = Blueprint("places", __name__, url_prefix="/api/places")


@blueprint.route("/", methods=["GET"])
def get():
    auth = get_authorization()
    if not auth.valid:
        return Response(status=401)

    session = Session()
    res = session.query(Place.name).all()
    session.close()

    places = []
    for place in res:
        places.append(place[0])

    return jsonify(places)


@blueprint.route("/<string:name>", methods=["PUT"])
def put(name):
    auth = get_authorization()
    if not auth.valid or not auth.user.administrator:
        return Response(status=401)

    session = Session()

    if not session.query(Place.name).where(Place.name == name).all():
        place = Place(name=name)
        
        session.add(place)
        session.commit()

    session.close()

    return Response(status=200)


@blueprint.route("/<string:place>", methods=["DELETE"])
def delete(place: str):
    auth = get_authorization()
    if not auth.valid or not auth.user.administrator:
        return Response(status=401)
    
    session = Session()
    session.query(Place).where(Place.name == place).delete()
    session.commit()
    session.close()

    return Response(status=200)
