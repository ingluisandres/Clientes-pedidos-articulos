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