def auth_header(client, email="inventory@test.com"):
    client.post("/api/auth/register", json={
        "email": email,
        "password": "password"
    })

    token = client.post("/api/auth/login", json={
        "email": email,
        "password": "password"
    }).json()["access_token"]

    return {"Authorization": f"Bearer {token}"}


def create_sweet(client, headers, quantity: int):
    response = client.post(
        "/api/sweets",
        headers=headers,
        json={
            "name": "Ladoo",
            "category": "Indian",
            "price": 5.0,
            "quantity": quantity
        }
    )
    return response.json()["id"]


def test_purchase_sweet_decreases_quantity(client):
    headers = auth_header(client, "inventory1@test.com")

    sweet_id = create_sweet(client, headers, 2)

    response = client.post(
        f"/api/sweets/{sweet_id}/purchase",
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["quantity"] == 1


def test_purchase_fails_when_out_of_stock(client):
    headers = auth_header(client, "inventory2@test.com")

    sweet_id = create_sweet(client, headers, 0)

    response = client.post(
        f"/api/sweets/{sweet_id}/purchase",
        headers=headers
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Out of stock"
