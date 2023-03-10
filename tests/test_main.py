from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_camera():
    test_uuid = "cfbc7f43-9be8-4052-9919-d52996fcbfd8"
    response = client.post("/api/v1/camera", data={"uuid": test_uuid})
    assert response.status_code == 200
    assert response.json()["uuid"] == test_uuid
    assert "id" in response.json()
