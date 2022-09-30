from typing import NoReturn
from typing import Optional, List
from abc import abstractproperty


from .models import OID, UserDB


class Manager:
    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    @abstractproperty
    async def connect_to_database(self, path: str) -> NoReturn: ...

    @abstractproperty
    async def close_database_connection(self) -> NoReturn: ...

    @abstractproperty
    async def add_user(self, user: UserDB) -> NoReturn: ...

    @abstractproperty
    async def get_users(self) -> List[UserDB]: ...

    @abstractproperty
    async def get_user(self, user_id: OID) -> Optional[UserDB]: ...

    @abstractproperty
    async def update_user(self, user_id: OID, user: UserDB) -> NoReturn: ...

    @abstractproperty
    async def delete_user(self, user_id: OID) -> NoReturn: ...


__all__ = [
    "Manager"
]
