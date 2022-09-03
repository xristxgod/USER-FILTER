from fastapi import FastAPI

from src import main_router
from src.database import inserter


app = FastAPI(title="Prod project!")
app.include_router(main_router)


@app.on_event("startup")
async def startup():
    inserter()