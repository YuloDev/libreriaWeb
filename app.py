from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuración de la base de datos


def get_db_connection():
    conn = sqlite3.connect('.sqlite')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM BOOKS').fetchall()
    conn.commit()
    conn.close()

    return render_template('dashboard.html', books=books)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     title = request.form['title']
    #     user = request.form['user']

    #     if not title or not user:
    #         return "Por favor, completa todos los campos."

    #     conn = get_db_connection()
    #     conn.execute('INSERT INTO loans (title, user) VALUES (?, ?)', (title, user))
    #     conn.commit()
    #     conn.close()

    #     return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM BOOKS').fetchall()
    conn.commit()
    conn.close()

    return render_template('cart.html',books=books)


if __name__ == '__main__':
    app.run(debug=True)
