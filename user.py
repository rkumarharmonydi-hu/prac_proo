from fastapi import APIRouter, Depends
from sqlmodel import Session

from db import get_session
from crud import create_user
from models import UserCreate, UserResponse

router = APIRouter(prefix="/booking", tags=["User"])


@router.get("/first")
async def your_name():
    return {"Name": "Hii i am user"}


@router.post("/users", response_model=UserResponse)
async def create_new_user(
    user: UserCreate,
    session: Session = Depends(get_session)
):
    return create_user(session, user)