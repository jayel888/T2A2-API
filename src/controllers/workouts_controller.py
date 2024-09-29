from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.workouts import Workout, workout_schema, workouts_schema

from controllers.workout_exercises_controller import workout_exercise_bp

workouts_bp = Blueprint("workouts", __name__, url_prefix="/workouts")
workouts_bp.register_blueprint(workout_exercise_bp)

# /workouts - GET - fetch all workouts in database
@workouts_bp.route("/")
def get_all_workouts():
    stmt = db.select(Workout).order_by(Workout.date_completed.desc())
    workouts = db.session.scalars(stmt)
    return workouts_schema.dump(workouts)

# /workouts/<id> - GET - fetch specific workout
@workouts_bp.route("/<int:workout_id>")
def get_workout(workout_id):
    stmt = db.select(Workout).filter_by(id=workout_id)
    workout = db.session.scalar(stmt)
    if workout:
        return workout_schema.dump(workout)
    else:
        return {"error": f"Workout with id:{workout_id} cannot be found."}, 404

# /workouts - POST - Create a new workout
@workouts_bp.route("/", methods=["POST"])
@jwt_required()
def add_workout():
    body_data = request.get_json()
    workout = Workout(
        date_completed = date.today(),
        duration = body_data.get("duration"),
        notes = body_data.get("notes"),
        user_id = get_jwt_identity()
    )

    db.session.add(workout)
    db.session.commit()

    return workout_schema.dump(workout)

# /workouts/<id> - DELETE - Delete a workout
@workouts_bp.route("/<int:workout_id>", methods=["DELETE"])
@jwt_required()
def delete_workout(workout_id):
    stmt = db.select(Workout).filter_by(id=workout_id)
    workout = db.session.scalar(stmt)
    if workout:
        if workout.user_id != get_jwt_identity():
            return {"error": "Unable to perform operation. Only owners are allowed to execute this operation"}
        
        db.session.delete(workout)
        db.session.commit()
        return {"message": f"Workout {workout_id} completed on {workout.date_completed} has been deleted"}
    else:
        return {"error": f"Workout entry with id:{workout_id} does not exist."}, 404
    
# /workouts/<id> - PUT,PATCH - Edit a workout entry
@workouts_bp.route("/<int:workout_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_workout(workout_id):
    body_data = request.get_json()
    stmt = db.select(Workout).filter_by(id=workout_id)
    workout = db.session.scalar(stmt)
    if workout:
        if workout.user_id != get_jwt_identity():
            return {"error": "Unable to perform operation. Only owners are allowed to execute this operation"}
        
        workout.duration = body_data.get("duration") or workout.duration
        workout.notes = body_data.get("notes") or workout.notes

        db.session.commit()
        return workout_schema.dump(workout)
    
    else:
        return {"error": f"Workout with id:{workout_id} cannot be found."}, 404
    