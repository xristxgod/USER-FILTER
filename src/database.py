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
        if start is None and end is None:
            return {}
        elif start and end is None:
            return {name: {"$gt": start - 1}}
        elif start is None and end:
            return {name: {"$lt": end + 1}}
        elif start == end:
            return {name: start}
        else:
            return {name: {"$gt": start - 1, "$lt": end + 1}}

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
        if start is None and end is None:
            return {}
        elif start and end is None:
            return {name: {"$gt": (start - sec).isoformat()}}
        elif start is None and end:
            return {name: {"$lt": (end + sec).isoformat()}}
        elif start == end:
            return {name: start}
        else:
            return {name: {"$gt": (start - sec).isoformat(), "$lt": (end + sec).isoformat()}}


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
        """Return all users!"""
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

    def insert_data(self, data: List[Dict]) -> bool:
        """Add data to table"""
        self.collection.insert_many(data)
        return True


db = Database()


def inserter():
    """Install test users in the database!"""
    import json
    import logging
    if len(db.get_all_data()) == 0:
        with open(FILE, "r") as file:
            data = json.loads(file.read())
        db.insert_data(data=data)
        logging.info("Add test data to Database")
    return


__all__ = [
    "db", "inserter"
]
