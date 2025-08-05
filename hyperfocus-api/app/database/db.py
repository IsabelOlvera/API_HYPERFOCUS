# app/database/db.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Base para los modelos
Base = declarative_base()

# 👇 Importa los modelos para que SQLAlchemy los registre
from app.models import user, role  # mantener aquí

# Lee la URL desde variable de entorno (ideal para Render)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root@localhost/hyperfocus_2"  # fallback local
)

# Crea el engine
engine = create_engine(DATABASE_URL)

# Crea la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea las tablas (si aún no existen)
Base.metadata.create_all(bind=engine)

# Dependency para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
