from fastapi import FastAPI
from sqlmodel import SQLModel
from db import engine

from user import router as user_router
from firm import router as firm_router
from admin import router_admin

app = FastAPI()


#  Create tables on startup
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/")
async def start():
    return {"msg": "Booking system running"}


# Include routers
app.include_router(user_router)
app.include_router(firm_router)
app.include_router(router_admin)
