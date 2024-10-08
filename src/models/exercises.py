from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, OneOf

# ensure only certain inputs accepted for category and target areas
VALID_CATEGORIES = ("Strength", "Hypertrophy", "Cardio", "Compound")
VALID_TARGET_AREAS = ("Chest", "Shoulders", "Back", "Legs", "Arms", "Core", "Cardio")

class Exercises(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String, nullable=False, unique=True)
    target_area = db.Column(db.String)
    category = db.Column(db.String)
    description = db.Column(db.String)

    # creating relationship between workout_exercises table
    workout_exercises = db.relationship("WorkoutExercises", back_populates="exercise")

class ExercisesSchema(ma.Schema):
    workout_exercises = fields.List(fields.Nested("WorkoutExercisesSchema", exclude=["exercise"]))
    # validation ensuring exercise name is greater than 3 characters and only alphanumeric characters. Must start with a capital letter
    exercise_name = fields.String(required=True, validate=And(Length(min=3, error="Exercise name must be at least 3 characters in length."), Regexp("^[A-Z][A-Za-z0-9 ]+$", error="Exercise name must start with a capital letter and have alphanumeric characters only.")))
    # must be one of the inputs above
    category = fields.String(validate=OneOf(VALID_CATEGORIES))
    target_area = fields.String(validate=OneOf(VALID_TARGET_AREAS, error="Invalid area selected. Must be either Chest, Shoulders, Back, Legs, Arms or Core"))

    class Meta:
        fields = ("id", "exercise_name", "target_area", "category", "description")
        ordered=True
        
exercise_schema = ExercisesSchema()

exercises_schema = ExercisesSchema(many=True)
