from src.test.app import test


def test_create_item():
    response = test.post(
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
    response = test.get(f"/items/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Test title"

def test_update_item():
    response = test.put(
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

def test_delete_item():
    response = test.delete(f'/items/1')
    data = response.json()
    assert response.status_code == 200, response.text
    assert data == {'message': 'successfully deleted item with id: 1'}
    test_response = test.get(f'/items/1')
    test_data = test_response.json()
    assert test_data == {'detail': 'sorry this item does not exist'}