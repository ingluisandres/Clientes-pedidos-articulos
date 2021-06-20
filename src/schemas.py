from typing import List
import pydantic as _pydantic
import datetime as _dt
from typing import List, Optional


# Client
class _ClientBase(_pydantic.BaseModel):
    name: str
    last_name: str
    email: str
    phone_number: Optional[int]
    address: Optional[str]
    postal_code: Optional[int]

class ClientCreate(_ClientBase):
    pass

class Client(_ClientBase):
    id: int
    # orders_client: List[Order] = []

    class Config:
        orm_mode = True


# Item
class _ItemBase(_pydantic.BaseModel):
    title: str
    description: str
    price: int

class ItemCreate(_ItemBase):
    pass

class Item(_ItemBase):
    id: int

    class Config:
        orm_mode = True


# Order
class _OrderBase(_pydantic.BaseModel):
    client_id: int
    items_id: int
    units: int

class OrderCreate(_OrderBase):
    pass

class Order(_OrderBase):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True