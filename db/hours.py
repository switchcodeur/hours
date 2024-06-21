from datetime import date, time
from typing import List, Dict

from .connection import get as getDB

def addHours(
    username: str,
    place: str,
    day: str,
    start: str,
    end: str,
    fees: str,
    _break: str
) -> None:
    con, cur = getDB()
    cur.execute(f'INSERT INTO Hours (username, place, day, start, end, fees, _break) VALUES ("{username}", "{place}", "{day}", "{start}", "{end}", "{fees}", "{_break}")')
    con.commit()

def getHours(username: str) -> List[Dict]:
    _, cur = getDB()
    res = cur.execute(f'SELECT * FROM Hours WHERE username = "{username}"')
    res = res.fetchall()

    hours = []
    for infos in res:
        hours.append({
            "place": infos[1],
            "day": infos[2],
            "start": infos[3],
            "end": infos[4],
            "fees": infos[5],
            "break": infos[6]
        })

    return hours