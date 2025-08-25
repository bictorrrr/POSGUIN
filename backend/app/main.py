# backend/app/main.py
from fastapi import FastAPI
from database import engine, Base
from app.routers import user

# Crea tablas (solo para pruebas iniciales, luego usaremos Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar routers
app.include_router(user.router)

