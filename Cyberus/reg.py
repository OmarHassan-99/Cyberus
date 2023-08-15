from flask import Flask, request, jsonify, render_template,redirect,url_for,session
import db
Registration = Flask(__name__)
Registration.secret_key = "SUPER-SECRET"
connect = db.DBconnect()

@Registration.route('/register', methods = ["GET", "POST"])
def reg():
    if request.method == 'GET':
        return render_template('register_team.html')
    else:
        username = request.form['username']
        password = request.form['password']
        user = db.get_users(connect, username)
        if user:
            return redirect(url_for('reg_not_complete'))
        db.add_users(connect, username, password)
        return redirect(url_for('login'))

@Registration.route('/login', methods = ["GET"])
def login():
    return render_template('login_team.html')

@Registration.route('/', methods = ["GET"])
def default():
    return "Hello"

@Registration.route('/complete')
def reg_complete():
    return "Registration has been completed"

@Registration.route('/not/complete')
def reg_not_complete():
    return "Registration has not been completed"

if (__name__) == 'main':
    db.DBcreate(connect)
    Registration.run(debug = True)
