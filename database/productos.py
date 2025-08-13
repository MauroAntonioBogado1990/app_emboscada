# Chipás, precios, categorías
from sqlalchemy import Column, Integer, String
from db import Base

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    precio = Column(Integer)