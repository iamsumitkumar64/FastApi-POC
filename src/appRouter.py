from fastapi import APIRouter
from feature.hello.helloRouter import helloRouter
from feature.book.helloRouter import helloRouter as bookRouter

appRouter = APIRouter()

appRouter.include_router(helloRouter)
appRouter.include_router(bookRouter)