from database.hotelserviice import (add_hotel_db, get_hotel_db, get_hotel_by_country_db,
                                    delete_hotel_db, edit_hotel_db, get_all_hotel_db)
from fastapi import APIRouter
from api.hotel import Hotel, HotelEdit


hotel_router = APIRouter(prefix='/hotel', tags=['Methods for hotel'])


@hotel_router.get('/all-hotel')
async def get_all_hotels():
    hotel = get_all_hotel_db()
    return hotel


@hotel_router.post('/add-hotel')
async def add_hotel(data: Hotel):
    hotel = add_hotel_db(**data.model_dump())
    return hotel


@hotel_router.get('/hotel')
async def get_hotel(hotel_id: int):
    hotel = get_hotel_db(hotel_id=hotel_id)
    return hotel


@hotel_router.get('/hotel-country')
async def get_hotel_by_country(country_id: int):
    hotel = get_hotel_by_country_db(country_id=country_id)
    return hotel


@hotel_router.patch('/hotel-edit')
async def edit_hotel(data: HotelEdit):
    hotel = edit_hotel_db(**data.model_dump())
    return hotel


@hotel_router.delete('/delete-hotel')
async def delete_hotel(hotel_id: int):
    hotel = delete_hotel_db(hotel_id=hotel_id)
    return hotel
















































































