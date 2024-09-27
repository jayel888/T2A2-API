from init import db, ma
from marshmallow import fields

class User(db.Model):
    # Name of the table
    __tablename__ = "users"
    # Table Attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    workouts = db.relationship("Workout", back_populates="user")

class UserSchema(ma.Schema):
    workouts = fields.List(fields.Nested("WorkoutSchema", exclude=["user"]))
    class Meta:
        fields = ("id","name","email","password","is_admin", "workouts")

# Handle a single user object
user_schema = UserSchema(exclude=["password"])

# Handle a list of user objects
users_schema = UserSchema(exclude=["password"], many=True)