from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. call /search or /wiki"}


def test_read():
    response = client.get("/phrase/Narendra Modi")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "narendra damodardas modi",
            "gujarati",
            "[ ˈnəɾendɾə dɑmodəɾˈdɑs ˈmodiː ]",
            "september",
            "indian politician",
            "prime minister",
            "india",
            "may",
        ]
    }
