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
    db_client = _models.Client(email=client.email)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client