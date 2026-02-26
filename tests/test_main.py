from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from Jenkins CI/CD!"}

def test_add():
    response = client.get("/add/5/7")
    assert response.status_code == 200
    assert response.json() == {"result": 12}