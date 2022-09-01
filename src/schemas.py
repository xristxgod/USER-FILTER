import decimal
from typing import Optional, Dict
from datetime import datetime

from fastapi import HTTPException, status
from dateutil import parser

from pydantic import BaseModel, Field, EmailStr, validator


def is_iso_8601(date: str) -> datetime:
    try:
        return parser.parse(date)
    except parser._parser.ParserError as error:
        raise HTTPException(
            detail="The date must be in the format: ISO 8601",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )


class QueryUser(BaseModel):
    age: Optional[int] = Field(description="User age", default=None)
    company: Optional[str] = Field(description="Company", default=None)
    gender: Optional[str] = Field(description="User gender", default=None)
    jobTitle: Optional[str] = Field(description="Job title", default=None)
    joinDateStart: Optional[str] = Field(default=None)      # ISO 8601
    joinDateEnd: Optional[str] = Field(default=None)        # ISO 8601
    salaryStart: Optional[decimal.Decimal] = Field(default=None)
    salaryEnd: Optional[decimal.Decimal] = Field(default=None)

    @validator("gender")
    def valid_gender(cls, gender: str):
        if gender is None:
            return None
        if gender not in ["female", "male", "other"]:
            raise HTTPException(
                detail="Gender can only be: female, male, other",
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        return gender

    @validator("joinDateStart")
    def valid_join_date_start(cls, join_date_start: Optional[str]):
        if join_date_start is None:
            return None
        return is_iso_8601(join_date_start)

    @validator("joinDateEnd")
    def valid_join_date_end(cls, join_date_end: str, values: Dict):
        if join_date_end is None and values.get("joinDateStart"):
            return values["joinDateStart"]
        elif join_date_end is None and not values.get("joinDateStart"):
            return None
        elif join_date_end and not values.get("joinDateStart"):
            return is_iso_8601(join_date_end)
        else:
            end = is_iso_8601(join_date_end)
            if end < values["joinDateStart"]:
                raise HTTPException(
                    detail="The start date must be less than the end date!",
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
                )
            return is_iso_8601(join_date_end)

    @validator("salaryStart")
    def valid_salary_start(cls, salary_start: decimal.Decimal):
        if salary_start is None:
            return None
        return salary_start

    @validator("salaryEnd")
    def valid_salary_end(cls, salary_end: decimal.Decimal, values: Dict):
        if salary_end is None and values.get("salaryStart"):
            return values.get("salaryStart")
        elif salary_end is None and not values.get("salaryStart"):
            return None
        elif salary_end and not values.get("salaryStart"):
            return salary_end
        else:
            if salary_end < values.get("salaryStart"):
                raise HTTPException(
                    detail="The starting salary must be less than the final salary!",
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
                )
            return salary_end


class ResponseUser(BaseModel):
    name: str = Field(description="User name")
    email: EmailStr = Field(description="Email")
    age: int = Field(description="User age")
    company: str = Field(description="Company")
    joinDate: datetime = Field(description="Date of employment", alias="join_date")
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
                "join_date": "2003-12-28T18:18:10-08:00",
                "job_title": "janitor",
                "gender": "female",
                "salary": 9632
            }
        }


__all__ = [
    "ResponseUser", "QueryUser"
]
