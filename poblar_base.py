from requests import Session
from sqlalchemy import create_engine
from model import Book
from faker import Faker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///.sqlite',echo=True)
Base = declarative_base()
session = Session(engine)
# Configura el proveedor en español
fake = Faker('es_ES')


# Generar 10 libros ficticios con categorías en español utilizando Faker
categories = ["Ficción", "No Ficción",
              "Misterio", "Romance", "Ciencia Ficción"]
books_data = [(fake.sentence(), fake.paragraph(),
               fake.random_element(categories)) for _ in range(10)]



print("Base de datos poblada exitosamente.")
