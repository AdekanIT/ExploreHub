from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    fname: str
    lname: str
    tellNo: str
    email: str


class UserEdit(BaseModel):
    user_id: int
    edit: str
    new: Union[str, int, float]