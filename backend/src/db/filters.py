from datetime import datetime
from dataclasses import dataclass, field
from typing import NoReturn
from typing import Union, Optional, List

from src.db import Manager
from src.db.models import User
from src.rest.schemas import NUMERIC, QueryUserFilter


@dataclass()
class FilterData:
    name: str
    start: Optional[Union[NUMERIC, datetime]] = field(default=None)
    end: Optional[Union[NUMERIC, datetime]] = field(default=None)


class FilterManager:

    def __init__(self, manager: Manager, query: QueryUserFilter):
        self.manager = manager
        self.query = query

        self.params = {}
        self._set()

    def _set_base_filter(self) -> NoReturn:
        if self.query.company:
            self.params.update({"company": self.query.company})
        if self.query.gender:
            self.params.update({"gender": self.query.gender})
        if self.query.jobTitle:
            self.params.update({"jobTitle": self.query.jobTitle})

    def _set_filter(self, data: FilterData) -> NoReturn:
        params = {}
        if data.start:
            params.update({"$gte": data.start})
        if data.end:
            params.update({"$lte": data.end})
        if params:
            self.params.update({data.name: params})

    def _set(self) -> NoReturn:
        self._set_base_filter()
        self._set_filter(FilterData(name="age", start=self.query.ageStart, end=self.query.ageEnd))
        self._set_filter(FilterData(name="joinDate", start=self.query.joinDateStart, end=self.query.joinDateEnd))
        self._set_filter(FilterData(name="salary", start=self.query.salaryStart, end=self.query.salaryEnd))

    async def filter(self) -> List[User]:
        return [
            User(id=user["_id"], **user)
            async for user in self.manager.db.users.find(self.params)
        ]


__all__ = [
    "FilterManager"
]
