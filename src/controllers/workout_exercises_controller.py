from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.workout_exercises import WorkoutExercises, workout_exercise_schema, workout_exercises_schema
from models.workouts import Workout



workout_exercise_bp = Blueprint("workout_exercises", __name__, url_prefix="/<int:workout_id>/exercises")

@workout_exercise_bp.route("/", methods=["POST"])
@jwt_required()
def add_exercise_to_workout(workout_id):
    # Retrieve the current user from the JWT
    current_user_id = get_jwt_identity()  # Assumes JWT identity is set to user_id
    print(f"Current user ID: {current_user_id}")  # Debugging
    
    body_data = request.get_json()

    # Fetch the workout by ID
    stmt = db.select(Workout).filter_by(id=workout_id)
    workout = db.session.scalar(stmt)
    
    if workout:
        print(f"Workout user ID: {workout.user_id}")  # Debugging

        # Check if the current user is the creator of the workout
        if int(workout.user_id) == int(current_user_id):
            # Proceed to add exercise
            exercise = WorkoutExercises(
                workout=workout,
                exercise_id=body_data.get("exercise_id"),
                sets=body_data.get("sets"),
                reps=body_data.get("reps"),
                weight=body_data.get("weight"),
                rest_in_seconds=body_data.get("rest_in_seconds")
            )
            db.session.add(exercise)
            db.session.commit()
            return workout_exercise_schema.dump(exercise), 201
        else:
            return {"error": "You do not have permission to modify this workout."}, 403
    else:
        return {"error": f"Workout with id {workout_id} not found."}, 404



