from datetime import datetime, timedelta
from typing import Optional, List, Dict

import pymongo

from src.schemas import ResponseUser, QueryUser
from config import Config, FILE


class Filter:
    """Filter - to create filters!"""
    @staticmethod
    def filter_integer(name: str, *, start: Optional[int] = None, end: Optional[int] = None) -> Dict:
        """
        Create a filter for integers!
        :param name: Field name
        :param start: Start from
        :param end: Finish on
        :return: Finished filter
        """
        filters = {}
        if start:
            filters.update({"$gt": start - 1})
        if end:
            filters.update({"$lt": end + 1})

        if len(filters) == 0:
            return {}
        else:
            return {name: filters}

    @staticmethod
    def filter_datetime(name: str, *, start: Optional[datetime] = None, end: Optional[datetime] = None) -> Dict:
        """
        Create filter for datetime!
        :param name: Field name
        :param start: Start from
        :param end: Finish on
        :return: Finished filter
        """
        sec = timedelta(microseconds=1)
        filters = {}
        if start:
            filters.update({"$gt": (start - sec).isoformat()})
        if end:
            filters.update({"$lt": (end + sec).isoformat()})

        if len(filters) == 0:
            return {}
        else:
            return {name: filters}


class Database:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.client = pymongo.MongoClient(Config.MONGODB_URL)
        self.db = self.client.get_database(Config.MONGODB_NAME)
        self.collection = self.db.get_collection(Config.MONGODB_COLLECTION)

    async def get_all_data(self) -> List[ResponseUser]:
        """Return all users!"""
        return [ResponseUser(**user) for user in self.collection.find({})]

    async def get_filter(self, query: QueryUser) -> List[ResponseUser]:
        """Search users by filters"""
        _filters = {}

        if query.company is not None:
            _filters.update({"company": query.company})
        if query.gender is not None:
            _filters.update({"gender": query.gender})
        if query.jobTitle is not None:
            _filters.update({"job_title": query.jobTitle})
        if query.ageStart or query.ageEnd:
            _filters.update(Filter.filter_integer("age", start=query.ageStart, end=query.ageEnd))
        if query.joinDateStart or query.joinDateEnd:
            _filters.update(Filter.filter_datetime(
                "join_date",
                start=query.joinDateStart,
                end=query.joinDateEnd
            ))
        if query.salaryStart or query.salaryEnd:
            _filters.update(Filter.filter_integer(
                "salary",
                start=query.salaryStart,
                end=query.salaryEnd
            ))

        return [ResponseUser(**user) for user in self.collection.find(_filters)]

    async def insert_data(self, data: List[Dict]) -> bool:
        """Add data to table"""
        self.collection.insert_many(data)
        return True


db = Database()


async def inserter():
    """Install test users in the database!"""
    import json
    import logging
    if len(await db.get_all_data()) == 0:
        with open(FILE, "r") as file:
            data = json.loads(file.read())
        await db.insert_data(data=data)
        logging.info("Add test data to Database")
    return


__all__ = [
    "db", "inserter", "Filter"
]
