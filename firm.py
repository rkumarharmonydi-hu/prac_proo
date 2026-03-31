from fastapi import APIRouter

router1 = APIRouter(prefix="/firm", tags=["Firm admin"])

@router1.post("/name")
async def name():
    return {"name": "Gurdeep(Firm admin)"}