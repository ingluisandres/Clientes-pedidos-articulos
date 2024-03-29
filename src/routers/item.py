import sys
sys.path.append("..")

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import sqlalchemy.orm as _orm

from src.services import item as _services
import src.database as _database
import src.schemas as _schemas


router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.post("/", response_model=_schemas.Item, status_code=status.HTTP_201_CREATED)
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


@router.get('/{item_id}', response_model=_schemas.Item)
def read_item(
            item_id: int, 
            db: _orm.Session=Depends(_database.get_db)):
    db_item = _services.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(
            status_code=404, detail='sorry this item does not exist'
        )
    return db_item


@router.put('/{item_id}', response_model=_schemas.Item)
def update_item(
            item_id: int, 
            item: _schemas.ItemCreate,
            db: _orm.Session = Depends(_database.get_db)):
    db_item = _services.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(
            status_code=404, detail='sorry this item does not exist'
        )
    return _services.update_item(db=db, item=item, item_id=item_id)


@router.delete('/{item_id}')
def delete_item(
            item_id: int, 
            db: _orm.Session = Depends(_database.get_db)):
    db_item = _services.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(
            status_code=404, detail='sorry this item does not exist'
        )
    _services.delete_item(db=db, item_id=item_id)
    return{'message':f'successfully deleted item with id: {item_id}'}