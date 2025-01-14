from http import HTTPStatus


def test_health_check(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    print(response)
    assert response.json == {'status': True}
