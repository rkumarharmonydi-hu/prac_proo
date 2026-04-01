from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from db import get_session
from crud import get_pending_firm, appove_firm, reject_firm
from models import FirmResponse, User
from dependencies import get_current_user

router_admin = APIRouter(prefix="/admin", tags=["Admin"])


# Admin check function
def require_admin(user: User = Depends(get_current_user)):
    if user.role != ["admin"]:
        raise HTTPException(status_code=403, detail="Admin  access required")
    elif user.role != ["Firm_admin"]:
        raise HTTPException(status_code=403, detail="Firm Admin access required")
    return user 

# Get all pending firms
@router_admin.get("/firms/pending", response_model=list[FirmResponse])
def pending_firms(
    session: Session = Depends(get_session),
    admin: User = Depends(require_admin)
):
    return get_pending_firm(session)


# Approve firm
@router_admin.put("/firms/{firm_id}/approve", response_model=FirmResponse)
def approve(
    firm_id: int,
    session: Session = Depends(get_session),
    admin: User = Depends(require_admin)
):
    firm = appove_firm(session, firm_id)
    if not firm:
        raise HTTPException(status_code=404, detail="Firm not found")
    return firm


# Reject firm
@router_admin.put("/firms/{firm_id}/reject", response_model=FirmResponse)
def reject(
    firm_id: int,
    session: Session = Depends(get_session),
    admin: User = Depends(require_admin)
):
    firm = reject_firm(session, firm_id)
    if not firm:
        raise HTTPException(status_code=404, detail="Firm not found")
    return firm