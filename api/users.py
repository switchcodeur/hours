from flask import Blueprint, jsonify, Response, request
from secrets import choice as rchoice

from db.database import User, Session
from utils.auth import get_authorization
from utils.encryption import encrypt


blueprint = Blueprint("users", __name__, url_prefix="/api/users")


@blueprint.route("/", methods=["GET"])
def get():
    session = Session()
    users = {}

    for user in session.query(User).all():
       users[user.name] = {"administrator": user.administrator}

    session.close()
    return jsonify(users)


@blueprint.route("/<string:username>", methods=["PUT"])
def put(username: str):
    auth = get_authorization()
    if not auth.valid and not auth.user.name == username:
        if not auth.user.administrator:
            return Response(status=401)

    characters = [chr(i) for i in range(33, 127)]
    password = "".join([rchoice(characters) for i in range(12)])
    encrypted_password = None

    session = Session()
    administrator = session.query(User.administrator).where(User.name == username).scalar()
    session.query(User).where(User.name == username).delete()

    json = request.get_json()
    if json:
        encrypted_password = json.get("password")
        

    user = User(
        name=username,
        password=encrypted_password or encrypt(password),
        administrator=administrator or False
    )
    session.add(user)
    session.commit()
    session.close()

    return jsonify({"password": password})


@blueprint.route("/<string:username>", methods=["DELETE"])
def delete(username: str):
    auth = get_authorization()
    if not auth.valid or not auth.user.administrator:
        return Response(status=401)
    
    session = Session()
    session.query(User).where(User.name == username).delete()
    session.commit()
    session.close()

    return Response(status=200)
