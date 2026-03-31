from fastapi import FastAPI
from sqlmodel import SQLModel
from db import engine
from user import router
from firm import router1

app = FastAPI()

SQLModel.metadata.create_all(engine)


@app.get("/")
async def start():
    return {"msg": "Booking system running"}


app.include_router(router)
app.include_router(router1)