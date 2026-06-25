from http import HTTPStatus


def read_root():
    return {"message": "(⌐■_■)👌"}


def Register(client):

    response = client.post(
        "/auth/",
        json={
            "username": "baianinhodemaua",
            "email": "baianinho@example.com",
            "password": "secret",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "baianinhodemaua",
        "email": "baianinho@example.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'baianinhodemaua',
                'email': 'baianinho@example.com',
                'id': 1,
            }
        ]
    }
