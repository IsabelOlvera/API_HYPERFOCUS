from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth_routes

app = FastAPI()

# CORS: permite que React Native consuma tu API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Este prefix es CLAVE para que funcione /api/register y /api/check-email
app.include_router(auth_routes.router, prefix="/api", tags=["Auth"])
