from src.test.app import test


def test_create_client():
    response = test.post(
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
    assert response.status_code == 201, response.text
    data = response.json()

    assert data["name"] == "Rodrigo"
    assert data["last_name"] == "Robinson"
    assert data["email"] == "ingluisandres3@gmail.com"
    assert data["phone_number"] == 8116952022
    assert data["address"] == "comanches 14"
    assert data["postal_code"] == 88240

    assert "id" in data


def test_get_client():
    response = test.get(f"/clients/1")
    assert response.status_code == 200, response.text
    data = response.json()

    assert data["name"] == "Rodrigo"
    assert data["last_name"] == "Robinson"
    assert data["email"] == "ingluisandres3@gmail.com"
    assert data["phone_number"] == 8116952022
    assert data["address"] == "comanches 14"
    assert data["postal_code"] == 88240


def test_update_client():
    response = test.put(
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

    assert data["name"] == "Luis"
    assert data["last_name"] == "Contreras"
    assert data["email"] == "andy031197@gmail.com"
    assert data["phone_number"] == 8116952021
    assert data["address"] == "Comanches 15"
    assert data["postal_code"] == 88240


def test_delete_client():
    response = test.delete(f"/clients/1")
    data = response.json()
    assert response.status_code == 200, response.text
    assert data == {'message': 'successfully deleted client with id: 1'}
    
    test_response = test.get(f"/clients/1")
    test_data = test_response.json()
    assert test_data == {'detail': 'sorry this client does not exist'}