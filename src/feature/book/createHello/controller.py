from fastapi import APIRouter
from .handler import createHelloHandler

createHelloRouter = APIRouter()

@createHelloRouter.post("/hello")
async def create_hello():
    response = await createHelloHandler()
    return response