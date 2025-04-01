import re
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_empty_cart():
    response = client.get("e-com-store/v1/cart")
    response_data = response.json()
    assert response_data["cartItems"] == []
    assert response.status_code == 200

def test_cart_items_validation():
    response = client.put("e-com-store/v1/cart", json={
        "cartItems": [
            {
                "itemId": "123",
                "itemName": "Test Item",
                "quantity": 0,
                "price": 0.0
            }
        ]
    })

    assert response.status_code == 422


def test_cart():
    payload = {"cartItems": [
            {
                "itemId": "123",
                "itemName": "Test Item",
                "quantity": 10,
                "price": 10.0
            }
        ]
    }
    response = client.put("e-com-store/v1/cart", json=payload)

    assert response.status_code == 200

    response = client.get("e-com-store/v1/cart")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data == payload


def test_delete_cart():
    payload = {"cartItems": [
            {
                "itemId": "123",
                "itemName": "Test Item",
                "quantity": 10,
                "price": 10.0
            }
        ]
    }
    response = client.put("e-com-store/v1/cart", json=payload)

    assert response.status_code == 200

    response = client.get("e-com-store/v1/cart")
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["cartItems"]) != 0

    response = client.delete("e-com-store/v1/cart")
    assert response.status_code == 200