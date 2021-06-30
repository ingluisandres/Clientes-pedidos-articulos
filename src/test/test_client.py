from src.test.app import client

def test_create_client():
    response = client.post(
        "/clients/",
        json={
            "name": "Rodrigo", 
            "last_name": "Robinson", 
            "email": "ingluisandres3@gmail.com", 
            "phone_number":8116952021, 
            "address":"comanches 14", 
            "postal_code": 88240
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "ingluisandres3@gmail.com"
    assert data["phone_number"] == 8116952021
    assert "id" in data
    
    # user_id = data["id"]
    # response = client.get(f"/users/{user_id}")
    # assert response.status_code == 200, response.text
    # data = response.json()
    # assert data["email"] == "deadpool@example.com"
    # assert data["id"] == user_id




# def test_ping():
#     response = client.get("/clients/ping")
#     assert response.status_code == 200
#     assert response.json() == {"ping": "pong!"}

# def test_read_main():
#     response = client.get("/clients/?skip=0&limit=10")
#     assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}

# def test_create_item():
#     response = client.post("/clients",json=data,)
#     assert response.status_code == 200
#     assert data in response.json()