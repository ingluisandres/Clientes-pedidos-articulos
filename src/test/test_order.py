from src.test.conftest import test


def test_create_order():
    response = test.post(
        "/orders/",
        json={
            "client_id": 1,
            "items_id": 1,
            "units": 10
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()

    assert data["client_id"] == 1
    assert data["items_id"] == 1
    assert data["units"] == 10

    assert "id" in data

def test_create_order_invalid_json():
    response = test.post(
        '/orders/',
        json={ 
            "client_id": 1,
            "units": 10
        }
    )
    assert response.status_code == 422


def test_get_order():
    response = test.get(f"/orders/1")
    assert response.status_code == 200, response.text
    data = response.json()

    assert data["client_id"] == 1
    assert data["items_id"] == 1
    assert data["units"] == 10

def test_get_order_incorrect_id():
    response = test.get('/orders/999')
    assert response.status_code == 404
    assert response.json()['detail'] == 'sorry this order does not exist'


def test_update_order():
    response = test.put(
        '/orders/1',
        json={
            "client_id": 5,
            "items_id": 3,
            "units": 2
            },
    )
    assert response.status_code == 200, response.text
    data = response.json()

    assert data['client_id'] == 5
    assert data['items_id'] == 3
    assert data["units"] == 2

def test_update_order_incorrect_id():
    response = test.put(
        '/orders/999',
        json={
            "client_id": 5,
            "items_id": 3,
            "units": 2 
        }
    )
    assert response.status_code == 404
    assert response.json()['detail'] == 'sorry this order does not exist'

def test_delete_order():
    response = test.delete(f'/orders/1')
    data = response.json()
    assert response.status_code == 200, response.text
    assert data == {'message': 'successfully deleted order with id: 1'}
    test_response = test.get(f'/orders/1')
    test_data = test_response.json()
    assert test_data == {'detail': 'sorry this order does not exist'}

def test_delete_order_incorrect_id():
    response = test.delete('/orders/999')
    assert response.status_code == 404
    assert response.json()['detail'] == 'sorry this order does not exist'