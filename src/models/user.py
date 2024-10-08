from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp

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

    # validation for email, ensuring it meets specific requirements
    email = fields.String(required=True, validate=Regexp("^\S+@\S+\.\S+$", error="Invalid email format."))

    class Meta:
        fields = ("id","name","email","password","is_admin", "workouts")
        ordered=True
# Handle a single user object
user_schema = UserSchema(exclude=["password"])

# Handle a list of user objects
users_schema = UserSchema(exclude=["password"], many=True)