# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from app.routers import user as user_router
from app.routers import product as product_router

# Crea tablas (solo para pruebas iniciales, luego usaremos Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="POSGUIN API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(user_router.router)
app.include_router(product_router.router)

