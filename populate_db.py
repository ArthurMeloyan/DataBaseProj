import requests
import random
from faker import Faker

fake = Faker()

BASE_URL = 'http://127.0.0.1:8000'

# List of measurements unit for random choice
unit_of_measurements = ["kg", "m", "cm", "g", "L", "km", "lb", "oz", "mm", "mL"]

# List of competitions names for random choice
competitions = [
    "Olympic Games",
    "FIFA World Cup",
    "Super Bowl",
    "UEFA Champions League",
    "Wimbledon",
    "The Masters (Golf)",
    "Tour de France (Cycling)",
    "NBA Finals",
    "Stanley Cup (Ice Hockey)",
    "Australian Open (Tennis)",
    "World Series (Baseball)",
    "Super Rugby",
    "NCAA March Madness (Basketball)",
    "Indianapolis 500 (Auto Racing)",
    "The Ashes (Cricket)",
    "UFC 264",
    "Ryder Cup (Golf)",
    "Copa America (Football)",
    "French Open (Tennis)",
    "Six Nations Championship (Rugby)",
    "Daytona 500 (Auto Racing)",
    "CONCACAF Gold Cup (Football)",
    "ICC Cricket World Cup",
    "NBA All-Star Game",
    "The Open Championship (Golf)",
    "NFL Pro Bowl",
    "UEFA Europa League",
    "Copa Libertadores (Football)",
    "Indian Premier League (Cricket)",
    "Boston Marathon (Athletics)",
    "Tokyo Marathon (Athletics)",
    "NASCAR Cup Series",
    "Preakness Stakes (Horse Racing)",
    "Boston Red Sox vs. New York Yankees (Baseball)",
    "UFC 257",
    "NHL All-Star Game",
    "FIBA Basketball World Cup",
    "BWF World Championships (Badminton)",
    "World Chess Championship",
    "NCAA College Football Playoff",
    "ICC T20 World Cup (Cricket)",
    "The Players Championship (Golf)",
    "NBA Summer League",
    "Tour Championship (Golf)",
    "Dubai World Cup (Horse Racing)",
    "MLB All-Star Game",
    "UFC Fight Night",
    "European Athletics Championships",
    "Paris-Roubaix (Cycling)",
    "World Swimming Championships"
]


# Function to create sport type
def create_sport_type():
    url = f"{BASE_URL}/sport_types/"
    data = {
        "unit_of_measurement": random.choice(unit_of_measurements),
        "name": fake.name(),
        "world_record": abs(round(fake.pyfloat(min_value=-1e8, max_value=1e8), 2)),
        "olympic_record": abs(round(fake.pyfloat(min_value=-1e8, max_value=1e8), 2))
    }
    response = requests.post(url, json=data)
    return response.json()


# Function to create result
def create_result():
    random_date = fake.date_between(start_date='-30y', end_date='today').strftime("%Y-%m-%d")
    url = f"{BASE_URL}/results/"
    data = {
        "competition_name": random.choice(competitions),
        "performance": fake.pyint(),
        "place": fake.pyint(),
        "date": random_date,
        "venue": fake.city(),
    }
    response = requests.post(url, json=data)
    return response.json()


# Function to create athlete
def create_athlete():
    url = f"{BASE_URL}/athletes/"
    data = {
        "win": fake.pyint(),
        "full_name": fake.name(),
        "birth_year": random.randint(1968, 2001),
        "country": fake.country(),
    }
    response = requests.post(url, json=data)
    return response.json()


# Populate Data Base with N sport types
for _ in range(10):
    create_sport_type()

# Populate Data Base with N athletes
for _ in range(10):
    create_athlete()

# Populate Data Base with N results
for _ in range(10):
    create_result()

print("Data Base population completed")  # Message to know that populating DB completed successfully



