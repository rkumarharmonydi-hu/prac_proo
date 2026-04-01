from sqlmodel import Session,select 
from models import User, UserCreate, Firm, FirmCreate
from auth import hash_password

# USER 
def create_user(session, user_data):
    user = User(
        name=user_data.name,
        email=user_data.email,
        password=hash_password(user_data.password)  
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

#get user by email
def get_user_by_email(session:Session,email:str):
    statement=select(User).where(User.email==email)
    return session.exec(statement).first()


# FIRM
def create_firm_db(session: Session, firm_data: FirmCreate,user_id:int):
    firm = Firm(**firm_data.dict(),owner_id=user_id)
    session.add(firm)
    session.commit()
    session.refresh(firm)
    return firm 

#pendig firm (admin)
def get_pending_firm(session:Session):
    statement=select(Firm).where(Firm.status=="pending")
    return session.exec(statement).all()

#Approve firm 
def appove_firm(session:Session,firm_id:int):
    firm=Session.get(firm,firm_id)
    if firm:
        firm.status="approved"
        session.add(firm)
        session.commit()
        session.refresh(firm)
    return firm 

#Reject firm
def reject_firm(session:Session,firm_id:int):
    firm=session.get(Firm,firm_id)
    if firm:
        firm.status="rejected"
        session.add(firm)
        session.commit()
        session.refresh(firm)
    return firm 