from flask import Flask, request, jsonify, render_template,redirect,url_for,flash
import db
Registration = Flask(__name__)
connection = db.connect_to_database()

@Registration.route('/')
def default():
    return "Hello"

@Registration.route('/complete')
def reg_complete():
    return "Registration has been completed"

@Registration.route('/not/complete')
def reg_not_complete():
    return "Registration has not been completed"

  
  
  
  
if (__name__) == 'main':
    Registration.run(debug = True)