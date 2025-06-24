import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["octofit_db"]

# Insert test users
db.users.insert_many([
    {"email": "alice@example.com", "name": "Alice", "password": "alicepass"},
    {"email": "bob@example.com", "name": "Bob", "password": "bobpass"},
    {"email": "carol@example.com", "name": "Carol", "password": "carolpass"}
])

# Insert test teams
db.teams.insert_many([
    {"name": "Team Alpha", "members": ["alice@example.com", "bob@example.com"]},
    {"name": "Team Beta", "members": ["carol@example.com"]}
])

# Insert test activities
db.activity.insert_many([
    {"user": "alice@example.com", "type": "run", "duration": 30, "date": datetime(2025, 6, 24)},
    {"user": "bob@example.com", "type": "walk", "duration": 45, "date": datetime(2025, 6, 23)},
    {"user": "carol@example.com", "type": "cycle", "duration": 60, "date": datetime(2025, 6, 22)}
])

# Insert test workouts
db.workouts.insert_many([
    {"user": "alice@example.com", "activity": "run", "date": datetime(2025, 6, 24)},
    {"user": "bob@example.com", "activity": "walk", "date": datetime(2025, 6, 23)}
])

# Insert test leaderboard
db.leaderboard.insert_many([
    {"team": "Team Alpha", "points": 150},
    {"team": "Team Beta", "points": 80}
])

print("Test data inserted into octofit_db.")
