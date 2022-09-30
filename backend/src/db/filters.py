from typing import NoReturn
from typing import List

from src.db import Manager
from src.db.models import User
from src.rest.schemas import QueryUserFilter


class FilterManager:

    def __init__(self, manager: Manager, query: QueryUserFilter):
        self.manager = manager
        self.query = query

        self.params = {}

    def _set_base_filter(self) -> NoReturn:
        self.params.update({
            "company": self.query.company,
            "gender": self.query.gender,
            "jobTitle": self.query.jobTitle
        })

    def _set_age_filter(self) -> NoReturn:
        self.params.update({
            "age": {
                "$gt": self.query.ageStart,
                "$lt": self.query.ageEnd
            }
        })

    def _set_join_date_filter(self) -> NoReturn:
        self.params.update({
            "joinDate": {
                "$gte": self.query.joinDateStart,
                "$lt": self.query.joinDateEnd
            }
        })

    def _set_salary_filter(self) -> NoReturn:
        self.params.update({
            "salary": {
                "$gt": self.query.salaryStart,
                "$lt": self.query.salaryEnd
            }
        })

    def _set(self) -> NoReturn:
        self._set_base_filter()
        self._set_age_filter()
        self._set_join_date_filter()
        self._set_salary_filter()

    def filter(self) -> List[User]:
        self._set()
        print(self.params)


__all__ = [
    "FilterManager"
]
