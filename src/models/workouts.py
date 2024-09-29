from init import db, ma
from marshmallow import fields

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date_completed = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer)
    notes = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # create relationship between User and Workout_exercises table
    user = db.relationship("User", back_populates="workouts")
    workout_exercises = db.relationship("WorkoutExercises", back_populates="workout", cascade="all, delete")

class WorkoutSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["id", "name", "email"])
    workout_exercises = fields.List(fields.Nested("WorkoutExercisesSchema", only=["exercise", "sets", "reps","weight", "rest_in_seconds"]))

    class Meta:
        fields = ("id", "date_completed", "duration", "notes", "user", "workout_exercises")
        ordered=True

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)