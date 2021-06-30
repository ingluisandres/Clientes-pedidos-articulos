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