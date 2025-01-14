from http import HTTPStatus

from flask import Blueprint, g, jsonify
from flask_pydantic import validate
from werkzeug.security import generate_password_hash

from app.domains.user.user import User
from app.domains.user.user_repository import UserRepository
from app.domains.user.user_schemas import UserPublic, UserSchema

user_bp = Blueprint('user', __name__, url_prefix='/users')


@user_bp.post('')
@validate(on_success_status=201)
def create_user(body: UserSchema):
    user = body
    user_repository = UserRepository(g.db_session)

    db_user = user_repository.find_by_email_or_username(
        email=user.email, username=user.username
    )

    if db_user:
        if db_user.username == user.username:
            return jsonify({
                'message': 'Username already exists'
            }), HTTPStatus.BAD_REQUEST
        elif db_user.email == user.email:
            return jsonify({
                'message': 'Email already exists'
            }), HTTPStatus.BAD_REQUEST

    pass_hash = generate_password_hash(user.password)

    db_user = User(
        username=user.username, password=pass_hash, email=user.email
    )
    user_repository.create(db_user)

    return UserPublic(
        id=db_user.id, username=db_user.username, email=db_user.email
    )
