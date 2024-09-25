from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.exercises import Exercises, exercise_schema, exercises_schema

exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises")

@exercises_bp.route("/")
def get_all_exercises():
    stmt = db.select(Exercises)
    exercises = db.session.scalars(stmt)
    return exercises_schema.dump(exercises)

@exercises_bp.route("/<int:exercise_id>")
def get_exercise(exercise_id):
    stmt = db.select(Exercises).filter_by(id=exercise_id)
    exercise = db.session.scalar(stmt)
    if exercise:
        return exercise_schema.dump(exercise)
    else:
        return {"error": f"Exercise with id:{exercise_id} cannot be found."}, 404