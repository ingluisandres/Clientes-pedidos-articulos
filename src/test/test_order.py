from src.test.app import client


def test_create_order():
    response = client.post(
        "/orders/",
        json={
            "client_id": 1,
            "items_id": 1,
            "units": 10
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data

def test_get_order():
    response = client.get(f"/orders/1")
    assert response.status_code == 200, response.text
    data = response.json()

def test_update_client():
    response = client.put(
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