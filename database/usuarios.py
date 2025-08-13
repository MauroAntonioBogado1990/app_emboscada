# Clientes, admins, roles
from sqlalchemy import Column, Integer, String, Boolean
from db import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    
    es_admin = Column(Boolean, default=False)
    telefono = Column(String, nullable=True)
    whatsapp = Column(String, nullable=True)