from datetime import date

from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.workouts import Workout
from models.exercises import Exercises

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

    exercises = [
        Exercises(
            exercise_name = "Bench Press",
            target_area = "Chest/Triceps",
            category = "Hypertrophy/Strength",
            description = "Maintain slight arch in back, drive feet into ground, shoulders pinned back, bring bar to lower chest maintaining wrists directly over elbows. Focus tension on chest"
        ),
        Exercises(
            exercise_name = "Squat",
            target_area = "Lower body",
            category = "Hypertrophy/Strength",
            description = "Rest bar on upper traps, shoulders pinned back, brace core, lead with your hips going back, maintain bar over middle of feet."
        ),
        Exercises(
            exercise_name = "Deadlift",
            target_area = "Lower body/Back",
            category = "Strength",
            description = "Brace core before lift, maintain neutral spine alignment during lift. Keep bar touching legs throughout entire lift"
        )
    ]

    db.session.add_all(exercises)
    db.session.commit()
    print("Tables Seeded Successfully")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped successfully")