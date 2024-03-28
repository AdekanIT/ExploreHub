from database.countryservice import (add_country_db, get_country_db, get_all_country_db,
                                     delete_country_db, edit_country_db)
from api.country import Country, CountryEdit
from fastapi import APIRouter


country_router = APIRouter(prefix='/country', tags=['Methods for country'])


@country_router.get('/all-country')
async def get_all_country():
    country = get_all_country_db()
    return country


@country_router.post('/add-country')
async def add_country(data: Country):
    country = add_country_db(**data.model_dump())
    return country


@country_router.get('/country')
async def get_country(country_id: int):
    country = get_country_db(country_id=country_id)
    return country


@country_router.patch('/edit-country')
async def edit_country(data: CountryEdit):
    country = edit_country_db(**data.model_dump())
    return country


@country_router.delete('/delete-country')
async def delete_country(country_id: int):
    country = delete_country_db(country_id=country_id)
    return country









