from flask import request
from dataclasses import dataclass
from typing import Union, Tuple

from db.database import User, Session


@dataclass
class Authorization:
    user: Union[User, None]
    valid: bool


def get_authenticators() -> Tuple[str, bytes]:
    authorization = request.headers.get("Authorization")

    if not authorization or not " " in authorization:
        return 0, b""
    
    username, password = authorization.split(" ")

    return username, password


def get_authorization() -> Authorization:
    username, password = get_authenticators()

    if not username or not password:
        return Authorization(user=None, valid=False)

    session = Session()
    user = session.query(User).where(User.name == username).first()
    session.close()

    if not user:
        return Authorization(user=None, valid=False)
    
    return Authorization(user=user, valid=user.password == password)
