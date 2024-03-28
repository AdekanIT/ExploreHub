from database.agentservice import get_agents_db, get_all_agent_db, get_agents_by_country_db, add_agent_db, edit_agent_db, delete_agent_db
from api.agent import TourAgent, TourAgentEdit
from fastapi import APIRouter


agent_router = APIRouter(prefix='/tour-agent', tags=['Methods for agent'])


@agent_router.get('/all-agent')
async def get_all_agent():
    agent = get_all_agent_db()
    return agent


@agent_router.post('/add-agent')
async def add_agent(data: TourAgent):
    agent = add_agent_db(**data.model_dump())
    return agent


@agent_router.get('/agent')
async def get_agent(agent_id: int):
    agent = get_agents_db(agent_id=agent_id)
    return agent


@agent_router.get('/by-country')
async def get_agent_by_country(country_id):
    agent = get_agents_by_country_db(country_id=country_id)
    return agent


@agent_router.patch('/edit-agent')
async def edit_agent(data: TourAgentEdit):
    agent = edit_agent_db(**data.model_dump())
    return agent


@agent_router.delete('/delete-agent')
async def delete_agent(agent_id: int):
    agent = delete_agent_db(agent_id=agent_id)
    return agent



















































