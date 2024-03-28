from pydantic import BaseModel


class Hotel(BaseModel):
    country_id: int
    hotel_name: str
    cost: float
    address: str


class HotelEdit(BaseModel):
    hotel_id: int
    edit: str
    new: str | int | float