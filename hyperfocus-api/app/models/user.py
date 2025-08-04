from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    edad = Column(Integer, nullable=True)
    foto_perfil = Column(String(255), nullable=True)
    rol_id = Column(Integer, ForeignKey("roles.id"))
    estatus = Column(Boolean, default=True)
