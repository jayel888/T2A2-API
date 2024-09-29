from flask import Blueprint, request
from datetime import timedelta

from models.user import User, user_schema, UserSchema
from init import bcrypt, db
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity



auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # retrieves the data from the body of the request
        body_data = UserSchema().load(request.get_json())
        # creates an instance of the User model
        user = User(
            name = body_data.get("name"),
            email = body_data.get("email")
        )
        # hashes the password
        password = body_data.get("password")
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        # Adds and commits to the DB
        db.session.add(user)
        db.session.commit()
        # Returns an acknowledgement
        return user_schema.dump(user), 201
    except IntegrityError as err:
        # not null violation
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 400
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email address already in use"}, 400

@auth_bp.route("/login", methods=["POST"])
def user_login():
    # retrieves data from the body of the request
    body_data = request.get_json()
    # locates the user in the DB with matching email address
    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)
    # Checks if the user exists and password is matching
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # create JWT
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        # acknowledgement
        return {"email": user.email, "is_admin": user.is_admin, "token": token}
    else:
        return {"error": "Incorrect email or password"}, 400

@auth_bp.route("/users/", methods=["PUT", "PATCH"])
@jwt_required()
def update_user():
    body_data = UserSchema().load(request.get_json(), partial=True)
    password = body_data.get("password")
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)

    if user:
        user.name = body_data.get("name") or user.name
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        db.session.commit()
        return user_schema.dump(user)
    else:
        return {"error": "User does not exist"}