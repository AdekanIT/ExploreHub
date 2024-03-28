from database import get_db
from database.models import Country


def get_all_country_db():
    db = next(get_db())
    country = db.query(Country).all()
    return country


def add_country_db(country_name):
    db = next(get_db())
    country = Country(country_name=country_name)
    db.add(country)
    db.commit()
    return 'Country added'


def get_country_db(country_id):
    db = next(get_db())
    country = db.query(Country).filter_by(country_id=country_id).first()
    if country:
        return country
    else:
        return f'Country by {country_id} ID not found'


def edit_country_db(country_id, edit, new):
    db = next(get_db())
    country = db.query(Country).filter_by(country_id=country_id).first()
    if country:
        if edit == 'country_name':
            country.country_name = new
        else:
            return 'Argument not found'
        db.commit()
        return country
    else:
        return f'Country by {country_id} ID not found'


def delete_country_db(country_id):
    db = next(get_db())
    country = db.query(Country).filter_by(country_id=country_id).first()
    if country:
        db.delete(country)
        db.commit()
        return 'Country deleted'
    else:
        return f'Country by {country_id} ID not found'

















































