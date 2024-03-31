from typing import Union
from pydantic import BaseModel


class Country(BaseModel):
    country_name: str


class CountryEdit(BaseModel):
    country_id: int
    edit: str
    new: Union[str, int, float]