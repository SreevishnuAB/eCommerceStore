from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_checkout():
    response = client.get("e-com-store/v1/checkout")
    assert response.status_code == 200