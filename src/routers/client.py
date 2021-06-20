import sys
sys.path.append("..") 

from fastapi import APIRouter, HTTPException, Depends
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services


router = APIRouter()

@router.post("/clients/", response_model=_schemas.Client, tags=["clients"])
def create(client: _schemas.ClientCreate, db: _orm.Session=Depends(_services.get_db)):
    db_client = _services.get_client_by_email(db=db, email=client.email)
    if db_client:
        raise HTTPException(status_code=400, detail="woops the email is in use")

    return _services.create_client(db=db, client=client)