from fastapi import FastAPI
import uvicorn
from config.envConfig import envConfig
from .appRouter import appRouter

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Server!"} 

app.include_router(appRouter)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=envConfig.HOSTNAME,
        port=envConfig.PORT,
        reload=True
    )