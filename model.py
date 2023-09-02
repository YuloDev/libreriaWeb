from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String , DateTime
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///.sqlite',echo=True)
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(),autoincrement=True,primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
Base.metadata.create_all(engine)


with Session(engine) as session:
    spongebob = User(username="spongebob",email="Spongebob Squarepants",password="1234")
    session.add_all([spongebob])
    session.commit()
    

