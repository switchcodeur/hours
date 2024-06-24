from hashlib import sha1


def encrypt(string: str) -> str:
    hash = sha1()
    hash.update(string.encode())

    return hash.hexdigest()
