from http import HTTPStatus


def test_authenticate_success(client, user):
    response = client.post(
        '/api/v1/auth',
        json={
            'username': user.username,
            'password': 'testtest',
        },
    )

    assert response.status_code == HTTPStatus.OK
    data = response.json
    assert data['message'] == 'Validated successfully'
    assert 'token' in data
    assert 'exp' in data


def test_authenticate_user_not_found(client):
    response = client.post(
        '/api/v1/auth',
        json={
            'username': 'Teste',
            'password': 'testtest',
        },
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    data = response.json
    assert data['message'] == 'user not found'


def test_authenticate_invalid_password(client, user):
    response = client.post(
        '/api/v1/auth',
        json={
            'username': user.username,
            'password': 'Teste',
        },
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    data = response.json
    assert data['message'] == 'could not verify'
    assert data['WWW-Authenticate'] == 'Basic auth="Login required"'
