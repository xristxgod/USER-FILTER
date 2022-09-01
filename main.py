from fastapi import FastAPI

from src import main_router
from src.database import inserter


app = FastAPI(
    title="Test project!"
)

app.include_router(main_router)


@app.on_event(
    "startup"
)
async def startup():
    inserter()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app")
