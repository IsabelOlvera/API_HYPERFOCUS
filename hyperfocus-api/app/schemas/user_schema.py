from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    name: str
    apellido: str
    email: EmailStr
    password: str
    edad: int | None = None
    foto_perfil: str | None = None
    rol_id: int

class UserLogin(BaseModel):
    email: EmailStr
    password: str
