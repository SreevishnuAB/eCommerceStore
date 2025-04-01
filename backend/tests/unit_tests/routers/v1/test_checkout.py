from src.handlers.stats_handler import ENV_ORDERS_BETWEEN_DISCOUNT
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_checkout_empty_cart():
    response = client.get("e-com-store/v1/checkout")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cart is empty"}

def test_checkout():
    payload = {
        "cartItems": [
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

    response = client.get("e-com-store/v1/checkout")
    assert response.status_code == 200
    assert response.json() == {"amountPayable": 100.0}

def test_checkout_with_invalid_discount_code():
    payload = {
        "cartItems": [
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

    # Assuming the discount code is valid and the discount amount is 10.0
    response = client.get("e-com-store/v1/checkout?discount-code=DISCOUNT10")
    assert response.status_code == 400

def test_checkout_with_discount(monkeypatch):
    monkeypatch.setenv(ENV_ORDERS_BETWEEN_DISCOUNT, "1")
    payload = {
        "cartItems": [
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

    response = client.get("e-com-store/v1/admin/discount")
    assert response.status_code == 200
    discount_code = response.json()["discountCode"]

    response = client.get(f"e-com-store/v1/checkout?discount-code={discount_code}")
    assert response.status_code == 200
    assert response.json() == {"amountPayable": 90.0}