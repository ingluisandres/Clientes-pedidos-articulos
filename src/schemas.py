from typing import List, Optional
from fastapi import Body, Query
import pydantic as _pydantic
import datetime as _dt


# Client
class _ClientBase(_pydantic.BaseModel):
    name: str = Query(..., min_length=2, max_length=20)
    last_name: str = Query(..., min_length=2, max_length=20)
    email: str = Query(..., min_length=2, max_length=30)
    phone_number: int = Query(..., gt=1000000000)
    address: Optional[str] = Query(None, min_length=3, max_length=50)
    postal_code: Optional[int] = Query(None, gt=10000)

class ClientCreate(_ClientBase):
    pass

class Client(_ClientBase):
    id: int
    # orders_client: List[Order] = []

    class Config:
        orm_mode = True


# Item
class _ItemBase(_pydantic.BaseModel):
    title: str = Query(..., min_length=5, max_length=20)
    description: str = Query(..., min_length=10, max_length=50)
    price: int

class ItemCreate(_ItemBase):
    pass

class Item(_ItemBase):
    id: int

    class Config:
        orm_mode = True


# Order
class _OrderBase(_pydantic.BaseModel):
    client_id: int = Query(..., gt=0)
    items_id: int = Query(..., gt=0)
    units: int = Query(..., gt=0)

class OrderCreate(_OrderBase):
    pass

class Order(_OrderBase):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True