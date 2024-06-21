from typing import List

from utils.encryption import encrypt
from .connection import get as getDB


def getUsernames() -> List[str]:
    _, cur = getDB()
    res = cur.execute("SELECT name FROM Users")
    res = res.fetchall()

    usernames = []
    for username in res:
        usernames.append(username[0])
    
    return usernames


def userExists(username: str) -> bool:    
    return username in getUsernames()


def isAdministrator(username: str) -> bool:
    if not userExists(username):
        return False
    
    _, cur = getDB()
    res = cur.execute(f'SELECT administrator FROM Users WHERE name = "{username}"')
    res = res.fetchone()

    return bool(res[0]) or False


def delUser(username: str) -> None:
    con, cur = getDB()
    cur.execute(f'DELETE FROM Users WHERE name = "{username}"')
    cur.execute(f'DELETE FROM Hours WHERE username = "{username}"')
    con.commit()


class User:
    def __init__(
        self,
        name: str,
        password: str,
        administrator: bool = False,
        _encrypt: bool = True           
    ) -> None:
        self.con, self.cur = getDB()

        self.name = name
        self.administrator = administrator

        if _encrypt: self.password = encrypt(password) 
        else: self.password = password

        self.valid = self.isValid()

    def isValid(self) -> bool:
        if not userExists(self.name):
            return False

        res = self.cur.execute(f'SELECT password FROM Users WHERE name = "{self.name}"')
        res = res.fetchone()

        return res[0] == self.password
    
    def save(self) -> None:
        if userExists(self.name):
            self.administrator = isAdministrator(self.name)
            self.cur.execute(f'DELETE FROM Users WHERE name = "{self.name}"')

        self.cur.execute(f'INSERT INTO Users (name, password, administrator) VALUES ("{self.name}", "{self.password}", {int(self.administrator)})')
        self.con.commit()
