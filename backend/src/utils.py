import decimal
import functools
from typing import NoReturn
from typing import Callable, Union, List

from bson import Decimal128

from src.db.models import User


def convert_salary(func: Callable):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs) -> NoReturn:
        user: User = kwargs.pop("user")
        if isinstance(user.salary, decimal.Decimal):
            user.salary = Decimal128(str(user.salary))
        kwargs["user"] = user
        await func(*args, **kwargs)
    return wrapper


def convert_join_date(func: Callable):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs) -> Union[List[User], User]:
        result: Union[List[User], User] = await func(*args, **kwargs)
        if isinstance(result, list):
            for res in result:
                res.joinDate = res.joinDate.isoformat()
        else:
            result.joinDate = result.joinDate.isoformat()
        return result
    return wrapper


__all__ = [
    "convert_salary",
    "convert_join_date"
]
