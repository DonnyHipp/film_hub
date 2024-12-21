from fastapi import FastAPI

from src.api.auth.router import auth_router

app = FastAPI()

app.include_router(prefix="/v1", router=auth_router)
