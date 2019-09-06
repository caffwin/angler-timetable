from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from datetime import datetime

from model_constants import (
BAIT_TYPE, WEATHER_INTERVALS,
WEATHER_CONDITIONS
)


db = SQLAlchemy()

"""Data Model for Angler Timetable"""

# General idea: database stores fish species/catch conditions
# One user may have many fish in their list of fish to catch
# Eventually, the user will be able to query for only the fish they still need and omit the rest

# Need:
# User table
# Fish table
# User-Fish table

# One user has many fish and any given fish may be favourited by more than one user
# Many to many relationship

class User(db.Model):

    # Users create rows in the database by signing up, and have lists of fish that they may
    # choose to view. By default, the full list is viewable.
    
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(150))

    def __repr__(self):
        """Provides information on the user."""
        return 'User ID: {}, First Name: {}, Last Name: {}, Username: {}'.format(self.user_id, self.fname, self.lname, self.username)


class Fish(db.Model):
    # List of all fish with specific weather requirements
    # Each fish has an official in-game name, image, bait type, weather condition requirement
    
    # Notes:
    
    # There may be more than one type of bait that works
    # The bait may be a "mooch" - a different fish. If it's a different fish, how can this
    # be handled? 

    # Weather conditions may be flexible (there may be more than one)
    # If weather isn't one specific weather pattern, it will be X > Y where X may vary and Y 
    # is set as a specific condition that does not change 
         
    # Time is always concrete - fish may only be available between a certain period of time
    # This time period never changes

    # Some fish are available for more than one "block" of time - create start and end times
    # in the form of two arrays, with matching respective indices? 

    # Example:
    # Start: [08:00, 20:00]
    # End:   [16:00, 04:00]
    #           0      1
    # First time slot begins at start[0], finishes end[0]
    # Second time slot begins at start[1], finishes end[1]

    __tablename__ = "fishies"

    fish_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fish_name = db.Column(db.String(50), nullable=False)
    fish_location = db.Column(db.String(24), nullable=True)
    fish_img = db.Column(db.String(50), nullable=True)
    fish_bait = db.Column(db.String(50), nullable=True) # Can this be an array? # Use JSON type?
    fish_wc1 = db.Column(db.String(500), nullable=True) # same with this
    fish_wc2 = db.Column(db.String(500), nullable=True) 
    fish_timetable = db.Column(db.String(500), nullable=True)
    mooch_fish_name = db.Column(db.String(16), nullable=True)

    # Another idea for storing various bait and preceding weather conditions is to store them as an integer

    # Example:

    # 0 = Fair Skies
    # 1 = Clear Skies
    # 2 = Fog
    # 3 = Thunder
    # 4 = Dust Storms
    # 5 = Rain


    # 025 > 1 could mean Fair/Fog/Rain preceding Clear Skies are all valid

    fish_time_start = db.Column(db.String(8), nullable=True)
    fish_time_end = db.Column(db.String(8), nullable=True)

    def __repr__(self):
        """Provides information on the fish."""
        # Assuming weather condition is single item, not array
        return 'Fish ID: {}, fish name: {}, best bait: {}, required weather: {}'.format(self.fish_id, self.fish_name, self.fish_bait, self.fish_wc)


class FishList(db.Model):

    """A list of all fish that a user will see"""

    # List of all of the relationships between users and fish - if a row exists, it means the
    # user has this fish on their list

    # Subtractive system? ToFish table starts as full, and users will manually remove items 
    # rather than adding caught fish one by one

    __tablename__ = "fish_list"

    to_fish_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fish_id = db.Column(db.Integer, 
                        db.ForeignKey('fishies.fish_id')) 
    
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id'))
    # fav_date = db.Column(db.DateTime)

    user = db.relationship('User',
                           backref="fish_list",
                           order_by=to_fish_id)
    # Necessary to see how many fish have been favourited by a user

    fish = db.relationship('Fish')
    # No backref needed, not necessary to check how many users have favourited a specific fish

    def __repr__(self):
        """Provides information on the user-fish connection."""
        return 'User {} has favourited {} fish'.format(self.user, self.fish)


# Helper functions

def connect_to_db(app, db_uri='postgresql:///angler-timetable'):

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app 
    connect_to_db(app)
    print("Connected to DB.")
