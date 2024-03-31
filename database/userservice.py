from database import get_db
from database.models import User
from datetime import datetime


def get_all_user_db():
    db = next(get_db())
    users = db.query(User).all()
    return users


def add_user_db(fname, lname, email, tellNo):
    db = next(get_db())
    user = User(fname=fname, lname=lname, email=email, tellNo=tellNo, reg_date=datetime.now())
    db.add(user)
    db.commit()
    return 'User added'


def get_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        return user
    else:
        return f'User by {user_id} ID not found'


def edit_user_db(user_id, edit, new):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        if edit == 'fname':
            user.fname = new
        elif edit == 'lname':
            user.lname = new
        elif edit == 'tellNo':
            user.tellNo = new
        elif edit == 'email':
            user.email = new
        else:
            return 'Argument not found'
        db.commit()
        return user
    else:
        return f'User by {user_id} ID not found'


def add_status_user_db(user_id, status_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        user.status_id = status_id
        db.commit()
        return user
    else:
        return f'User by {user_id} ID not found'


def delete_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return 'User deleted'
    else:
        return f'User by {user_id} ID not found'























































