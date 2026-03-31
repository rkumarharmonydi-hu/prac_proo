from sqlmodel import Session
from models import User, UserCreate, Firm, FirmCreate

# USER 
def create_user(session: Session, user_data: UserCreate):
    user = User(**user_data.dict())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# FIRM
def create_firm_db(session: Session, firm_data: FirmCreate):
    firm = Firm(**firm_data.dict())
    session.add(firm)
    session.commit()
    session.refresh(firm)
    return firm