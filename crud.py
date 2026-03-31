from sqlmodel import Session
from models import User, UserCreate

def create_user(session: Session, user_data: UserCreate):
    user = User(**user_data.dict())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user