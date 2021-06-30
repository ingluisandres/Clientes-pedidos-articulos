from src.test.app import client


def test_create_client():
    response = client.post(
        "/clients/",
        json={
            "name": "Rodrigo", 
            "last_name": "Robinson", 
            "email": "ingluisandres3@gmail.com", 
            "phone_number":8116952022, 
            "address":"comanches 14", 
            "postal_code": 88240
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "ingluisandres3@gmail.com"
    assert data["phone_number"] == 8116952022
    assert "id" in data

def test_get_client():
    response = client.get(f"/clients/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "ingluisandres3@gmail.com"
    assert data["phone_number"] == 8116952022

def test_update_client():
    response = client.put(
        "/clients/1",
        json={
            "name": "Luis", 
            "last_name": "Contreras", 
            "email": "andy031197@gmail.com", 
            "phone_number":8116952021, 
            "address":"Comanches 15", 
            "postal_code": 88240
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "andy031197@gmail.com"
    assert data["phone_number"] == 8116952021