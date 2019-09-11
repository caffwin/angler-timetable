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

# nullable=False is a required field
# can include "unique" and "default" variables


#### User Class #####

class User(db.Model):

    # Users create rows in the database by signing up, and have lists of fish that they may
    # choose to view. By default, the full list is viewable.
    
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150), nullable=False)

    # All fields required when signing up

    def __repr__(self):
        """Provides information on the user."""
        return 'User ID: {}, First Name: {}, Last Name: {}, Username: {}'.format(self.user_id, self.fname, self.lname, self.username)


##### Fish Class #####

fish_bait_enum = Enum(*BAIT_TYPE, name="bait_type")
# fish_wc2_enum = Enum(*WEATHER_CONDITIONS, name="weather_conditions") # Preceding weather conditions

class Fish(db.Model):

    """Fish class, including weather and time"""
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

    # For now, assume that there is only one start and end time

    __tablename__ = "fish"

    fish_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fish_name = db.Column(db.String(50), nullable=False)
    fishing_hole = db.Column(db.String(24), nullable=False) 
    fish_img = db.Column(db.String(50), nullable=True)
    fish_bait = db.Column(fish_bait_enum, nullable=False) 
    fish_wc1 = db.Column(db.String(500), default="None", nullable=True) # Some fish may not have a weather requirement
    fish_wc2 = db.Column(fish_wc2_enum, default="None", nullable=True) 
    fish_time_start = db.Column(db.String(500), default="None", nullable=True)
    fish_time_end = db.Column(db.String(500), default="None", nullable=True)
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

    fish_time_start = db.Column(db.String(8), nullable=True) # Some fish may not have start or end time
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
                        db.ForeignKey('fish.fish_id')) 
    
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
        """Provides information on each user-fish relationship."""
        return 'User {} has favourited {} fish'.format(self.user, self.fish)


##### Weather-related Classes #####

class WeatherType(db.Model):
    """Weather class"""

    __tablename__ = "weather_types"

    weather_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    weather_name = db.Column(db.String(16), nullable=False)
    
    def __repr__(self):
        """Prints weather type."""
        return 'Weather type is: {}'.format(self.weather_name)



class WeatherRequired(db.Model): 
    """Table containing fish with weather requirements"""

    # The weather requirement must exist for this fish to be eligible for capture 
    # This weather requirement may need to be preceded by a weather window
    # This is the wc1 attribute for the fish class

    __tablename__ = "weather_reqs" # Think of a better name?

    weather_required_id = db.Column(db.Integer, autoincrement=True, primary_key=True) # PK
    fish = db.relationship('Fish') # FK
    weather = db.relationship('WeatherType') # FK

    def __repr__(self):
        """Provides information on the required weather condition for a specific fish."""
        return 'The {} fish is available under {} condition'.format(self.fish.fish_name, self.weather.weather_name)

        # Eventually: print out a different string stating the preceding weather if that exists


class WeatherPreceding(db.Model):
    """Table containing fish that have a weather requirement that must be preceded by additional weather requirement(s)."""

    # If a row exists in this table, it means:
    # 1) The fish is only catchable under a certain weather condition and
    # 2) That weather condition must be preceded by another weather condition
    # 3) There may be more than one weather condition that can precede the required weather condition,
    # so several rows may exist for one specific fish
    # Example: Clear Skies > Thunder or Fair Skies > Thunder or Fog > Thunder for one specific fish
    # where wc1 = Thunder and wc2 = Clear Skies, Fair Skies, or Fog

    # This is the wc2 attribute for the fish class
    # Also add in relationship with WeatherRequired class - WeatherPreceding only exists if
    # WeatherRequired exists 

    __tablename__ = "pre_weather" # Think of a better name?

    weather_preceding_id = db.Column(db.Integer, autoincrement=True, primary_key=True) # PK
    fish_id = db.Column(db.Integer, 
                        db.ForeignKey('fish.fish_id')) # FK
    weather_id = db.Column(db.Integer, 
                        db.ForeignKey('weather_reqs.weather_id')) # FK
    req_weather_id = db.Column(db.Integer, 
                        db.ForeignKey('weather_reqs.weather_required_id')) # FK



##### Region Class #####


# Still deciding how to implement this

# region_enum = 

class Region(db.Model):
    """Regions in Eorzea, created to sort fish by region"""

    __tablename__ = "regions"

    region_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    region_name = db.Column(db.String(24), nullable=False)
    # subregion_id = db.Column(db.Integer, 
    #                     db.ForeignKey("subregions.subregion_id")) # Linked by this attribute

    # subregion = db.relationship("Subregion",
    #                             backref="regions",
    #                             order_by="region_id")

    # Regions have numerous subregions

    def __repr__(self):
        """Prints region name"""

        return '<Region ID: {}, Region name: {}>'.format(self.region_id, self.region_name)
        # Try: regions.region_id and subregion.subregion_id


class RegionSubregion(db.Model):
    """Region to subregion relationships exist as rows here"""


# subregion_enum = 

class Subregion(db.Model):
    """Location model, each World has several regions"""

    __tablename__ = "subregions"

    subregion_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fishing_hole = db.relationship("FishingHole",
                           backref="subregions",
                           order_by=subregion_id)
    # Subregions have numerous fishing holes

    def __repr__(self):
        """Prints"""

        return '<User ID: {}, Bird ID: {}>'.format(self.user_id, self.bird_id)

fishing_hole_enum = ENUM(FISHING_HOLES, name="fishing_holes")

class FishingHole(db.Model):
    """Fish belong to specific Fishing holes, each fish can only be found at one specific hole"""
    # Fishing holes are the leaf nodes to the world tree model (region-subregion-fishing_hole)
    # One to many relationship between fishing hole and big fish

    __tablename__ = "fishing_holes"

    fishing_hole_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fishing_hole_name = db.Column(fishing_hole_enum, nullable=False)

    def __repr__(self):
        """Prints the name of the current fishing hole."""
        return 'The current fishing hole is: {}'.format(self.fishing_hole_name)

class WhereIsTheFish(db.Model):
    """Relationship between fish and fishing holes"""


##### Helper functions #####

def connect_to_db(app, db_uri='postgresql:///angler-timetable'):
    """Connects database to flask app"""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    """Allows user to work with database directly"""

    from server import app 
    connect_to_db(app)
    print("Connected to DB.")
