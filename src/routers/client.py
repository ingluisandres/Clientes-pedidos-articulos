import sys
sys.path.append("..") 

from fastapi import APIRouter, HTTPException, Depends
from typing import List
from services import client as _services
import sqlalchemy.orm as _orm
import schemas as _schemas
import database as _database


router = APIRouter(
    prefix="/clients",
    tags=["clients"]
)


@router.post("/", response_model=_schemas.Client)
def create(client: _schemas.ClientCreate, db: _orm.Session=Depends(_database.get_db)):
    db_client = _services.get_client_by_email(db=db, email=client.email)
    if db_client:
        raise HTTPException(status_code=400, detail="woops the email is in use")

    return _services.create_client(db=db, client=client)

@router.get("/", response_model=List[_schemas.Client])
def read_all(
            skip: int=0, 
            limit: int=10, 
            db: _orm.Session=Depends(_database.get_db)):
    users = _services.get_users(db=db, skip=skip, limit=limit)
    return users