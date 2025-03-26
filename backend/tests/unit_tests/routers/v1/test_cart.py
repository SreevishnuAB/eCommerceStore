from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_cart():
    response = client.get("e-com-store/v1/cart")
    assert response.status_code == 200