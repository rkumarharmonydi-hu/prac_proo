from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from db import get_session
from crud import UserCreate, get_user_by_email, create_user,User 
from models import LoginData 
from auth import verify_password, create_access_token,hash_password
from dependencies import require_firm_admin

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

@router.post("/create-user-under-firm")
def create_user_under_firm(
    user_data: UserCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(require_firm_admin)
):
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hash_password(user_data.password),
        role="user",
        firm_id=current_user.firm_id or current_user.id
    )
    session.add(new_user)
    session.commit()
    return new_user