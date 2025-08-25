from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configura la URL de la BD
DATABASE_URL = "postgresql://posguin:posguin123@localhost:5433/posguin"

# Crea el engine
engine = create_engine(DATABASE_URL, echo=True)

# Crea la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependency para usar en endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
