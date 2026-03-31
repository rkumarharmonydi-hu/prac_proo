from sqlmodel import SQLModel, Field
from typing import Optional

class UserBase(SQLModel):
    name: str
    email: str

class User(UserBase, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    password: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

class LoginData(SQLModel):
    email: str
    password: str