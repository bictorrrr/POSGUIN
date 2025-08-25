import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://posguin:posguin123@localhost:5433/posguin"

settings = Settings()
