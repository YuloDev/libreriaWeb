from flask import Flask, render_template, request, redirect, url_for,session
import sqlite3


app = Flask(__name__)

app.secret_key = 'mysecretkey'  

# Configuración de la base de datos

def esta_autenticado():
    return 'usuario' in session

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
    if request.method == 'GET':
        if not esta_autenticado():
            return redirect(url_for('login'))
        else:
            return render_template('dashboard.html',books=books)
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        user = request.form['username']
        password = request.form['password']
        if user == 'admin' and password == 'admin':
            session['usuario'] = user
            return redirect(url_for('dashboard')) 


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
