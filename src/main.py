import sys
sys.path.append("..")

from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

from src.routers import client, item, order
import src.database as _database


app = _fastapi.FastAPI()


_database.create_database()


app.include_router(client.router)
app.include_router(item.router)
app.include_router(order.router)