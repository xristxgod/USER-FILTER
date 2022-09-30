from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.db import Manager, db
from src.settings import get_settings
from src.rest import views
from config import ALLOW_CORS


app = FastAPI(title="User project!")

app.include_router(views.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_CORS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def add_fake_data(manager: Manager):
    """Install test users in the database!"""
    import os
    import json
    import logging
    import aiofiles
    from src.db.models import User
    from config import ROOT_DIR
    if len(await manager.get_users()) == 0:
        async with aiofiles.open(os.path.join(ROOT_DIR, "fake_data.json"), "r") as file:
            for user in json.loads(await file.read()):
                await manager.add_user(user=User(
                    name=user["name"],
                    email=user["email"],
                    age=user["age"],
                    company=user["company"],
                    joinDate=user["join_date"],
                    jobTitle=user["job_title"],
                    gender=user["gender"],
                    salary=user["salary"],
                ))
        logging.info("Add test data to Database")


@app.on_event("startup")
async def startup():
    settings = get_settings()
    await db.connect_to_database(path=settings.db_path)
    await add_fake_data(manager=db)


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()
