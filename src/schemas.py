from typing import List
import pydantic as _pydantic
import datetime as _dt


# Client
class _ClientBase(_pydantic.BaseModel):
    name: str
    last_name: str
    email: str
    phone_number: str
    address: str
    postal_code: str

class ClientCreate(_ClientBase):
    pass

class Client(_ClientBase):
    id: int
    # orders: List[Order] = []

    class Config:
        orm_mode = True


# Item
class _ItemBase(_pydantic.BaseModel):
    title: str
    description: str
    price: str

class ItemCreate(_ItemBase):
    pass

class Item(_ItemBase):
    id: int

    class Config:
        orm_mode = True


# Order
class _OrderBase(_pydantic.BaseModel):
    units: str

class OrderCreate(_OrderBase):
    pass

class Order(_OrderBase):
    id: int
    client_id: int
    items_id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True