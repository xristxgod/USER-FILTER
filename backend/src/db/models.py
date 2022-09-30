import decimal
from typing import Optional
from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel, Field
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


class User(BaseDBModel):
    id: Optional[OID] = Field(description="User ID")
    name: str = Field(description="User name")
    email: EmailStr = Field(description="Email")
    age: int = Field(description="User age")
    company: str = Field(description="Company")
    joinDate: datetime = Field(description="Date of employment")
    jobTitle: str = Field(description="Job title", alias="job_title")
    gender: str = Field(description="User gender")
    salary: decimal.Decimal = Field(description="Salary")

    class Config:
        schema_extra = {
            "example": {
                "name": "Flynn Vang",
                "email": "turpis.non@Nunc.edu",
                "age": 69,
                "company": "Twitter",
                "joinDate": "2003-12-28T18:18:10-08:00",
                "jobTitle": "janitor",
                "gender": "female",
                "salary": 9632
            }
        }


__all__ = [
    "OID",
    "User"
]