from sqlmodel import SQLModel, Field
from typing import Optional

# USER
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    password: str
    role: str = "user"
    firm_id:Optional[int]=Field(default=None,foreign_key="firm.id")   

class UserCreate(SQLModel):
    name: str
    email: str
    password: str

class UserResponse(SQLModel):
    id: int
    name: str
    email: str
    role: str

class LoginData(SQLModel):
    email: str
    password: str

# FIRM
class FirmBase(SQLModel):
    name: str
    email: str

class Firm(FirmBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    address: Optional[str] = None
    status: str = "pending"
    owner_id: int = Field(foreign_key="user.id")

class FirmCreate(FirmBase):
    address: Optional[str] = None

class FirmResponse(FirmBase):
    id: int
    address: Optional[str] = None
    status: str