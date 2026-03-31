from sqlmodel import SQLModel, Field
from typing import Optional

# USER 

class UserBase(SQLModel):
    name: str
    email: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

class LoginData(SQLModel):
    email: str
    password: str


#  FIRM 

class FirmBase(SQLModel):
    name: str
    email: str

class Firm(FirmBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    address: Optional[str] = None

class FirmCreate(FirmBase):
    address: Optional[str] = None

class FirmResponse(FirmBase):
    id: int
    address: Optional[str] = None