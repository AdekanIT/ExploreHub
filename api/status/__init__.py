from pydantic import BaseModel
from typing import  Union


class Status(BaseModel):
    status_name: str
    cost: float


class StatusEdit(BaseModel):
    status_id: int
    edit: str
    new: Union[str, int, float]