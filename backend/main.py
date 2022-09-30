import uvicorn
from fastapi import FastAPI

from src.db import db
from src.settings import get_settings
from src.rest import views

app = FastAPI(title="User project!")

app.include_router(views.router, prefix="/api")


@app.on_event("startup")
async def startup():
    settings = get_settings()
    await db.connect_to_database(path=settings.db_path)


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
