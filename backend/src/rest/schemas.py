from typing import Optional

from pydantic import BaseModel, Field


class QueryUserFilter(BaseModel):
    ageStart: Optional[int] = Field(description="Start with", default=None)
    ageEnd: Optional[int] = Field(description="Finish on", default=None)
    company: Optional[str] = Field(description="Company", default=None)
    gender: Optional[str] = Field(description="User gender", default=None)
    jobTitle: Optional[str] = Field(description="Job title", default=None)
    joinDateStart: Optional[str] = Field(description="Start with", default=None)
    joinDateEnd: Optional[str] = Field(description="Finish on", default=None)  # ISO 8601
    salaryStart: Optional[int] = Field(description="Start with", default=None)
    salaryEnd: Optional[int] = Field(description="Finish on", default=None)


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
