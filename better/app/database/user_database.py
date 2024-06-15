import pickle
from better.app.models.user_model import User, UsersWrapper

class Database:
    @staticmethod
    def create_user(userObject: User):
        usersWrapper = Database._load_users()
        if usersWrapper.has_user(userObject.username):
            return "User already exists"
        else:
            usersWrapper.putUser(userObject)
            Database._save_users(usersWrapper)
            return "user created successfully"

    @staticmethod
    def get_users():
        usersWrapper = Database._load_users()
        return usersWrapper

    @staticmethod
    def get_user(username: str):
        usersWrapper = Database._load_users()
        if usersWrapper.has_user(username):
            return usersWrapper.getUser(username)
        else:
            return "User not found"

    @staticmethod
    def update_user(username: str, userObject: User):
        usersWrapper = Database._load_users()
        if usersWrapper.has_user(username):
            usersWrapper.putUser(userObject)
            Database._save_users(usersWrapper)
            return "User updated successfully"
        else:
            return "User not found"

    @staticmethod
    def delete_user(username: str):
        usersWrapper = Database._load_users()
        if usersWrapper.has_user(username):
            usersWrapper.deleteUser(username)
            Database._save_users(usersWrapper)
            return "User deleted successfully"
        else:
            return "User not found"

    @staticmethod
    def _load_users():
        with open('users.pkl', 'rb') as inp:
            return pickle.load(inp)

    @staticmethod
    def _save_users(usersWrapper):
        with open("users.pkl", 'wb') as f:
            pickle.dump(usersWrapper, f, pickle.HIGHEST_PROTOCOL)