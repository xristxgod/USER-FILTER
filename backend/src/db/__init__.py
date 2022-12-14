from .manager import Manager
from .mongo.manager import MongoManager

db = MongoManager()


async def get_database() -> Manager:
    return db


__all__ = [
    "db",
    "Manager",
    "get_database"
]
