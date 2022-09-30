from enum import Enum
from typing import Optional, Dict

from fastapi import HTTPException, status
from pydantic import BaseModel, Field, validator


class GenderEnum(Enum):
    pass


class QueryUserFilter(BaseModel):
    ageStart: Optional[int] = Field(description="Start with", default=None)
    ageEnd: Optional[int] = Field(description="Finish on", default=None)
    company: Optional[str] = Field(description="Company", default=None)
    gender: Optional[str] = Field(description="User gender", default=None)
    jobTitle: Optional[str] = Field(description="Job title", default=None)
    joinDateStart: Optional[str] = Field(description="Start with", default=None)
    joinDateEnd: Optional[str] = Field(description="Finish on", default=None)
    salaryStart: Optional[int] = Field(description="Start with", default=None)
    salaryEnd: Optional[int] = Field(description="Finish on", default=None)

    @validator("ageEnd")
    def valid_age_end(cls, age: int, values: Dict):
        if age is None and not values.get("ageStart"):
            return None
        elif age and not values.get("ageStart"):
            return age
        elif age is not None and values.get("ageStart") is not None and age < values.get("ageStart"):
            raise HTTPException(
                detail="The starting age must be less than the end!",
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        return age


class ResponseSuccessfully(BaseModel):
    successfully: bool = Field(default=True)

    class Config:
        schema_extra = {
            "example": {
                "successfully": True
            }
        }


__all__ = [
    "ResponseSuccessfully"
]
