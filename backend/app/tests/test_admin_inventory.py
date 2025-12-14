from app.db.session import SessionLocal
from app.db.models import User


def register_and_login(client, email, password, role="USER"):
    client.post("/api/auth/register", json={
        "email": email,
        "password": password,
        "role": role
    })

    token = client.post("/api/auth/login", json={
        "email": email,
        "password": password
    }).json()["access_token"]

    return {"Authorization": f"Bearer {token}"}


def create_sweet(client, headers, quantity):
    response = client.post(
        "/api/sweets",
        headers=headers,
        json={
            "name": "Barfi",
            "category": "Indian",
            "price": 15.0,
            "quantity": quantity
        }
    )
    return response.json()["id"]


def test_admin_can_restock_sweet(client):
    admin_headers = register_and_login(
    client, "admin@test.com", "adminpass", role="ADMIN"
)

    sweet_id = create_sweet(client, admin_headers, 1)

    response = client.post(
        f"/api/sweets/{sweet_id}/restock",
        headers=admin_headers,
        json={"amount": 5}
    )

    assert response.status_code == 200
    assert response.json()["quantity"] == 6


def test_non_admin_cannot_restock(client):
    user_headers = register_and_login(
    client, "user@test.com", "userpass"
)

    sweet_id = create_sweet(client, user_headers, 1)

    response = client.post(
        f"/api/sweets/{sweet_id}/restock",
        headers=user_headers,
        json={"amount": 5}
    )

    assert response.status_code == 403
