from sqlalchemy.orm import (
    DeclarativeBase, 
    Mapped, 
    sessionmaker
)
from sqlalchemy import (
    Column, 
    String, 
    ForeignKey,
    Boolean,
    Float,
    Integer,
    create_engine
)
from os.path import dirname


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    name: Mapped[str] = Column(String(), primary_key=True)
    password: Mapped[str] = Column(String())
    administrator: Mapped[bool] = Column(Boolean)

    def __repr__(self) -> str:
        return f"User(name={self.name!r}, password={self.password!r}, administrator={self.administrator!r})"


class Place(Base):
    __tablename__ = "place"

    name: Mapped[str] = Column(String(), primary_key=True)

    def __repr__(self) -> str:
        return f"Place(name={self.name!r})"


class Hours(Base):
    __tablename__ = "hours"

    id: Mapped[int] = Column(Integer(), primary_key=True)

    username: Mapped[str] = Column(ForeignKey("user.name"))
    place: Mapped[str] = Column(ForeignKey("place.name"))

    day: Mapped[str] = Column(String())
    start: Mapped[str] = Column(String())
    end: Mapped[str] = Column(String())
    fees: Mapped[float] = Column(Float())
    _break: Mapped[str] = Column(String())

    def __repr__(self) -> str:
        return f"Place(start={self.start!r}, end={self.end!r}, fees={self.fees!r}, _break={self._break!r})"
    

engine = create_engine(f"sqlite:///{dirname(__file__)}/database.sqlite3")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
