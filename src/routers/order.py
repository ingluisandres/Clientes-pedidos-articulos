import sys
sys.path.append("..")

from fastapi import APIRouter, Depends
from typing import List
import sqlalchemy.orm as _orm

from src.services import order as _services
import src.database as _database
import src.schemas as _schemas


router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.post("/", response_model=_schemas.Order)
def create(order: _schemas.OrderCreate, db: _orm.Session=Depends(_database.get_db)):

    return _services.create_order(db=db, order=order)

@router.get('/', response_model=List[_schemas.Order])
def read_all(
            skip: int=0, 
            limit: int=10, 
            db: _orm.Session=Depends(_database.get_db)):
    orders = _services.get_orders(db=db, skip=skip, limit=limit)
    return orders

@router.get('/{order_id}', response_model=_schemas.Order)
def read_client(
            order_id: int, 
            db: _orm.Session=Depends(_database.get_db)):
    db_order = _services.get_order(db=db, order_id=order_id)
    if db_order is None:
        raise HTTPException(
            status_code=404, detail='sorry this order does not exist'
        )
    return db_order