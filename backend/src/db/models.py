import decimal
from typing import Optional
from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel
from pydantic import EmailStr


class OID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if v == "":
            raise TypeError("ObjectId is empty")
        if not ObjectId.is_valid(v):
            raise TypeError("ObjectId invalid")
        return str(v)


class BaseDBModel(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

        @classmethod
        def alias_generator(cls, string: str) -> str:
            """CamelCase generator"""
            temp = string.split("_")
            return temp[0] + "".join(ele.title() for ele in temp[1:])


class UserDB(BaseDBModel):
    id: Optional[OID]
    name: str
    email: EmailStr
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: str
    salary: decimal.Decimal


__all__ = [
    "OID",
    "UserDB"
]