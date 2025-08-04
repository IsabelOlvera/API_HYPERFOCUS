from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.models.user import User
from app.schemas.user_schema import UserRegister, UserLogin
import bcrypt
from app.auth.auth_handler import create_access_token

router = APIRouter(prefix="/api", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/register")
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")

    new_user = User(
        name=user.name,
        apellido=user.apellido,
        email=user.email,
        password=user.password,
        rol_id=user.rol_id,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Usuario registrado correctamente", "user_id": new_user.id}


@router.post("/check-email")
def check_email(payload: dict, db: Session = Depends(get_db)):
    email = payload.get("email")
    if not email:
        raise HTTPException(status_code=400, detail="Email es requerido")
    user = db.query(User).filter(User.email == email).first()
    return {"exists": bool(user)}

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.email == data.email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if not bcrypt.checkpw(data.password.encode('utf-8'), usuario.password.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    token = create_access_token({"sub": usuario.email, "id": usuario.id})
    return {"access_token": token, "token_type": "bearer", "usuario_id": usuario.id}