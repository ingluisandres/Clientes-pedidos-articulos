from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas, database as _database
from routers import client, item, order

app = _fastapi.FastAPI()

_database.create_database()

app.include_router(client.router)
app.include_router(item.router)
app.include_router(order.router)