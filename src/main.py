from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas 
from routers import client

app = _fastapi.FastAPI()

_services.create_database()

app.include_router(client.router)


# Client
# @app.post("/clients/", response_model=_schemas.Client, tags=["clients"])
# def create_client(client: _schemas.ClientCreate, db: _orm.Session=_fastapi.Depends(_services.get_db)):
#     db_client = _services.get_client_by_email(db=db, email=client.email)
#     if db_client:
#         raise _fastapi.HTTPException(status_code=400, detail="woops the email is in use")

#     return _services.create_client(db=db, client=client)


# Item
@app.post("/items/", response_model=_schemas.Item, tags=["items"])
def create_item(item: _schemas.ItemCreate, db: _orm.Session=_fastapi.Depends(_services.get_db)):
    db_item = _services.get_item_by_title(db=db, title=item.title)
    if db_item:
        raise _fastapi.HTTPException(status_code=400, detail="woops the title is in use")

    return _services.create_item(db=db, item=item)


# Order
@app.post("/orders/", response_model=_schemas.Order, tags=["orders"])
def create_order(order: _schemas.OrderCreate, db: _orm.Session=_fastapi.Depends(_services.get_db)):

    return _services.create_order(db=db, order=order)