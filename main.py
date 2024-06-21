from flask import Flask, send_from_directory

from logs import logger
from db import addPlace
import api.loader

app = Flask(__name__)
api.loader.load(app)

@app.route("/<path:path>")
def public_file(path):
    return send_from_directory("public", path)

@app.route("/")
def index():
    return public_file("index.html")

app.run(port=8080)