from typing import Union
from pydantic import BaseModel


class Sight(BaseModel):
    country_id: int
    sight_name: str
    sight_info: str
    sight_address: str


class SightEdit(BaseModel):
    sight_id: int
    edit: str
    new: Union[str, int, float]
