from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
Base = declarative_base()

# 👇 Importa tus modelos para que SQLAlchemy los registre
from app.models import user, role  # <- esta línea debe estar aquí


DATABASE_URL = "mysql+pymysql://root@localhost/hyperfocus_2"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 👇 Esta línea es la que crea todas las tablas si aún no existen
Base.metadata.create_all(bind=engine)

