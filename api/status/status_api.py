from database.statusservice import add_status_db, edit_status, delete_status_db, get_all_status_db
from fastapi import APIRouter
from api.status import Status, StatusEdit


status_router = APIRouter(prefix='/status', tags=['Methods for status'])


@status_router.get('/all-status')
async def get_all_status():
    user = get_all_status_db()
    return user


@status_router.post('/add-status')
async def add_status(status_name, cost):
    status = add_status_db(status_name=status_name, cost=cost)
    return status


@status_router.patch('/edit-status')
async def edit_status(data: StatusEdit):
    status = edit_status(**data.model_dump())
    return status


@status_router.delete('/delete-status')
async def delete_status(status_id: int):
    status = delete_status_db(status_id)
    return status



























































