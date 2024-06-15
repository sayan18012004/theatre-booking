from enum import Enum
from pydantic import BaseModel
import json

class USER_TYPE(str, Enum):
    ADMIN = "ADMIN"
    REGULAR = "REGULAR"

class GENDER(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class User(BaseModel):
    username: str
    password: str
    type: USER_TYPE
    gender: GENDER
    age: int
    preferences: str

class UsersWrapper:
    def __init__(self):
        self.userDict = {}

    def putUser(self, user: User):
        self.userDict[user.username] = user

    def getUser(self, username: str):
        return self.userDict.get(username)

    def deleteUser(self, username: str):
        if username in self.userDict:
            del self.userDict[username]

    def has_user(self, username: str):
        return username in self.userDict

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)