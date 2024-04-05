from database import get_db
from database.models import Status


def get_all_status_db():
    db = next(get_db())
    status = db.query(Status).all()
    return status


def add_status_db(status_name, cost):
    db = next(get_db())
    status = Status(status_name=status_name, cost=cost)
    db.add(status)
    db.commit()
    return 'Status added'


def edit_status_db(status_id, edit, new):
    db = next(get_db())
    status = db.query(Status).filter_by(status_id=status_id).first()
    if status:
        if edit == 'status_name':
            status.status_name = new
        elif edit == 'cost':
            status.cost = new
        else:
            return 'Argument not found!'
        db.commit()
        return status
    else:
        return f'Status by {status_id} not found!'


def delete_status_db(status_id):
    db = next(get_db())
    status = db.query(Status).filter_by(status_id=status_id).first()
    if status:
        db.delete(status)
        return 'Status deleted'
    else:
        return f'Status by {status_id} not found!'









































































