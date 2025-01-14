from datetime import datetime, timedelta
from functools import wraps
from http import HTTPStatus
from zoneinfo import ZoneInfo

import jwt
from flask import g, jsonify, request

from app.config.settings import Settings
from app.domains.user.user_repository import UserRepository


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({
                'message': 'token is missing',
            }), HTTPStatus.UNAUTHORIZED
        try:
            data = jwt.decode(
                token, Settings().SECRET_KEY, algorithms=[Settings().ALGORITHM]
            )
            user_repository = UserRepository(g.db_session)
            current_user = user_repository.find_by_email_or_username(
                username=data['username']
            )
        except Exception:
            return jsonify({
                'message': 'token is invalid or expired',
            }), HTTPStatus.UNAUTHORIZED
        return f(current_user, *args, **kwargs)

    return decorated


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=Settings().ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, Settings().SECRET_KEY, algorithm=Settings().ALGORITHM
    )
    return encoded_jwt
