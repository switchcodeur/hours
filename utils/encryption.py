from hashlib import sha1


def encrypt(text: str) -> str:
    return sha1(str.encode(text)).hexdigest()
