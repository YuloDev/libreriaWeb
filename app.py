import datetime
import json
from flask import Flask, render_template, request, redirect, url_for,session
from model import User,Book
from sqlalchemy import select

app = Flask(__name__)

app.secret_key = 'mysecretkey'  

books = []


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    books = Book.getAll()
    if not 'usuario' in session:
        return redirect(url_for('login'))     
    return render_template('dashboard.html',books=books,username = session['usuario'] or "")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        all_users = User.getAll()
        username = request.form['username']
        password = request.form['password']
        for user in all_users:
            if username == user.username and password == user.password:
                session['usuario'] = username
                return redirect(url_for('dashboard')) 

    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect('login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user = User(username = username, password = password, email = email)
        user.add()
        return redirect(url_for('login')) 

    return render_template('register.html')

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    #Comentario xd
    if 'user' in session:
        return redirect(url_for('login'))
    # Obtiene los datos de los libros de la URL
    libros = request.args.get('libros')
    
    if libros:
        libros = json.loads(libros)
        print(libros)
        # Ahora tienes los datos de los libros en forma de una lista de Python
        fecha_actual = datetime.datetime.now()
        fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
        # Renderiza el template print_reservation.html con los datos necesarios
        return render_template('print_reservation.html', books=libros, client=session["usuario"], date=fecha_formateada)    
    return render_template('cart.html',username = session['usuario'] or "")


    

if __name__ == '__main__':
    app.run(debug=True)
