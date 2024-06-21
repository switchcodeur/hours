CREATE TABLE IF NOT EXISTS Users (
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    administrator BIT
);

CREATE TABLE IF NOT EXISTS Places (
    place TEXT 
);

CREATE TABLE IF NOT EXISTS Hours (
    username TEXT NOT NULL,
    place TEXT NOT NULL,
    day CHAR(10) NOT NULL,
    start CHAR(5) NOT NULL,
    end CHAR(5) NOT NULL,
    fees TEXT NOT NULL,
    _break CHAR(5) NOT NULL
);