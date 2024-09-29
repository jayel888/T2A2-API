from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.exercises import Exercises, exercise_schema, exercises_schema
from utils import authorise_as_admin

# create blueprint to register in main.py
exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises")

# GET route to fetch all exercises in the database
@exercises_bp.route("/")
def get_all_exercises():
    stmt = db.select(Exercises)
    exercises = db.session.scalars(stmt)
    return exercises_schema.dump(exercises)

# GET route to fetch specific exercise by ID
@exercises_bp.route("/<int:exercise_id>")
def get_exercise(exercise_id):
    stmt = db.select(Exercises).filter_by(id=exercise_id)
    exercise = db.session.scalar(stmt)
    if exercise:
        return exercise_schema.dump(exercise)
    else:
        return {"error": f"Exercise with id:{exercise_id} cannot be found."}, 404

# POST request to add an exercise to database
@exercises_bp.route("/", methods=["POST"])
# must be logged in but any user can add
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
        return {"error": f"{e}"}, 500
    
@exercises_bp.route("/<int:exercise_id>", methods=["DELETE"])
@jwt_required()
def delete_exercise(exercise_id):
    # Only admin can delete exercises from database, but users can still edit.
    is_admin = authorise_as_admin()
    if not is_admin:
        return {"error": "User is not authorised to perform this action."}
    # filter by exercise id
    stmt = db.select(Exercises).filter_by(id=exercise_id)
    exercise = db.session.scalar(stmt)
    # if exercise exists, delete it.
    if exercise:
        db.session.delete(exercise)
        db.session.commit()
        # returns acknowledgement
        return {"message": f"The exercise {exercise_id}. {exercise.exercise_name} deleted successfully."}
    # else returns error
    else:
        return {"error": f"Exercise with id {exercise_id} cannot be found."}, 404
    
# request to update/edit an existing exercise
@exercises_bp.route("/<int:exercise_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_exercise(exercise_id):
    body_data = exercise_schema.load(request.get_json(), partial=True)
    stmt = db.select(Exercises).filter_by(id=exercise_id)
    exercise = db.session.scalar(stmt)
    # if exercise exists, update.
    if exercise:
        # retrieve data from body of request
        exercise.exercise_name = body_data.get("exercise_name") or exercise.exercise_name
        exercise.target_area = body_data.get("target_area") or exercise.target_area
        exercise.category = body_data.get("category") or exercise.category
        exercise.description = body_data.get("description") or exercise.description

        # commit changes and return updated exercise details
        db.session.commit()
        return exercise_schema.dump(exercise)
    # else returns an error
    else:
        return {"error": f"Exercise with id:{exercise_id} cannot be found."}, 404