import sys
sys.path.append("..") 

from fastapi import APIRouter, HTTPException, Depends
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services


router = APIRouter()

@router.post("/items/", response_model=_schemas.Item, tags=["items"])
def create(item: _schemas.ItemCreate, db: _orm.Session=Depends(_services.get_db)):
    db_item = _services.get_item_by_title(db=db, title=item.title)
    if db_item:
        raise HTTPException(status_code=400, detail="woops the title is in use")

    return _services.create_item(db=db, item=item)