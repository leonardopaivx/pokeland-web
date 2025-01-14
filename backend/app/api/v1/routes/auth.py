import datetime
from http import HTTPStatus

from flask import Blueprint, g, jsonify
from flask_pydantic import validate
from werkzeug.security import check_password_hash

from app.domains.user.user_repository import UserRepository
from app.domains.user.user_schemas import UserLogin
from app.helpers.security import create_access_token

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.post('')
@validate(on_success_status=200)
def authenticate(body: UserLogin):
    auth = body

    if not auth or not auth.username or not auth.password:
        return jsonify({
            'message': 'could not verify',
            'WWW-Authenticate': 'Basic auth="Login required"',
        }), HTTPStatus.UNAUTHORIZED

    user_repository = UserRepository(g.db_session)

    user = user_repository.find_by_email_or_username(username=auth.username)

    if not user:
        return jsonify({
            'message': 'user not found',
        }), HTTPStatus.UNAUTHORIZED

    if user and check_password_hash(user.password, auth.password):
        token = create_access_token({'username': user.username})
        return jsonify({
            'message': 'Validated successfully',
            'token': token,
            'exp': datetime.datetime.now() + datetime.timedelta(hours=12),
        })

    return jsonify({
        'message': 'could not verify',
        'WWW-Authenticate': 'Basic auth="Login required"',
    }), HTTPStatus.UNAUTHORIZED
