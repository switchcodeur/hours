from .connection import get as getDB


def getPlaces() -> list:
    _, cur = getDB()
    res = cur.execute("SELECT place FROM Places")
    res = res.fetchall()

    places = []
    for place in res:
        places.append(place[0])

    return places


def exists(place: str) -> bool:
    return place in getPlaces()


def addPlace(place: str) -> None:
    if exists(place):
        return
    
    con, cur = getDB()
    cur.execute(f'INSERT INTO Places (place) VALUES ("{place}")')
    con.commit()


def rmPlace(place: str) -> None:
    if not exists(place):
        return
    
    con, cur = getDB()
    cur.execute(f'DELETE FROM Places WHERE place="{place}"')
    con.commit()
