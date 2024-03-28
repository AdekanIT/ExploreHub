from pydantic import BaseModel


class User(BaseModel):
    fname: str
    lname: str
    tellNo: str
    email: str


class UserEdit(BaseModel):
    user_id: int
    edit: str
    new: str | int | float