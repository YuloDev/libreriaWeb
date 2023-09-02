from flask import Flask, render_template, request, redirect, url_for,session
from model import User


app = Flask(__name__)

app.secret_key = 'mysecretkey'  



@app.route('/', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        if session['usuario'] is None:
            return redirect(url_for('login'))
        else:
            return render_template('dashboard.html',username = session['usuario'] or "")
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        all_users = session.query(User).all()
        username = request.form['username']
        password = request.form['password']
        for user in all_users:
            if username == user.username and password == user.password:
                session['usuario'] = username
                return redirect(url_for('dashboard')) 

    return render_template('login.html',message = message)

@app.route('/logout', methods=['GET', 'POST'])
def logout():

    if request.method == 'POST':
        
        user = request.form['username']
        password = request.form['password']
        if user == 'admin' and password == 'admin':
            session['usuario'] = user
            return redirect(url_for('dashboard')) 


    return render_template('login.html')

@app.route('/cart', methods=['GET', 'POST'])
def cart():

    return render_template('cart.html')


if __name__ == '__main__':
    app.run(debug=True)
