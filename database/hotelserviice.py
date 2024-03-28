from database import get_db
from database.models import Hotels


def get_all_hotel_db():
    db = next(get_db())
    hotels = db.query(Hotels).all()
    return hotels


def add_hotel_db(country_id, hotel_name, cost, address):
    db = next(get_db())
    hotel = Hotels(country_id=country_id, hotel_name=hotel_name, cost=cost, address=address)
    db.add(hotel)
    db.commit()
    return 'Hotel added'


def get_hotel_db(hotel_id):
    db = next(get_db())
    hotel = db.query(Hotels).filter_by(hotel_id=hotel_id).first()
    if hotel:
        return hotel
    else:
        return f'Hotel by {hotel_id} ID not found'


def get_hotel_by_country_db(country_id):
    db = next(get_db())
    hotel = db.query(Hotels).filter_by(country_id=country_id).all()
    if hotel:
        return hotel
    else:
        return f'Hotels by {country_id} ID not found'


def edit_hotel_db(hotel_id, edit, new):
    db = next(get_db())
    hotel = db.query(Hotels).filter_by(hotel_id=hotel_id).first()
    if hotel:
        if edit == 'hotel_name':
            hotel.hotel_name = new
        elif edit == 'cost':
            hotel.cost = new
        elif edit == 'address':
            hotel.address = new
        elif edit == 'country_id':
            hotel.country_id = new
        else:
            return 'Argument not found'
        db.commit()
        return hotel
    else:
        return f'Hotel by {hotel_id} ID not found'


def delete_hotel_db(hotel_id):
    db = next(get_db())
    hotel = db.query(Hotels).filter_by(hotel_id=hotel_id).first()
    if hotel:
        db.delete(hotel)
        db.commit()
        return 'Hotel deleted'
    else:
        return f'Hotel by {hotel_id} ID not found'
