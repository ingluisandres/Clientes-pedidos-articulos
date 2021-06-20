from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas 


app = _fastapi.FastAPI()

_services.create_database()


# Root
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Client
@app.post("/clients/", response_model=_schemas.Client)
def create_client(client: _schemas.ClientCreate, db: _orm.Session=_fastapi.Depends(_services.get_db)):
    db_client = _services.get_client_by_email(db=db, email=client.email)
    if db_client:
        raise _fastapi.HTTPException(status_code=400, detail="woops the email is in use")

    return _services.create_client(db=db, client=client)


# Item
@app.post("/items/", response_model=_schemas.Client)
def create_item(client: _schemas.ClientCreate, db: _orm.Session=_fastapi.Depends(_services.get_db)):
    return _services.create_client(db=db, client=client)


# Order