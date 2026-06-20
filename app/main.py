from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Weather AI Agent"
)

app.include_router(router)