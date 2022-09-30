import logging
from typing import NoReturn
from typing import List

from fastapi import HTTPException, status
import motor.motor_asyncio as mongo_async
from bson import ObjectId

import pymongo
import pymongo.errors as mongo_ex
from src.utils import convert_salary, convert_join_date
from src.db import Manager
from src.db.models import OID, User


class MongoManager(Manager):

    async def set_index(self) -> NoReturn:
        logging.info("Set index")
        await self.db.users.create_index(
            [("email", pymongo.DESCENDING), ("name", pymongo.ASCENDING)],
            unique=True
        )

    async def connect_to_database(self, path: str) -> NoReturn:
        logging.info("Connecting to MongoDB")
        self.client = mongo_async.AsyncIOMotorClient(path, maxPoolSize=10, minPoolSize=10)
        self.db = self.client.main_db
        await self.set_index()
        logging.info("Connected to MongoDB")

    async def close_database_connection(self) -> NoReturn:
        logging.info("Closing connection with MongoDB")
        self.client.close()
        logging.info("Closed connection with MongoDB")

    @convert_salary
    async def add_user(self, user: User) -> NoReturn:
        try:
            await self.db.users.insert_one(user.dict(exclude={"id"}))
        except mongo_ex.DuplicateKeyError:
            raise HTTPException(
                detail="A user with that Name: '{}' or email: '{}' already exists!".format(user.name, user.email),
                status_code=status.HTTP_402_PAYMENT_REQUIRED
            )

    @convert_join_date
    async def get_users(self) -> List[User]:
        users = []
        users_qs = self.db.users.find()
        async for user in users_qs:
            users.append(User(id=user["_id"], **user))
        return users

    @convert_join_date
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


class FilterMongoManager(MongoManager):

    def filter(self):
        pass


__all__ = [
    "MongoManager"
]
