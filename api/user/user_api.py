from database.userservice import (get_all_user_db, get_user_db, add_user_db, edit_user_db,
                                  delete_user_db, add_status_user_db)
from fastapi import APIRouter
from api.user import User, UserEdit


user_router = APIRouter(prefix='/user', tags=['Methods for users'])


@user_router.get('/all-user')
async def get_all_user():
    users = get_all_user_db()
    return users


@user_router.post('user-regist')
async def user_regist(data: User):
    user = add_user_db(**data.model_dump())
    return user


@user_router.get('/get-user')
async def get_user(user_id: int):
    user = get_user_db(user_id=user_id)
    return user


@user_router.patch('/edit-user')
async def edit_user(data: UserEdit):
    user = edit_user_db(**data.model_dump())
    return user


@user_router.post('add-status-user')
async def add_status(user_id: int, status_id: int):
    user = add_status_user_db(user_id=user_id, status_id=status_id)
    return user


@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    user = delete_user_db(user_id=user_id)
    return user