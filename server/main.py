from fastapi import FastAPI

from server.config.factory import settings
from server.utils.startup import create_database_tables

app = FastAPI()


@app.on_event("startup")
async def app_startup():
    await create_database_tables()


@app.get("/health")
async def health_check():
    return {"status": "ok", "appName": settings.APP_NAME}
