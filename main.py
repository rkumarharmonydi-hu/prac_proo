from fastapi import FastAPI, APIRouter
from firm import router1
from user import router
app = FastAPI()
@app.get("/")
async def start():
    return {"msg":"Bokking system running"}
app.include_router(router)
app.include_router(router1)