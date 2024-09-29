from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.workout_exercises import WorkoutExercises, workout_exercise_schema, workout_exercises_schema
from models.workouts import Workout, workout_schema
from models.exercises import Exercises


workout_exercise_bp = Blueprint("workout_exercises", __name__, url_prefix="/<int:workout_id>/exercise")

# route to add an exercise to a workout
@workout_exercise_bp.route("/", methods=["POST"])
@jwt_required()
def add_exercise_to_workout(workout_id):
    # retrieve data from body of request 
    body_data = request.get_json()
    # check logged in user
    current_user = get_jwt_identity()
    # Fetch the workout by ID
    stmt = db.select(Workout).filter_by(id=workout_id)
    workout = db.session.scalar(stmt)

    # if workout exist and logged in user matches user who created workout:
    if workout and int(workout.user_id) == int(current_user):
        exercise_name = body_data.get("exercise_name")
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

        # Add the exercise to the workout_exercises table
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
        # return workout with exercises
        return workout_schema.dump(workout), 201
    
    elif not workout:
        # return error that workout doesn't exist
        return {"error": f"Workout with id {workout_id} not found."}, 404
    else:
        # return error that user doesn't have permission if they didn't create workout
        return {"error": "You do not have permission to modify this workout."}, 403
    
# Delete an exercise from a workout
@workout_exercise_bp.route("/<int:workout_exercises_id>", methods=["DELETE"])
@jwt_required()
def delete_exercise_in_workout(workout_id, workout_exercises_id):
    stmt = db. select(WorkoutExercises).filter_by(id=workout_exercises_id)
    workout_exercise = db.session.scalar(stmt)
    # if exercise exist, delete it
    if workout_exercise:
        db.session.delete(workout_exercise)
        db.session.commit()
        return {"message": f"Exercise id:{workout_exercise.exercise_id} deleted from workout {workout_exercise.workout_id} successfully."}, 200
    # else return error
    else:
        return {"error": f"Exercise with id {workout_exercises_id} not found"}, 404

# Update an exercise sets/reps/weight in a workout 
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
        return {"error": f"Exercise {workout_exercises_id} in Workout {workout_id} not found"}, 404
