import requests
import pytest
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def get_headers():
    return {"Content-Type": "application/json"}

def test_get_request(get_headers):
    response = requests.get(f"{BASE_URL}/posts/1", headers=get_headers)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and data["id"] == 1

def test_post_request(get_headers):
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", headers=get_headers, data=json.dumps(payload))
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

def test_put_request(get_headers):
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", headers=get_headers, data=json.dumps(payload))
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updated title"

def test_delete_request(get_headers):
    response = requests.delete(f"{BASE_URL}/posts/1", headers=get_headers)
    assert response.status_code == 200
