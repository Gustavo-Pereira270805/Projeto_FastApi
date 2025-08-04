from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}


def test_criar_usuario(client):
    response = client.post(
        "/users/",
        json={
            "name": "gustavo",
            "email": "gustavo@exemplo.com",
            "password": "segredo",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "name": "gustavo",
        "email": "gustavo@exemplo.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "name": "gustavo",
                "email": "gustavo@exemplo.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "name": "gustavo",
            "email": "gdnp@teste.com",
            "password": "novosegredo",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "name": "gustavo",
        "email": "gdnp@teste.com",
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}
