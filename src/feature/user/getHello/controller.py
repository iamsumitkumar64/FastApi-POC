from .handler import get_hello_handler
from fastapi import APIRouter

getHelloRouter = APIRouter()

@getHelloRouter.get("/hello")
async def get_hello():
    response=await get_hello_handler()
    return response