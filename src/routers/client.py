import sys
sys.path.append("..")

from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
import sqlalchemy.orm as _orm

from src.services import client as _services
import src.database as _database
import src.schemas as _schemas


router = APIRouter(
    prefix="/clients",
    tags=["clients"]
)


@router.post("/", response_model=_schemas.Client)
def create(client: _schemas.ClientCreate, db: _orm.Session=Depends(_database.get_db)):
    db_client = _services.get_client_by_email(db=db, email=client.email)
    if db_client:
        raise HTTPException(status_code=400, detail="woops the email is in use")

    db_client_phone = _services.get_client_by_phone(db=db, phone_number=client.phone_number)
    if db_client_phone:
        raise HTTPException(status_code=400, detail="woops the phone number is in use")

    return _services.create_client(db=db, client=client)

@router.get("/", response_model=List[_schemas.Client])
def read_all(
            skip: int=0, 
            limit: int=10, 
            db: _orm.Session=Depends(_database.get_db)):
    """Without test"""
    users = _services.get_users(db=db, skip=skip, limit=limit)
    return users