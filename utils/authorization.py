from db import User, isAdministrator
from flask import request
from logging import getLogger

logger=getLogger()

def getUser(encrypt: bool = False) -> User:
    username, password = request.headers.get("Authorization").split(" ")
    return User(username, password, isAdministrator(username), encrypt)