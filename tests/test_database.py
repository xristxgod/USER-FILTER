import unittest
from unittest.mock import Mock, patch


from src.schemas import QueryUser, ResponseUser
from src.database import db


TEST_DATA = [
    {
        "name": "Derek Cole",
        "email": "nec.metus@VivamusnisiMauris.co.uk",
        "age": 46,
        "company": "Google",
        "join_date": "2012-03-20T09:18:26-07:00",
        "job_title": "director",
        "gender": "male",
        "salary": 1101
    },
    {
        "name": "Russell Parrish",
        "email": "nonummy.Fusce@Maurisnon.com",
        "age": 50,
        "company": "Auchan",
        "join_date": "2014-10-21T06:14:41-07:00",
        "job_title": "janitor",
        "gender": "female",
        "salary": 3292
    },
    {
        "name": "Kenneth Dunlap",
        "email": "eu.accumsan@Phasellus.ca",
        "age": 56,
        "company": "Auchan",
        "join_date": "2004-04-17T19:04:25-07:00",
        "job_title": "driver",
        "gender": "female",
        "salary": 1135
    },
    {
        "name": "Vincent Martinez",
        "email": "libero@vehicula.edu",
        "age": 47,
        "company": "LinkedIn",
        "join_date": "1997-11-18T07:39:48-08:00",
        "job_title": "janitor",
        "gender": "male",
        "salary": 2665
    },
    {
        "name": "Abbot Leon",
        "email": "gravida@ametmetusAliquam.co.uk",
        "age": 37,
        "company": "Amazon",
        "join_date": "2009-03-22T03:13:12-07:00",
        "job_title": "director",
        "gender": "other",
        "salary": 1334
    },
    {
        "name": "Paul Rose",
        "email": "sit.amet@eu.org",
        "age": 21,
        "company": "Auchan",
        "join_date": "1999-11-29T19:42:18-08:00",
        "job_title": "designer",
        "gender": "female",
        "salary": 1095
    }
]


class TestDatabase(unittest.TestCase):
    @patch("src.database.db.collection.find")
    def test_get_all_data(self, find: Mock):
        find.return_value = TEST_DATA
        result = db.get_all_data()
        assert isinstance(result, list)
        assert isinstance(result[0], ResponseUser)
