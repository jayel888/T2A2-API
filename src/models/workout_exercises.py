from init import db, ma
from marshmallow import fields

class WorkoutExercises(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)

    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    weight = db.Column(db.Float)
    rest_in_seconds = db.Column(db.Integer)

    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercises", back_populates="workout_exercises")

class WorkoutExercisesSchema(ma.Schema):
    workout = fields.Nested("WorkoutSchema", only=["date_completed"])
    exercise = fields.Nested("ExercisesSchema", only=["exercise_name"])
    class Meta:
        fields = ("id", "sets", "reps", "weight", "rest_in_seconds", "workout", "exercise")
        ordered=True
workout_exercise_schema = WorkoutExercisesSchema()
workout_exercises_schema = WorkoutExercisesSchema(many=True)