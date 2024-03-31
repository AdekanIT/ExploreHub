from typing import Union
from pydantic import BaseModel


class TourAgent(BaseModel):
    country_id: int
    agent_name: str
    agent_tellNo: str
    agent_email: str
    tour_cost: float


class TourAgentEdit(BaseModel):
    agent_id: int
    edit: str
    new: Union[str, int, float]