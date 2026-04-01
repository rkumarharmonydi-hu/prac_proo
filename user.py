from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from db import get_session
from crud import UserCreate, get_user_by_email, create_user
from models import LoginData 
from auth import verify_password, create_access_token,hash_password

router = APIRouter(prefix="/booking", tags=["User"])

@router.get("/first")
async def your_name():
    return {"Name": "Hii i am user"}

# Create User API
@router.post("/users")
async def create_new_user(
    user: UserCreate,
    session: Session = Depends(get_session)
):
    new_user = create_user(session, user)
    return new_user

#login api 
@router.post("/login")
def login(data: LoginData, session: Session = Depends(get_session)):
    user = get_user_by_email(session, data.email)
    
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({
        "sub": str(user.id),
        "type": "access"
    })
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }