from jwt import decode

from app.helpers.security import create_access_token
from backend.app.config.settings import Settings


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(token, Settings().SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']
