from fastapi import FastAPI
from database import Base, engine
from api.agent.agent_api import agent_router
from api.sight.sight_api import sight_router
from api.status.status_api import status_router
from api.user.user_api import user_router
from api.hotel.hotel_api import hotel_router
from api.country.country_api import country_router

app = FastAPI(docs_url='/')

app.include_router(agent_router)
app.include_router(sight_router)
app.include_router(status_router)
app.include_router(user_router)
app.include_router(hotel_router)
app.include_router(country_router)

Base.metadata.create_all(bind=engine)