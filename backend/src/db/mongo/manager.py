import logging
from typing import NoReturn
from typing import List

from bson import ObjectId
import motor.motor_asyncio as async_mongodb

from src.db import Manager
from src.db.models import OID, UserDB


class MongoManager(Manager):
    client: async_mongodb.AsyncIOMotorClient
    db: async_mongodb.AsyncIOMotorDatabase

    async def connect_to_database(self, path: str) -> NoReturn:
        logging.info("Connecting to MongoDB")
        self.client = async_mongodb.AsyncIOMotorClient(
            path,
            maxPoolSize=10,
            minPoolSize=10
        )
        self.db = self.client.main_db
        logging.info("Connected to MongoDB")

    async def close_database_connection(self) -> NoReturn:
        logging.info("Closing connection with MongoDB")
        self.client.close()
        logging.info("Closed connection with MongoDB")

    async def add_user(self, user: UserDB) -> NoReturn:
        await self.db.users.insert_one(user.dict(exclude={"id"}))

    async def get_users(self) -> List[UserDB]:
        users = []
        users_qs = self.db.users.find()
        async for user in users_qs:
            users.append(UserDB(id=user["_id"], **user))
        return users

    async def get_user(self, user_id: OID) -> UserDB:
        user_qs = await self.db.users.find_one({"_id": ObjectId(user_id)})
        if user_qs:
            return UserDB(id=user_qs["_id"], **user_qs)

    async def update_user(self, user_id: OID, user: UserDB) -> NoReturn:
        await self.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user.dict(exclude={"id"})}
        )

    async def delete_user(self, user_id: OID) -> NoReturn:
        await self.db.users.delete_one({"_id": ObjectId(user_id)})


__all__ = [
    "MongoManager"
]
