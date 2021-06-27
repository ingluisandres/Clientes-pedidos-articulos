import sys
sys.path.append("..") 

from fastapi import APIRouter, Depends
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services


router = APIRouter()

@router.post("/orders/", response_model=_schemas.Order, tags=["orders"])
def create(order: _schemas.OrderCreate, db: _orm.Session=Depends(_services.get_db)):

    return _services.create_order(db=db, order=order)