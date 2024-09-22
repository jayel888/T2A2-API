from flask import Blueprint
from init import db, bcrypt
from models.user import User

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("seed")
def seed_tables():
    users = [
        User(
            name = "Jess",
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
    db.session.commit()
    print("Tables Seeded Successfully")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped successfully")