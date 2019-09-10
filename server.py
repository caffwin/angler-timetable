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
        print('Current logged in user is: ' + str(session['user_id']))

    else:
        print('No user currently logged in.')

    return render_template('homepage.html', user=user)


def get_hashed_password(plain_text_password):
    """Takes in a plain text password and returns the hashed/salted password"""
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def check_password(plain_text_password, hashed_password):
    """Takes in plain text password & hashed password and compares them
    True if match, False if no match"""
    return bcrypt.checkpw(plain_text_password, hashed_password)




@app.route("/register", methods=["GET"])
def registration_form():

    return render_template("register_page.html")


def register_user():
    # Work on this
    return redirect("/")
    

@app.route("/login", methods=["GET"])
def login_form():

    return render_template("login_page.html")
    # Instead of this, figure out a way to create a pop up for easy login without page refresh

if __name__ == "__main__":

    app.debug = False
    app.run(debug=True)
    # app.run()
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')