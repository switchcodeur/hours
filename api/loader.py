from os.path import dirname, realpath
from typing import List
from flask import Flask
from importlib import import_module

from utils.tree import tree
import __main__


root = dirname(realpath(__main__.__file__))


def find() -> List[str]:
    files = tree(dirname(__file__))
    paths = []

    for file in files:
        if not any([
            not file.endswith(".py"),
            file == __file__.replace("\\", "/")
        ]):
            paths.append(file[len(root) + 1:][:-3].replace("/", "."))

    return paths


def load(app: Flask) -> None:
    paths = find()
    
    for path in paths:
        module = import_module(path, path)
        app.register_blueprint(blueprint=module.blueprint)
        