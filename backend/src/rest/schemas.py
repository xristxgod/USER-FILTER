import decimal
from enum import Enum, IntEnum
from datetime import datetime
from typing import Union, Optional, Dict

from fastapi import HTTPException, status
from pydantic import BaseModel, Field, validator


NUMERIC = Union[decimal.Decimal, float, int]


class SortMethod(IntEnum):
    asc = 0
    desc = 1


class SortEnum(Enum):
    id = "id"
    name = "name"
    age = "age"
    joinDate = "joinDate"
    salary = "salary"


class GenderEnum(Enum):
    female = "female"
    male = "male"
    other = "other"


class QueryUserSorted(BaseModel):
    sortField: Optional[SortMethod] = Field(default=None, description="By which field to sort")
    sortMethod: Optional[SortMethod] = Field(default=None, description="DESC or ASC sort")


class QueryUserFilter(BaseModel):
    ageStart: Optional[int] = Field(description="Start with", default=None)
    ageEnd: Optional[int] = Field(description="Finish on", default=None)
    company: Optional[str] = Field(description="Company", default=None)
    gender: Optional[GenderEnum] = Field(description="User gender", default=None)
    jobTitle: Optional[str] = Field(description="Job title", default=None)
    joinDateStart: Optional[datetime] = Field(description="Start with", default=None)
    joinDateEnd: Optional[datetime] = Field(description="Finish on", default=None)
    salaryStart: Optional[NUMERIC] = Field(description="Start with", default=None)
    salaryEnd: Optional[NUMERIC] = Field(description="Finish on", default=None)

    @validator("ageEnd")
    def valid_age(cls, age: int, values: Dict):
        if (age and values["ageStart"]) and values["ageStart"] > age:
            raise HTTPException(
                detail="The starting age must be less than the end!",
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        return age

    @validator("joinDateEnd")
    def valid_join_data(cls, join_data: datetime, values: Dict):
        if (join_data and values["joinDateStart"]) and values["joinDateStart"] > join_data:
            raise HTTPException(
                detail="The start date must be less than the end date!",
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        return join_data

    @validator("salaryEnd")
    def valid_salary(cls, salary: NUMERIC, values: Dict):
        if (salary and values["salaryStart"]) and values["salaryStart"] > salary:
            raise HTTPException(
                detail="The starting salary must be less than the final salary!",
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        return salary


class ResponseSuccessfully(BaseModel):
    successfully: bool = Field(default=True)

    class Config:
        schema_extra = {
            "example": {
                "successfully": True
            }
        }


__all__ = [
    "QueryUserFilter",
    "ResponseSuccessfully",
    "NUMERIC"
]
