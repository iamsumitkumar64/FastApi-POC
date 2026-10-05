from fastapi import APIRouter
from .getHello.controller import getHelloRouter
from .createHello.controller import createHelloRouter

helloRouter = APIRouter()
helloRouter.include_router(getHelloRouter)
helloRouter.include_router(createHelloRouter)