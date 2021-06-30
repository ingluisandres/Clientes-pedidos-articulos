import sys
sys.path.append("..")

import sqlalchemy.orm as _orm

import src.schemas as _schemas
import src.models as _models


def get_item_by_title(db: _orm.Session, title:str):
    return db.query(_models.Item).filter(_models.Item.title==title).first()

def create_item(db: _orm.Session, item: _schemas.ItemCreate):
    db_item = _models.Item(title= item.title, description= item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db:_orm.Session, skip:int, limit:int):
    return db.query(_models.Item).offset(skip).limit(limit).all()

def get_item(db: _orm.Session, item_id:int):
    return db.query(_models.Item).filter(_models.Item.id == item_id).first()

def update_item(
        db: _orm.Session, 
        item:_schemas.ItemCreate, 
        item_id:int):
    db_item=get_item(db=db, item_id=item_id)

    db_item.title = item.title
    db_item.description = item.description
    db_item.price = item.price

    db.commit()
    db.refresh(db_item)
    return db_item