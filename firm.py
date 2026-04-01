from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from db import get_session
from crud import create_firm_db
from models import FirmCreate, FirmResponse, Firm, User
from dependencies import get_current_user

router = APIRouter(prefix="/firm", tags=["Firm admin"])

# Create firm
@router.post("/create", response_model=FirmResponse)
def create_firm(
    firm: FirmCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Optional restriction (only user or firm_admin)
    if current_user.role not in ["user", "firm_admin", "admin"]:
        raise HTTPException(status_code=403, detail="Not allowed")

    return create_firm_db(session, firm, current_user.id)


# Get firm (ROLE BASED ACCESS)
@router.get("/{firm_id}", response_model=FirmResponse)
def get_firm(
    firm_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    firm = session.get(Firm, firm_id)
    if not firm:
        raise HTTPException(status_code=404, detail="Firm not found")
    if current_user.role == "admin":
        return firm
    # Firm Admin / User → only own firm
    if firm.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return firm