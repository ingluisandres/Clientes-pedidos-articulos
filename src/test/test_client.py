from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database import Base
from src.main import app
from src.routers.client import router
from src.database import get_db

#SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///./src/test/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)






def test_create_user():
    response = client.post(
        "/clients/",
        json={
            "name": "Rodrigo", 
            "last_name": "Robinson", 
            "email": "andy031197@gmail.com", 
            "phone_number":12345675, 
            "address":"comanches 14", 
            "postal_code": 88240
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "andy031197@gmail.com"
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