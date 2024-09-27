from init import db, ma
from marshmallow import fields

class Exercises(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String, nullable=False, unique=True)
    target_area = db.Column(db.String)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    workout_exercises = db.relationship("WorkoutExercises", back_populates="exercise")

class ExercisesSchema(ma.Schema):
    workout_exercises = fields.List(fields.Nested("WorkoutExercisesSchema", exclude=["exercise"]))
    class Meta:
        fields = ("id", "exercise_name", "target_area", "category", "description")
        ordered=True
exercise_schema = ExercisesSchema()

exercises_schema = ExercisesSchema(many=True)
