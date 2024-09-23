from datetime import date

from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.workouts import Workout

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("seed")
def seed_tables():
    users = [
        User(
            name = "Jess Lee",
            email = "admin@gym.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin = True
        ),
        User(
            name = "Sharla",
            email = "sharla@gym.com",
            password = bcrypt.generate_password_hash("sharla1").decode("utf-8")
        )
    ]

    db.session.add_all(users)

    workouts = [
        Workout(
            date_completed = date(2024,8,20),
            duration = 90,
            notes = "Completed chest workout for hypertrophy, increased all weight by 2.5kg",
            user = users[0]
        ),
        Workout(
            date_completed = date.today(),
            duration = 57,
            notes = "Leg workout completed, lifted less weights than last session. Increase caloric intake",
            user = users[0]
        ),
        Workout(
            date_completed = date.today(),
            duration = 45,
            notes = "Cardio workout completed, ran 1km more than last session in the same time.",
            user = users[1]
        )
    ]

    db.session.add_all(workouts)
    db.session.commit()
    print("Tables Seeded Successfully")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped successfully")