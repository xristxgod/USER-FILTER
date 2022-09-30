import decimal
from typing import NoReturn
from typing import Callable

from bson import Decimal128

from src.db.models import User


def convert_salary(func: Callable) -> NoReturn:
    def wrapper(*args, **kwargs):
        user: User = kwargs.pop("user")
        if isinstance(user.salary, decimal.Decimal):
            user.salary = Decimal128(str(user.salary))
        kwargs["user"] = user
        func(*args, **kwargs)
    return wrapper


__all__ = [
    "convert_salary"
]
