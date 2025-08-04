from app.database.db import Base, engine
from app.models.user import User
from app.models.role import Role

def create_tables():
    Base.metadata.create_all(bind=engine)
