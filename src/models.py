# Aqui estaran como luciran las tablas
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import database as _database
import datetime as _dt


class Client(_database.Base):
    # posts = _orm.relationship("Post", back_populates="owner")
    # nombre de la columna = orm.relationship("tabla externa", "nombre de la columna de esa tabla")

    __tablename__ = "clients"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, unique=True, index=True)
    last_name = _sql.Column(_sql.String, unique=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    phone_number = _sql.Column(_sql.Integer, index=True)
    address = _sql.Column(_sql.String, unique=True, index=True)
    postal_code = _sql.Column(_sql.Integer, index=True)

    orders_client = _orm.relationship("Order", back_populates="owner")


class Item(_database.Base):
    __tablename__ = "items"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title= _sql.Column(_sql.String, index=True)
    description = _sql.Column(_sql.String, index=True)
    price = _sql.Column(_sql.Integer, index=True)

    orders_item = _orm.relationship("Order", back_populates="items")


class Order(_database.Base):
    __tablename__ = "orders"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    client_id = _sql.Column(_sql.Integer, _sql.ForeignKey("clients.id"))
    items_id = _sql.Column(_sql.Integer, _sql.ForeignKey("items.id"))
    units = _sql.Column(_sql.String, index= True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    owner = _orm.relationship("Client",back_populates="orders_client")
    items = _orm.relationship("Item", back_populates="orders_item")