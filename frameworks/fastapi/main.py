# File: frameworks/fastapi/main.py

from fastapi import FastAPI
from frameworks.fastapi.routes import auth_routes

app = FastAPI()
app.include_router(auth_routes.router)
