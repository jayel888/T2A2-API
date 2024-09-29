from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.workout_exercises import WorkoutExercises, workout_exercise_schema, workout_exercises_schema
from models.workouts import Workout, workout_schema
from models.exercises import Exercises


workout_exercise_bp = Blueprint("workout_exercises", __name__, url_prefix="/<int:workout_id>/exercise")

@workout_exercise_bp.route("/", methods=["POST"])
@jwt_required()
def add_exercise_to_workout(workout_id):   
    body_data = request.get_json()

    # Fetch the workout by ID
    stmt = db.select(Workout).filter_by(id=workout_id)
    workout = db.session.scalar(stmt)

    if workout:
        exercise_name = body_data.get("exercise_name")  # Assuming exercise name is provided
        exercise = db.session.scalar(db.select(Exercises).filter_by(exercise_name=exercise_name))

        if not exercise:
            # If the exercise doesn't exist, create it
            exercise = Exercises(
                exercise_name = body_data.get("exercise_name"),
                target_area = body_data.get("target_area"),
                category = body_data.get("category"),
                description = body_data.get("description")
            )
            db.session.add(exercise)
            db.session.commit()

        # Now add the exercise to the workout_exercises table
        workout_exercise = WorkoutExercises(
            workout=workout,
            exercise_id=exercise.id,  # Use the new or existing exercise's id
            sets=body_data.get("sets"),
            reps=body_data.get("reps"),
            weight=body_data.get("weight"),
            rest_in_seconds=body_data.get("rest_in_seconds")
        )

        db.session.add(workout_exercise)
        db.session.commit()

        return workout_schema.dump(workout), 201

    else:
        return {"error": f"Workout with id {workout_id} not found."}, 404
    
@workout_exercise_bp.route("/<int:workout_exercises_id>", methods=["DELETE"])
@jwt_required()
def delete_exercise_in_workout(workout_id, workout_exercises_id):
    stmt = db. select(WorkoutExercises).filter_by(id=workout_exercises_id)
    workout_exercise = db.session.scalar(stmt)

    if workout_exercise:
        db.session.delete(workout_exercise)
        db.session.commit()
        return {"message": f"Exercise id:{workout_exercise.exercise_id} deleted from workout {workout_exercise.workout_id} successfully."}
    
    else:
        return {"error": f"Exercise with id {workout_exercises_id} not found"}
    
@workout_exercise_bp.route("/<int:workout_exercises_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_exercise_in_workout(workout_id, workout_exercises_id):
    body_data = request.get_json()
    stmt = db.select(WorkoutExercises).filter_by(id=workout_exercises_id)
    workout_exercise = db.session.scalar(stmt)
    if workout_exercise:
        workout_exercise.sets = body_data.get("sets") or workout_exercise.sets
        workout_exercise.reps = body_data.get("reps") or workout_exercise.reps
        workout_exercise.weight = body_data.get("weight") or workout_exercise.weight
        workout_exercise.rest_in_seconds = body_data.get("rest_in_seconds") or workout_exercise.rest_in_seconds

        db.session.commit()
        return {"message": f"Exercise {workout_exercise.id} in workout {workout_exercise.workout_id} updated successfully"}
    
    else:
        return {"error": f"Exercise {workout_exercises_id} in Workout {workout_id} not found"}
