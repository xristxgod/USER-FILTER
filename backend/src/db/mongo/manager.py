import logging
from typing import NoReturn
from typing import List

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.utils import convert_salary
from src.db import Manager
from src.db.models import OID, User


class MongoManager(Manager):

    async def connect_to_database(self, path: str) -> NoReturn:
        logging.info("Connecting to MongoDB")
        self.client = AsyncIOMotorClient(
            path,
            # maxPoolSize=10,
            # minPoolSize=10
        )
        self.db = self.client.main_db
        logging.info("Connected to MongoDB")

    async def close_database_connection(self) -> NoReturn:
        logging.info("Closing connection with MongoDB")
        self.client.close()
        logging.info("Closed connection with MongoDB")

    @convert_salary
    async def add_user(self, user: User) -> NoReturn:
        await self.db.users.insert_one(user.dict(exclude={"id"}))

    async def get_users(self) -> List[User]:
        users = []
        users_qs = self.db.users.find()
        async for user in users_qs:
            users.append(User(id=user["_id"], **user))
        return users

    async def get_user(self, user_id: OID) -> User:
        user_qs = await self.db.users.find_one({"_id": ObjectId(user_id)})
        if user_qs:
            return User(id=user_qs["_id"], **user_qs)

    @convert_salary
    async def update_user(self, user_id: OID, user: User) -> NoReturn:
        await self.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user.dict(exclude={"id"})}
        )

    async def delete_user(self, user_id: OID) -> NoReturn:
        await self.db.users.delete_one({"_id": ObjectId(user_id)})


__all__ = [
    "MongoManager"
]
