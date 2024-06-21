from sqlite3 import connect, Connection, Cursor
from typing import Tuple
from os.path import dirname, isfile


def get() -> Tuple[Connection, Cursor]:
    con = connect(f"{dirname(__file__)}/database.db")
    return con, con.cursor()


def reset(con: Connection, cur: Cursor) -> None:
    con, cur = get()

    if not isfile(f"{dirname(__file__)}/schema.sql"):
        return con, cur
    
    with open(f"{dirname(__file__)}/schema.sql") as schema:
        sql = schema.read()
        cur.executescript(sql)
    
    con.commit()


if not isfile(f"{dirname(__file__)}/database.db"):
    reset(*get())