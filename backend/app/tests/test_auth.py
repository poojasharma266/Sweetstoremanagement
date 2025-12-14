def test_user_registration(client):
    response = client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "password": "strongpassword"
        }
    )

    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["email"] == "test@example.com"


def test_user_login(client):
    # register first
    client.post(
        "/api/auth/register",
        json={
            "email": "login@example.com",
            "password": "password123"
        }
    )

    response = client.post(
        "/api/auth/login",
        json={
            "email": "login@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
