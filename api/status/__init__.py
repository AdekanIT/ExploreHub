from pydantic import BaseModel


class Status(BaseModel):
    status_name: str
    cost: float


class StatusEdit(BaseModel):
    status_id: int
    edit: str
    new: str | int | float