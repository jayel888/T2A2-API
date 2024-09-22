from init import db, ma

class User(db.Model):
    # Name of the table
    __tablename__ = "users"
    # Table Attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","name","email","password","is_admin")

# Handle a single user object
user_schema = UserSchema(exclude=["password"])

# Handle a list of user objects
users_schema = UserSchema(exclude=["password"], many=True)