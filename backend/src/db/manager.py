from typing import NoReturn
from typing import Optional, List
from abc import abstractmethod


from .models import OID, User


class Manager:
    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    @abstractmethod
    async def connect_to_database(self, path: str) -> NoReturn: ...

    @abstractmethod
    async def close_database_connection(self) -> NoReturn: ...

    @abstractmethod
    async def add_user(self, user: User) -> NoReturn: ...

    @abstractmethod
    async def get_users(self) -> List[User]: ...

    @abstractmethod
    async def get_user(self, user_id: OID) -> Optional[User]: ...

    @abstractmethod
    async def update_user(self, user_id: OID, user: User) -> NoReturn: ...

    @abstractmethod
    async def delete_user(self, user_id: OID) -> NoReturn: ...


__all__ = [
    "Manager"
]
