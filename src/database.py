import decimal
from datetime import datetime
from typing import Optional, List, Dict

import pymongo

from src.schemas import ResponseUser, QueryUser
from config import Config, FILE


class Filter:
    @staticmethod
    def filter_integer(start: Optional[int] = None, end: Optional[int] = None) -> Dict:
        if start is None and end is None:
            return {}
        elif start and end is None:
            return {"age": {"$gt": start - 1}}
        elif start is None and end:
            return {"age": {"$lt": end + 1}}
        elif start == end:
            return {"age": start}
        else:
            return {"age": {"$gt": start, "$lt": end}}

    @staticmethod
    def filter_datetime(start: Optional[datetime] = None, end: Optional[datetime] = None) -> Dict:
        if start is None and end is None:
            return {}


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
        return [ResponseUser(**user) for user in self.collection.find({})]

    def get_filter(self, query: QueryUser) -> List[ResponseUser]:
        """Search users by filters"""
        _filters = {}
        if query.company is not None:
            _filters.update({"company": query.company})
        if query.gender is not None:
            _filters.update({"gender": query.gender})
        if query.jobTitle is not None:
            _filters.update({"job_title": query.jobTitle})
        if query.ageStart or query.ageEnd:
            _filters.update(Filter.filter_integer(start=query.ageStart, end=query.ageEnd))
        if query.joinDateStart or query.joinDateEnd:
            _filters.update(Filter.filter_datetime(start=query.joinDateStart, end=query.joinDateEnd))
        if query.salaryStart or query.salaryEnd:
            _filters.update(Filter.filter_integer(start=query.salaryStart, end=query.salaryEnd))

        users = [ResponseUser(**user) for user in self.collection.find(_filters)]
        return users

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
