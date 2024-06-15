from fastapi import APIRouter

from services.Services import *

router = APIRouter()


@router.post("/create_user")
async def createUser(userObject: models.User):
    service_response = create_user(userObject)
    return service_response


@router.get("/get_users")
async def get_users():
    return usersWrapper


@router.get("/get_user/")
async def get_user(username: str):
    return get_particular_user(username)


@router.put("/update_user/")
async def update_user(username: str, userObject: models.User):
    service_response = update_user(username, userObject)
    return service_response


@router.delete("/delete_user/")
async def delete_user(username: str):
    service_response = delete_user(username)
    return service_response
