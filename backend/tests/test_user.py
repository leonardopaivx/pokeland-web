from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/api/v1/users',
        json={
            'username': 'leonardo',
            'email': 'leonardo@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json == {
        'username': 'leonardo',
        'email': 'leonardo@example.com',
        'id': 1,
    }


def test_create_user_username_already_exists(client, user):
    response = client.post(
        '/api/v1/users',
        json={
            'username': user.username,
            'email': 'leonardo2@example.com',
            'password': 'secret123',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'message': 'Username already exists'}


def test_create_user_email_already_exists(client, user):
    response = client.post(
        '/api/v1/users',
        json={
            'username': 'leonardo2',
            'email': user.email,
            'password': 'secret123',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'message': 'Email already exists'}


def test_create_user_invalid_payload(client):
    response = client.post(
        '/api/v1/users',
        json={
            'username': 'leonardo',
        },
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    assert 'validation_error' in response.json
    assert 'body_params' in response.json['validation_error']

    errors = response.json['validation_error']['body_params']
    assert any(
        error['loc'] == ['email'] and error['msg'] == 'Field required'
        for error in errors
    )
    assert any(
        error['loc'] == ['password'] and error['msg'] == 'Field required'
        for error in errors
    )
