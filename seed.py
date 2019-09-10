from sqlalchemy import func
from model import User
from model import Fish
from model import FishList
from model import 
from datetime import datetime # For later

# Loads users into database

def load_users():
    """Loads users into database."""

    print("Load users")

    User.query.delete()

    for row in open("user_data.txt"):
        row = row.rstrip()
        fname, lname, username, email, password, description = row.split(",")

        user = User(fname = fname.strip(),
                    lname = lname.strip(),
                    username = username.strip(),
                    email = email.strip(),
                    password = password.strip()

        db.session.add(user)

    db.session.commit()


def load_fish():
    """Loads fish into database."""

    print("Loading fish")

    Fish.query.delete()

    for row in open("fish_data.txt"):
        row = row.rstrip()
        fish_name, fish_img, fish_location, fish_bait, fish_wc1, fish_wc2, fish_time_start, fish_time_end, mooch_fish_name = row.split(",")

        fish = Fish(fish_name = fish_name.strip(),
                    fish_img = fish_img.strip(),
                    fish_location = fish_area.strip(),
                    fish_bait = fish_bait.strip(),
                    fish_wc1 = fish_wc1.strip()),
                    fish_wc2 = fish_wc2.strip(),
                    fish_time_start = fish_time_start.strip(),
                    fish_time_end = fish_time_end.strip()
                    mooch_fish_name = mooch_fish_name.strip()

        db.session.add(fish)
        
    db.session.commit()


def load_fishlist():
    """Loading all fish lists"""

    print("Fish List")

    FishList.query.delete()

    """Load user's fish lists into database."""

    for row in open("fishlist_data.txt"):
        row = row.rstrip()
        user_id, fish_id = row.split(",")

        list_fish = FishList(user_id = user_id.strip(),
                            fish_id = fish_id.strip())

        db.session.add(list_fish)
        
    db.session.commit()

def load_weather():
    """Loading all weather conditions"""
    print("Weather List")

    WeatherType.query.delete()

    """Loads all available weather conditions into database."""

    for row in open("weather_data.txt"):
        row = row.rstrip()
        weather_condition = row
        # Nothing to split on since it's just one column

        weather = WeatherType(weather_condition = weather_condition.strip())
        
        db.session.add(weather)

    db.session.commit()


if __name__ == "__main__":

    connect_to_db(app)

    db.create_all() 

    load_users()
    load_fish()
    load_fishlist()