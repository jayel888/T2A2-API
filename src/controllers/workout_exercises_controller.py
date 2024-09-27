from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.workout_exercises import WorkoutExercises, workout_exercise_schema, workout_exercises_schema
from models.workouts import Workout
from models.exercises import Exercises


workout_exercise_bp = Blueprint("workout_exercises", __name__, url_prefix="/<int:workout_id>/exercises")

@workout_exercise_bp.route("/", methods=["POST"])
@jwt_required()
def add_exercise_to_workout(workout_id):
    # Retrieve the current user from the JWT
    current_user_id = get_jwt_identity()
    
    body_data = request.get_json()

    # Fetch the workout by ID
    stmt = db.select(Workout).filter_by(id=workout_id)
    workout = db.session.scalar(stmt)

    if workout and int(workout.user_id) == int(current_user_id):
        # Check if the exercise exists in the `exercises` table
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

        return workout_exercise_schema.dump(workout_exercise), 201

    elif not workout:
        return {"error": f"Workout with id {workout_id} not found."}, 404
    else:
        return {"error": "You do not have permission to modify this workout."}, 403