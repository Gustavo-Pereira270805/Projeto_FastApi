from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_curso.app import app

client = TestClient(app)


def test_root_deve_retornar_ola_mundo():
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"ola": "mundo"}
