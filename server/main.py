from fastapi import FastAPI

from server.config.factory import settings

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok", "appName": settings.APP_NAME}
