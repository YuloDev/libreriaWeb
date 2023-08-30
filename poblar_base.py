import sqlite3
from faker import Faker

# Conectarse a la base de datos (se creará si no existe)
conn = sqlite3.connect('.sqlite')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        category TEXT
    )
''')
conn.commit()

# Configura el proveedor en español
fake = Faker('es_ES')


# Generar 10 libros ficticios con categorías en español utilizando Faker
categories = ["Ficción", "No Ficción",
              "Misterio", "Romance", "Ciencia Ficción"]
books_data = [(fake.sentence(), fake.paragraph(),
               fake.random_element(categories)) for _ in range(10)]

# Insertar datos de libros en la base de datos
for book in books_data:
    cursor.execute(
        'INSERT INTO books (title, description, category) VALUES (?, ?, ?)', book)
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()

print("Base de datos poblada exitosamente.")
