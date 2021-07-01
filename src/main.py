from datetime import date
from datetime import datetime
import sys
sys.path.append("..")

import fastapi as _fastapi

from src.routers import client, item, order
import src.database as _database


app = _fastapi.FastAPI()


_database.create_database()


# @app.on_event("startup")
# async def startup():
#     await _database.connect()

    # todays_date = date.today()
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # with open("log.txt", mode="a") as log:
    #     log.write(f"{todays_date} Application startup: {current_time}\n")


# @app.on_event("shutdown")
# async def shutdown():
#     await _database.disconnect()

    # todays_date = date.today()
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # with open("log.txt", mode="a") as log:
    #     log.write(f"{todays_date} Application shutdown: {current_time}\n\n")


app.include_router(client.router)
app.include_router(item.router)
app.include_router(order.router)