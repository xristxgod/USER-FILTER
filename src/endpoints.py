from typing import List

from fastapi import APIRouter, Depends

from .schemas import ResponseUser, QueryUser
from .database import db


router = APIRouter(
    prefix="/user",
    tags=["USER"]
)


@router.get(
    "/filter",
    # response_model=List[ResponseUser]
)
async def get_users(query: QueryUser = Depends()):
    print(query)
