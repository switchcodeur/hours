from os import listdir, PathLike
from os.path import isdir, normpath


def tree(directory: PathLike) -> list:
    files = []

    for file in listdir(directory):
        path = f"{directory}/{file}"

        if path.endswith("__pycache__"): pass

        elif isdir(path):
            files += tree(path)

        else:
            files.append(path.replace("\\", "/"))

    return files
