from database import get_db
from database.models import Sights


def get_all_sights_db():
    db = next(get_db())
    sights = db.query(Sights).all()
    return sights


def add_sights_db(country_id, sight_name, sight_info, sight_address):
    db = next(get_db())
    sight = Sights(country_id=country_id, sight_name=sight_name, sight_info=sight_info, sight_address=sight_address)
    db.add(sight)
    db.commit()
    return 'Sight added'


def get_sight_db(sight_id):
    db = next(get_db())
    sight = db.query(Sights).filter_by(sight_id=sight_id).first()
    if sight:
        return sight
    else:
        return f'Sight by {sight_id} ID not found'


def get_sight_by_country_db(country_id):
    db = next(get_db())
    sight = db.query(Sights).filter_by(country_id=country_id).all()
    if sight:
        return sight
    else:
        return f'Sights by {country_id} ID not found'


def edit_sight_db(sight_id, edit, new):
    db = next(get_db())
    sight = db.query(Sights).filter_by(sight_id=sight_id).first()
    if sight:
        if edit == 'sight_name':
            sight.sight_name = new
        elif edit == 'sight_info':
            sight.sight_info = new
        elif edit == 'sight_address':
            sight.sight_address = new
        elif edit == 'country_id':
            sight.country_id = new
        else:
            return 'Argument not found'
        db.commit()
        return 'Sight changed'
    else:
        return f'Sight by {sight_id} ID not found'


def delete_sight_db(sight_id):
    db = next(get_db())
    sight = db.query(Sights).filter_by(sight_id=sight_id).first()
    if sight:
        db.delete(sight)
        db.commit()
        return 'Sight deleted'
    else:
        return f'Sight by {sight_id} ID not found'










































































