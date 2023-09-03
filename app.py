from flask import Flask, render_template, request, redirect, url_for,session
from model import User
from sqlalchemy import select

app = Flask(__name__)

app.secret_key = 'mysecretkey'  



@app.route('/', methods=['GET', 'POST'])
def dashboard():
    if 'user' in session:
        return redirect(url_for('login'))     
    return render_template('dashboard.html', username = session['usuario'] or "")

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
    session['usuario'] = None
    return render_template('login.html')

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if 'user' in session:
        return redirect(url_for('login'))     
    return render_template('cart.html')


if __name__ == '__main__':
    app.run(debug=True)
