from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
