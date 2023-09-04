import select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String,Float
from sqlalchemy.orm import Session
import random
engine = create_engine('sqlite:///.sqlite',echo=True)
Base = declarative_base()
session = Session(engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(),autoincrement=True,primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    
    def add(self):
        session.add(self)
        session.commit()

    def getAll():
        return session.query(User).all()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(),autoincrement=True,primary_key=True)
    name = Column(String(50))
    category = Column(String(50))
    amount = Column(Integer(),default=0)
    description = Column(String(50),default="")

    def getAll():
        return session.query(Book).all()

class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer(),autoincrement=True,primary_key=True)
    user = Column(String(50))
    end_date = Column(String(50),default="")
    
    def add(self):
        session.add(self)
        session.commit()    

    def getAll():
        return session.query(Book).all()
    
class ReservationItem(Base):
    __tablename__ = 'invoice_items'
    id = Column(Integer(),autoincrement=True,primary_key=True)
    quantity = Column(Integer)
    subtotal = Column(Float)
    

Base.metadata.create_all(engine)
