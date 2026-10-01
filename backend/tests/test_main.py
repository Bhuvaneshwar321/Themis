import os
import sys

from fastapi.testclient import TestClient

from app.main import app

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "backend"}
