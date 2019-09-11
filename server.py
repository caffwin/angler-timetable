from jinja2 import StrictUndefined
from flask import (Flask, jsonify, render_template, redirect, request, flash,
                   session, url_for)
from werkzeug.utils import secure_filename
from flask_debugtoolbar import DebugToolbarExtension
from random import randint
from model import User, Fish, FishList, connect_to_db, db

import requests
import bcrypt

app = Flask(__name__)

app.secret_key = "secret_key"
app.jinja_env.undefined = StrictUndefined

# Create login and sign up system


@app.route('/')
def index():
    """Homepage"""

    user = None

    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        print('ID of user currently logged in: ' + str(session['user_id']))

    else:
        print('No one is currently logged in.')

    return render_template('homepage.html', user=user)


def get_hashed_password(plain_text_password):
    """Takes in a plain text password and returns the hashed/salted password"""
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def check_password(plain_text_password, hashed_password):
    """Takes in plain text password & hashed password and compares them
    True if match, False if no match"""
    return bcrypt.checkpw(plain_text_password, hashed_password)




@app.route("/register", methods=["GET"])
def show_registration_form():
    """Displays registration page"""

    return render_template("register_page.html")


@app.route("/register", methods=["POST"])
def register_user():
    # Work on this

    fname = request.form.get('reg-fname')
    lname = request.form.get('reg-lname')
    username = request.form.get('reg-username')
    regex_username = re.match("^[a-zA-Z0-9_.-]+$", username)
    email = request.form.get('reg-email')
    regex_email = re.findall(r'[^@]+@[^@]+\.[^@]+', email)
    password = request.form.get('reg-pw')
    hashed_pw = get_hashed_password(password)
    

    user = User.query.filter(User.email == email).first() # Can be any unique field to ID specific user

    if user == None: 
        print("No current user - registering...") 

        if regex_username is not None:
            print("Valid alphanumeric username!")
            # Username is valid
            if regex_email is not None: 
                # Email is valid
                print("Valid email format!")
                user = User(username=username, password=hashed_pw, email=email, fname=fname, lname=lname)
                db.session.add(user)
                db.session.commit()
                session['user_id'] = user.user_id
                print("User registered!")
        else:
            print("One or more fields are invalid! Please try again.")
            # Make this a popup instead? Or red text that appears, while starring incomplete/invalid fields
            return redirect('/register')
    # Other cases to consider for error handling: 
    # User enters an email that is already in use
        # Separate user_by_email variable? 
    # User enters a username that is already in use
    else: 
        print("The submitted email/username is already in use! Please submit a different email.")

    

    return redirect('/')
    

@app.route("/login", methods=["GET"])
def login_form():

    return render_template("login_page.html")
    # Instead of this, figure out a way to create a pop up for easy login without page refresh

@app.route('/logout')
def logout_process():
    """Logs user out and removes user from the current session"""
    del session['user_id']
    return redirect('/')


if __name__ == "__main__":

    app.debug = False
    app.run(debug=True)
    # app.run()
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')