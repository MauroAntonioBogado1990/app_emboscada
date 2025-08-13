from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    es_admin: bool = False
    telefono: Optional[str] = None
    whatsapp: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    pass  # Si querés agregar validaciones específicas al crear

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True  # Permite convertir desde SQLAlchemy a Pydantic