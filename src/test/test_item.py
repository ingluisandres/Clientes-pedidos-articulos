from src.test.conftest import test


def test_create_item():
    response = test.post(
        "/items/",
        json={
            "title": "Test title",
            "description": "Test description",
            "price": 10000
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()

    assert data["title"] == "Test title"
    assert data["description"] == "Test description"
    assert data["price"] == 10000

    assert "id" in data

def test_create_item_invalid_json():
    response = test.post(
        '/items/',
        json={ 
            "title": "Test title",
            "description": "Test description"
        }
    )
    assert response.status_code == 422


def test_get_item():
    response = test.get(f"/items/1")
    assert response.status_code == 200, response.text
    data = response.json()

    assert data["title"] == "Test title"
    assert data["description"] == "Test description"
    assert data["price"] == 10000

def test_get_item_incorrect_id():
    response = test.get('/items/999')
    assert response.status_code == 404
    assert response.json()['detail'] == 'sorry this item does not exist'


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
    assert data["description"] == "Updated description"
    assert data["price"] == 20000

def test_update_item_incorrect_id():
    response = test.put(
        '/items/999',
        json={
            "title": "Updated title",
            "description": "Updated description",
            "price": 20000
        }
    )
    assert response.status_code == 404
    assert response.json()['detail'] == 'sorry this item does not exist'

def test_delete_item():
    response = test.delete(f'/items/1')
    data = response.json()
    assert response.status_code == 200, response.text
    assert data == {'message': 'successfully deleted item with id: 1'}
    test_response = test.get(f'/items/1')
    test_data = test_response.json()
    assert test_data == {'detail': 'sorry this item does not exist'}

def test_delete_item_incorrect_id():
    response = test.delete('/items/999')
    assert response.status_code == 404
    assert response.json()['detail'] == 'sorry this item does not exist'