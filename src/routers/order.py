import sys
sys.path.append("..") 

from fastapi import APIRouter, Depends
from typing import List
from services import order as _services
import sqlalchemy.orm as _orm
import schemas as _schemas
import database as _database


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