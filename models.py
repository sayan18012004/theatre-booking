try:
    from enum import Enum
    from pydantic import BaseModel
    import json

    from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
    from sqlalchemy.orm import relationship

    from persistence.database import Base


    class User(Base):
        __tablename__ = "users"

        username = Column(String, primary_key=True, index=True)
        password = Column(String)
        type = Column(String)
        gender = Column(String)
        age = Column(Integer)
        preferences = Column(String)

    class Movie(Base):
        __tablename__ = "movies"

        title = Column(String, primary_key=True, index=True)
        genre = Column(String)
        start_time = Column(String)
        end_time = Column(String)
        total_seats = Column(Integer)
        booked_seats = Column(Integer)
        price_1_adult = Column(Integer)
        price_1_child = Column(Integer)
        rating = Column(String)


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


    class ratings(str, Enum):
        G = "G"
        PG = "PG"
        PG_13 = "PG_13"
        R = "R"
        NC_17 = "NC_17"

    class UserCreate(User):
        pass

    



    # class Movie(BaseModel):
    #     title: str
    #     genre: str
    #     start_time: str
    #     end_time: str
    #     total_seats: int
    #     booked_seats: int
    #     price_1_adult: int
    #     price_1_child: int
    #     rating: str



    # class UsersWrapper:
    #     # userDict: dict

    #     def __init__(self):
    #         self.userDict = {}

    #     def putUser(self, user: User):
    #         self.userDict[user.username] = user

    #     def getUser(self, username: str):
    #         return self.userDict.get(username)

    #     def deleteUser(self, username: str):
    #         if username in self.userDict:
    #             del self.userDict[username]

    #     def has_user(self, username: str):
    #         return username in self.userDict

    #     def toJSON(self):
    #         return json.dumps(
    #             self,
    #             default=lambda o: o.__dict__,
    #             sort_keys=True,
    #             indent=4)

    # class MoviesWrapper:

    #     def __init__(self):
    #         self.movieDict = {}

    #     def putMovie(self, movie: Movie):
    #         self.movieDict[movie.title] = movie

    #     def has_movie(self, title: str):
    #         return title in self.movieDict

    #     def toJSON(self):
    #         return json.dumps(
    #             self,
    #             default=lambda o: o.__dict__,
    #             sort_keys=True,
    #             indent=4)
        
except Exception as e:
    print("Error in models.py: ", e)