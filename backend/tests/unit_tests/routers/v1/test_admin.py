from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_stats():
    response = client.get("e-com-store/v1/admin/stats")
    assert response.status_code == 200
    response_data = response.json()
    assert "totalItemCount" in response_data
    assert "totalPurchaseAmount" in response_data
    assert "totalDiscount" in response_data
    assert "discountCodes" in response_data


def test_get_discount_code_for_ineligible_order():
    response = client.get("e-com-store/v1/admin/discount")
    assert response.status_code == 400
    assert response.json() == {"detail": "Order is not eligible for a discount"}


def test_get_discount_code_for_eligible_order(monkeypatch):
    monkeypatch.setenv("ORDERS_BETWEEN_DISCOUNT", "1")
    response = client.get("e-com-store/v1/admin/discount")
    assert response.status_code == 200
    assert "discountCode" in response.json()