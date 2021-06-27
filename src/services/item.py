import sqlalchemy.orm as _orm
import schemas as _schemas
import models as _models


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