from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.models.user import User

router = APIRouter(prefix="/api/usuarios", tags=["Usuarios"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}")
def obtener_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {
        "id": usuario.id,
        "nombre": usuario.name,
        "apellido": usuario.apellido,
        "email": usuario.email,
        "foto_perfil": usuario.foto_perfil,
        "edad": usuario.edad,
        "rol_id": usuario.rol_id,
        "estatus": usuario.estatus
    }
