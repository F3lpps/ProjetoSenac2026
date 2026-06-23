from fast_zero.app import app
from fastapi.testclient import TestClient


def Ola_mundoHtml():
    client = TestClient(app)
    response = client.get('/teste')
    assert '<h1> Olá Mundo </h1>' in response.text
