from typing import List

from fastapi import APIRouter, Depends

from src.db import Manager, get_database
from src.db.models import OID, User
from src.rest.schemas import ResponseSuccessfully


router = APIRouter(prefix="/user", tags=["USER"])


@router.post(
    "/",
    status_code=201,
    response_model=ResponseSuccessfully
)
async def add_user(user: User, db: Manager = Depends(get_database)):
    await db.add_user(user)
    return ResponseSuccessfully(successfully=True)


@router.get(
    "/",
    response_model=List[User]
)
async def all_users(db: Manager = Depends(get_database)):
    return await db.get_users()


@router.get(
    "/{user_id}",
    response_model=User
)
async def single_user(user_id: OID, db: Manager = Depends(get_database)):
    return await db.get_user(user_id=user_id)


@router.put(
    "/{user_id}",
    response_model=ResponseSuccessfully
)
async def update_user(user_id: OID, user: User, db: Manager = Depends(get_database)):
    await db.update_user(user_id=user_id, user=user)
    return ResponseSuccessfully(successfully=True)


@router.delete(
    "/{user_id}",
    response_model=ResponseSuccessfully
)
async def delete_user(user_id: OID, db: Manager = Depends(get_database)):
    await db.delete_user(user_id=user_id)
    return ResponseSuccessfully(successfully=True)


__all__ = [
    "router"
]
