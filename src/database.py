from typing import List, Dict

import pymongo

from src.schemas import ResponseUser
from config import Config, FILE


class Database:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.client = pymongo.MongoClient(Config.MONGODB_URL)
        self.db = self.client.get_database(Config.MONGODB_NAME)
        self.collection = self.db.get_collection(Config.MONGODB_COLLECTION)

    def get_all_data(self) -> List[ResponseUser]:
        users = self.collection.find({})
        data = []
        for user in users:
            data.append(ResponseUser(**user))
        return data

    def get_filter(self):
        pass

    def insert_data(self, data: List[Dict]) -> bool:
        self.collection.insert_many(data)
        return True


db = Database()


def inserter():
    import json
    import logging
    if len(db.get_all_data()) != 0:
        return
    with open(FILE, "r") as file:
        data = json.loads(file.read())
    db.insert_data(data=data)
    logging.info("Add test data to Database")


__all__ = [
    "db", "inserter"
]
