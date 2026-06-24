from http import HTTPStatus

from fastapi.testclient import TestClient

from ViajeiAPI.app import app


@app.get('/')
def read_root():
    return {'message': '( ͡° ͜ʖ ͡° )'}


def Register():
    client = TestClient(app)

    response = client.post(
        '/auth/',
        json={
            'username': 'baianinhodemaua',
            'email': 'baianinho@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'baianinhodemaua',
        'email': 'baianinho@example.com',
        'id': 1,
    }
