import sys
sys.path.append("..")

import sqlalchemy.orm as _orm

import src.schemas as _schemas
import src.models as _models


def get_client_by_email(db: _orm.Session, email:str):
    return db.query(_models.Client).filter(_models.Client.email==email).first()

def get_client_by_phone(db: _orm.Session, phone_number:str):
    return db.query(_models.Client).filter(_models.Client.phone_number==phone_number).first()

def create_client(db: _orm.Session, client: _schemas.ClientCreate):
    db_client = _models.Client(name= client.name, last_name= client.last_name, 
            email=client.email, phone_number=client.phone_number, 
            address=client.address, postal_code=client.postal_code)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db:_orm.Session, skip:int, limit:int):
    return db.query(_models.Client).offset(skip).limit(limit).all()

def get_client(db: _orm.Session, client_id:int):
    return db.query(_models.Client).filter(_models.Client.id == client_id).first()