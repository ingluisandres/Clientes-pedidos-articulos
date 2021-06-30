import sys
sys.path.append("..")

from fastapi import APIRouter, HTTPException, Depends
from typing import List
import sqlalchemy.orm as _orm

from src.services import item as _services
import src.database as _database
import src.schemas as _schemas


router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.post("/", response_model=_schemas.Item)
def create(item: _schemas.ItemCreate, db: _orm.Session=Depends(_database.get_db)):
    db_item = _services.get_item_by_title(db=db, title=item.title)
    if db_item:
        raise HTTPException(status_code=400, detail="woops the title is in use")

    return _services.create_item(db=db, item=item)

@router.get('/', response_model=List[_schemas.Item])
def read_all(
            skip: int=0, 
            limit: int=10, 
            db: _orm.Session=Depends(_database.get_db)):
    return services.get_items(db=db, skip=skip, limit=limit)