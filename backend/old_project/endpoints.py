# from typing import List
#
# from fastapi import APIRouter, Depends
#
# from old_project.schemas import ResponseUser, QueryUser
# from old_project.database import db
#
#
# router = APIRouter(prefix="/user", tags=["USER"])
#
#
# @router.get("/filter", response_model=List[ResponseUser], description="Get filtered and sorted data data!")
# async def get_users(query: QueryUser = Depends()):
#     return await db.get_filter(query=query)
#
#
# __all__ = [
#     "router"
# ]
