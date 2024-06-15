from better.app.models.user_model import User
from better.app.database.user_database import Database

class UserService:
    @staticmethod
    async def create_user(userObject: User):
        return Database.create_user(userObject)

    @staticmethod
    async def get_users():
        return Database.get_users()

    @staticmethod
    async def get_user(username: str):
        return Database.get_user(username)

    @staticmethod
    async def update_user(username: str, userObject: User):
        return Database.update_user(username, userObject)

    @staticmethod
    async def delete_user(username: str):
        return Database.delete_user(username)