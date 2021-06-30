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