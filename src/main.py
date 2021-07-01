import sys
sys.path.append("..")

import fastapi as _fastapi

from src.routers import client, item, order
import src.database as _database


app = _fastapi.FastAPI()


_database.create_database()


app.include_router(client.router)
app.include_router(item.router)
app.include_router(order.router)


@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}