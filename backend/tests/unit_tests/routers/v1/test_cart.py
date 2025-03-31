from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_cart():
    response = client.get("e-com-store/v1/cart")
    assert response.status_code == 200

def test_cart_items_validation():
    response = client.put("e-com-store/v1/cart", json={
        "cartItems": [
            {
                "itemId": "123",
                "itemName": "Test Item",
                "quantity": 0,
                "amount": 0.0
            }
        ]
    })

    assert response.status_code == 422