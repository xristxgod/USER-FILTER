from typing import List

from fastapi import APIRouter, Depends

from .schemas import ResponseUser, QueryUser
from .database import db


router = APIRouter(prefix="/user", tags=["USER"])


@router.get("/filter", response_model=List[ResponseUser], description="Get filtered and sorted data data!")
async def get_users(query: QueryUser = Depends()):
    return db.get_filter(query=query)


__all__ = [
    "router"
]
