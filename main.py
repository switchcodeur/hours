from flask import Flask, send_from_directory
from configparser import RawConfigParser

from api.loader import load as load_api
from db.database import Session, User
from utils.encryption import encrypt
import utils.logging


def add_administrators():
    parser = RawConfigParser()
    parser.read("server.conf")
    
    session = Session()

    for username in parser["ADMINISTRATORS"]["usernames"].split(" "):
        user = User(
            name=username,
            password=encrypt(parser["ADMINISTRATORS"]["password"].replace(" ", "")),
            administrator=True
        )
        
        if not session.query(User.name).where(User.name == username).all():
            session.add(user)
    
    session.commit()


app = Flask(__name__)

load_api(app)


@app.route("/<path:path>")
def public_file(path):
    return send_from_directory("public", path)


@app.route("/")
def index():
    return public_file("login.html")


if __name__ == "__main__":
    add_administrators()
    
    app.run(host="0.0.0.0", port=8080)
