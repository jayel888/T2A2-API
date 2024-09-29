from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

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
    
@exercises_bp.route("/", methods=["POST"])
@jwt_required()
def add_exercise():
    body_data = exercise_schema.load(request.get_json())

    # Check if an exercise with the same name already exists
    existing_exercise = db.session.scalar(
        db.select(Exercises).filter_by(exercise_name=body_data.get("exercise_name"))
    )
    
    if existing_exercise:
        # Return an error message if the exercise already exists
        return {"error": f"Exercise '{body_data.get('exercise_name')}' already exists."}, 400

    # Create a new exercise if it doesn't exist
    exercise = Exercises(
        exercise_name=body_data.get("exercise_name"),
        target_area=body_data.get("target_area"),
        category=body_data.get("category"),
        description=body_data.get("description")
    )

    try:
        db.session.add(exercise)
        db.session.commit()
        return exercise_schema.dump(exercise), 201
    except Exception as e:
        # Catch any other exceptions and return an error message
        db.session.rollback()
        return {"error": "An error occurred while adding the exercise."}, 500
    
@exercises_bp.route("/<int:exercise_id>", methods=["DELETE"])
@jwt_required()
def delete_exercise(exercise_id):
    stmt = db.select(Exercises).filter_by(id=exercise_id)
    exercise = db.session.scalar(stmt)
    if exercise:
        db.session.delete(exercise)
        db.session.commit()
        return {"message": f"The exercise {exercise_id}. {exercise.exercise_name} deleted successfully."}
    else:
        return {"error": f"Exercise with id {exercise_id} cannot be found."}, 404
    

@exercises_bp.route("/<int:exercise_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_exercise(exercise_id):
    body_data = exercise_schema.load(request.get_json(), partial=True)
    stmt = db.select(Exercises).filter_by(id=exercise_id)
    exercise = db.session.scalar(stmt)
    if exercise:
        exercise.exercise_name = body_data.get("exercise_name")
        exercise.target_area = body_data.get("target_area") or exercise.target_area
        exercise.category = body_data.get("category") or exercise.category
        exercise.description = body_data.get("description") or exercise.description

        db.session.commit()
        return exercise_schema.dump(exercise)
    
    else:
        return {"error": f"Exercise with id:{exercise_id} cannot be found."}, 404