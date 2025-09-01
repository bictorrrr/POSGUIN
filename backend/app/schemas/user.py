# app/schemas/user.py (Pydantic v2)
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str

class UserRead(BaseModel):
    id: int
    username: str
    email: str

    model_config = {"from_attributes": True}
