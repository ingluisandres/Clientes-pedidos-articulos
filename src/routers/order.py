import sys
sys.path.append("..") 

from fastapi import APIRouter, Depends
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