from fastapi import APIRouter, Depends
from sqlmodel import Session
from db import get_session
from crud import create_firm_db
from models import FirmCreate, FirmResponse, Firm

router1 = APIRouter(prefix="/firm", tags=["Firm admin"])


@router1.post("/create", response_model=FirmResponse)
def create_firm(firm: FirmCreate, session: Session = Depends(get_session)):
    return create_firm_db(session, firm)


@router1.get("/{firm_id}", response_model=FirmResponse)
def get_firm(firm_id: int, session: Session = Depends(get_session)):
    firm = session.get(Firm, firm_id)

    if not firm:
        return {"error": "Firm not found"}

    return firm