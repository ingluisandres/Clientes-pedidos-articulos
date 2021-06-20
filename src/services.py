import sqlalchemy.orm as _orm

import database as _database
import models as _models
import schemas as _schemas

import datetime as _dt


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Client
def get_client_by_email(db: _orm.Session, email:str):
    return db.query(_models.Client).filter(_models.Client.email==email).first()

def create_client(db: _orm.Session, client: _schemas.ClientCreate):
    db_client = _models.Client(name= client.name, last_name= client.last_name, email=client.email, phone_number=client.phone_number, address=client.address, postal_code=client.postal_code)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


# Item
def get_item_by_title(db: _orm.Session, title:str):
    return db.query(_models.Item).filter(_models.Item.title==title).first()

def create_item(db: _orm.Session, item: _schemas.ItemCreate):
    db_item = _models.Item(title= item.title, description= item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# Order
def create_order(db: _orm.Session, order: _schemas.OrderCreate):
    db_order = _models.Order(client_id=order.client_id, items_id=order.items_id, units= order.units)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order