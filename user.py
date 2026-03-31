from fastapi import APIRouter

router = APIRouter(prefix="/booking", tags=["Open"])

@router.get("/name")
async def your_name():
    return {"Name":"Hii i am user"}