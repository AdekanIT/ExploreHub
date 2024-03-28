from database.sightsservice import (get_sight_db, get_all_sights_db, get_sight_by_country_db, edit_sight_db,
                                    delete_sight_db, add_sights_db)
from fastapi import APIRouter
from api.sight import Sight, SightEdit


sight_router = APIRouter(prefix='/sight', tags=['Methods for sights'])


@sight_router.get('/all-sights')
async def get_all_sights():
    sight = get_all_sights_db()
    return sight


@sight_router.post('/add-sight')
async def add_sight(data: Sight):
    sight = add_sights_db(**data.model_dump())
    return sight


@sight_router.get('/sight')
async def get_sight(sight_id: int):
    sight = get_sight_db(sight_id=sight_id)
    return sight


@sight_router.get('/sight-by-country')
async def get_sight(country_id: int):
    sight = get_sight_by_country_db(country_id=country_id)
    return sight


@sight_router.patch('/edit-sight')
async def edit_sight(data: SightEdit):
    sight = edit_sight_db(**data.model_dump())
    return sight


@sight_router.delete('/delete-sight')
async def delete_sight(sight_id: int):
    sight = delete_sight_db(sight_id=sight_id)
    return sight


































































































