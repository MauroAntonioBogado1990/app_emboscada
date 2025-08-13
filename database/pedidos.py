# Pedidos, estados, fechas
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from db import Base
from datetime import datetime

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    fecha = Column(DateTime, default=datetime.utcnow)