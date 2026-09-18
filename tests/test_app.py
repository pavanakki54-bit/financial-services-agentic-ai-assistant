from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat():
    response = client.post(
        "/chat",
        json={
            "session_id": "demo-001",
            "message": "How long do I have to dispute a transaction?",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["session_id"] == "demo-001"
    assert "dispute_policy.md" in data["sources"]
    assert "60 days" in data["answer"]


def test_empty_message_rejected():
    response = client.post(
        "/chat",
        json={
            "session_id": "demo-001",
            "message": "",
        },
    )

    assert response.status_code == 422
