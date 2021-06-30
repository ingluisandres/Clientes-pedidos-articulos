from src.test.app import client


def test_create_item():
    response = client.post(
        "/items/",
        json={
            "title": "Test title",
            "description": "Test description",
            "price": 10000
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Test title"
    assert "id" in data

def test_get_item():
    response = client.get(f"/items/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Test title"

def test_update_item():
    response = client.put(
        '/items/1',
        json={
            "title": "Updated title",
            "description": "Updated description",
            "price": 20000
            },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['title'] == 'Updated title'