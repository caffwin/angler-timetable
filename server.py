from jinja2 import StrictUndefined
from flask import (Flask, jsonify, render_template, redirect, request, flash,
                   session, url_for)

import bcrypt



app = Flask(__name__)


app.secret_key = "secret_key"
app.jinja_env.undefined = StrictUndefined

# Create login and sign up system





def get_hashed_password(plain_text_password):
    """Takes in a plain text password and returns the hashed/salted password"""
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def check_password(plain_text_password, hashed_password):
    """Takes in plain text password & hashed password and compares them
    True if match, False if no match"""
    return bcrypt.checkpw(plain_text_password, hashed_password)




if __name__ == "__main__":

    app.debug = False
    app.run(debug=True)
    # app.run()
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')