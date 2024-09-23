from init import db, ma
from marshmallow import fields

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date_completed = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer)
    notes = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="workouts")

class WorkoutSchema(ma.Schema):
    class Meta:
        user = fields.Nested("UserSchema", only=["id", "name", "email"])
        fields = ("id", "date_completed", "duration", "notes", "user")
    
workout_schema = WorkoutSchema()

workouts_schema = WorkoutSchema(many=True)