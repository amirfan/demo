from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_chat_completion() -> None:
    response = client.post(
        "/v1/chat/completions",
        json={
            "model": "mock-gpt",
            "messages": [
                {"role": "user", "content": "你好"},
            ],
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["object"] == "chat.completion"
    assert data["model"] == "mock-gpt"
    assert data["choices"][0]["message"]["role"] == "assistant"
    assert "已收到: 你好" in data["choices"][0]["message"]["content"]
