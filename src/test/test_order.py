from src.test.app import test


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


def test_get_order():
    response = test.get(f"/orders/1")
    assert response.status_code == 200, response.text
    data = response.json()

    assert data["client_id"] == 1
    assert data["items_id"] == 1
    assert data["units"] == 10


def test_update_client():
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


def test_delete_client():
    response = test.delete(f'/orders/1')
    data = response.json()
    assert response.status_code == 200, response.text
    assert data == {'message': 'successfully deleted order with id: 1'}
    test_response = test.get(f'/orders/1')
    test_data = test_response.json()
    assert test_data == {'detail': 'sorry this order does not exist'}