import sys
sys.path.append("..")

import sqlalchemy.orm as _orm

import src.schemas as _schemas
import src.models as _models


def create_order(db: _orm.Session, order: _schemas.OrderCreate):
    db_order = _models.Order(client_id=order.client_id, items_id=order.items_id, units= order.units)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db:_orm.Session, skip:int, limit:int):
    return db.query(_models.Order).offset(skip).limit(limit).all()

def get_order(db: _orm.Session, order_id:int):
    return db.query(_models.Order).filter(_models.Order.id == order_id).first()

def update_order(
        db: _orm.Session, 
        order:_schemas.OrderCreate, 
        order_id:int):
    db_order=get_order(db=db, order_id=order_id)
    db_order.client_id = order.client_id
    db_order.items_id = order.items_id
    db_order.units = order.units
    db.commit()
    db.refresh(db_order)
    return db_order

def delete_order(db: _orm.Session, order_id:int):
    db.query(_models.Order).filter(_models.Order.id == order_id).delete()
    db.commit()