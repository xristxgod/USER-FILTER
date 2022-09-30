# from typing import Optional, Dict
# from datetime import datetime
#
# from fastapi import HTTPException, status
# from dateutil import parser
#
# from pydantic import BaseModel, Field, EmailStr, validator
#
#
# def _is_iso_8601(date: Optional[str] = None) -> Optional[datetime]:
#     """Check if a string is iso date!"""
#     try:
#         return parser.parse(date) if date is not None else None
#     except parser._parser.ParserError as error:
#         raise HTTPException(
#             detail="The date must be in the format: ISO 8601",
#             status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
#         )
#
#
# class QueryUser(BaseModel):
#     ageStart: Optional[int] = Field(description="Start with", default=None)
#     ageEnd: Optional[int] = Field(description="Finish on", default=None)
#     company: Optional[str] = Field(description="Company", default=None)
#     gender: Optional[str] = Field(description="User gender", default=None)
#     jobTitle: Optional[str] = Field(description="Job title", default=None)
#     joinDateStart: Optional[str] = Field(description="Start with", default=None)                      # ISO 8601
#     joinDateEnd: Optional[str] = Field(description="Finish on", default=None)                        # ISO 8601
#     salaryStart: Optional[int] = Field(description="Start with", default=None)
#     salaryEnd: Optional[int] = Field(description="Finish on", default=None)
#
#     @validator("ageEnd")
#     def valid_age_end(cls, age: int, values: Dict):
#         if age is None and not values.get("ageStart"):
#             return None
#         elif age and not values.get("ageStart"):
#             return age
#         elif age is not None and values.get("ageStart") is not None and age < values.get("ageStart"):
#             raise HTTPException(
#                 detail="The starting age must be less than the end!",
#                 status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
#             )
#         return age
#
#     @validator("gender")
#     def valid_gender(cls, gender: str):
#         if gender is None:
#             return None
#         if gender not in ["female", "male", "other"]:
#             raise HTTPException(
#                 detail="Gender can only be: female, male, other",
#                 status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
#             )
#         return gender
#
#     @validator("joinDateStart")
#     def valid_join_date_start(cls, join_date: str):
#         return _is_iso_8601(join_date)
#
#     @validator("joinDateEnd")
#     def valid_join_date_end(cls, join_date: str, values: Dict):
#         join_date = _is_iso_8601(join_date)
#         if join_date is None and not values.get("joinDateStart"):
#             return None
#         elif join_date and not values.get("joinDateStart"):
#             return join_date
#         elif join_date is not None and values.get("joinDateStart") and join_date < values.get("joinDateStart"):
#             raise HTTPException(
#                 detail="The start date must be less than the end date!",
#                 status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
#             )
#         return join_date
#
#     @validator("salaryEnd")
#     def valid_salary_end(cls, salary: int, values: Dict):
#         if salary is None and not values.get("salaryStart"):
#             return None
#         elif salary and not values.get("salaryStart"):
#             return salary
#         elif salary is not None and values.get("salaryStart") is not None and salary < values.get("salaryStart"):
#             raise HTTPException(
#                 detail="The starting salary must be less than the final salary!",
#                 status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
#             )
#         return salary
#
#
# class ResponseUser(BaseModel):
#     name: str = Field(description="User name")
#     email: EmailStr = Field(description="Email")
#     age: int = Field(description="User age")
#     company: str = Field(description="Company")
#     joinDate: datetime = Field(description="Date of employment", alias="join_date")
#     jobTitle: str = Field(description="Job title", alias="job_title")
#     gender: str = Field(description="User gender")
#     salary: int = Field(description="Salary")
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Flynn Vang",
#                 "email": "turpis.non@Nunc.edu",
#                 "age": 69,
#                 "company": "Twitter",
#                 "join_date": "2003-12-28T18:18:10-08:00",
#                 "job_title": "janitor",
#                 "gender": "female",
#                 "salary": 9632
#             }
#         }
#
#
# __all__ = [
#     "ResponseUser", "QueryUser"
# ]
