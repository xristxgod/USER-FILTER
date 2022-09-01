import decimal
from typing import Optional, Dict
from datetime import datetime

from pydantic import BaseModel, Field, EmailStr, ValidationError, validator


class QueryUser(BaseModel):
    age: Optional[int] = Field(description="User age", default=None)
    company: Optional[str] = Field(description="Company", default=None)
    gender: Optional[str] = Field(description="User gender", default=None)
    jobTitle: Optional[str] = Field(description="Job title", default=None)
    joinDateStart: Optional[datetime] = Field(default=None)
    joinDateEnd: Optional[datetime] = Field(default=None)
    salaryStart: Optional[decimal.Decimal] = Field(default=None)
    salaryEnd: Optional[decimal.Decimal] = Field(default=None)

    @validator("gender")
    def valid_gender(self, gender: str):
        if gender not in ["female", "male", "other"]:
            raise ValidationError("Gender can only be: female, male, other")
        return gender

    @validator("joinDateStart")
    def valid_join_date(self, join_date_start: datetime, values: Dict):
        if join_date_start < values["joinDateEnd"]:
            raise ValidationError()
        return join_date_start


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
