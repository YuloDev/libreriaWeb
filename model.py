import select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String , DateTime
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///.sqlite',echo=True)
Base = declarative_base()
session = Session(engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(),autoincrement=True,primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))

    def getAll():
        return session.query(User).all()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(),autoincrement=True,primary_key=True)
    name = Column(String(50))
    category = Column(String(50))
    amount = Column(Integer())
    description = Column(String(50))

    def getAll():
        return session.query(Book).all()


Base.metadata.create_all(engine)




session.add([Book(name="EL diario de ana frank")])

