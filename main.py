from fastapi import FastAPI
import uvicorn
import models
import os
import json


# JSON Encoder to handle custom objects
# class UserEncoder(json.JSONEncoder):
#     class UserEncoder(json.JSONEncoder):
#         def default(self, o):
#             if isinstance(o, models):
#                 return o.dict()
#             return super().default(o)


# Create a FastAPI instance
app = FastAPI()

# Create a dictionary to store user data

usersWrapper = models.UsersWrapper()

# userDict = {}

# newUserDict = {}
newMovieDict = {}

# Check if the file is empty or not then load the data

with open('users.txt') as f:
    data = f.read()
    usersWrapper = json.loads(data)

# if os.stat('data.json').st_size != 0:
#     with open('data.json', 'r') as json_data:
#         userDict = json.load(json_data)

# if os.stat('movies.json').st_size != 0:
#     with open('movies.json', 'r') as json_movies:
#         allMoviesData = json.load(json_movies)
# else:
#     allMoviesData = newMovieDict


# Creating End-points
@app.post("/create_user")
async def create_user(userObject: models.User):

    print(usersWrapper)
    # object_methods = [method_name for method_name in dir(usersWrapper)
    #                   if callable(getattr(object, method_name))]
    # print(object_methods)

    if usersWrapper.has_user(userObject.username):
        return "User already exists"
    else:
        usersWrapper.putUser(userObject)

    with open("users.txt", 'w') as f:
        f.write(usersWrapper.toJSON())

    # with open('data.json', 'w') as json_data:
    #     json.dump({k: v.dict() for k, v in userDict.items()}, json_data, cls=UserEncoder, indent=4)

    # if os.stat('data.json').st_size != 0:
    #     with open('data.json', 'r') as json_data:
    #         allUsersData = json.load(json_data)

    return "user created successfully";


@app.get("/get_users")
async def get_users():
    return usersWrapper


@app.get("/get_user/")
async def get_user(username: str):
    if usersWrapper.has_user(username):
        return usersWrapper.getUser(username)
    else:
        return "User not found"


@app.put("/update_user/")
async def update_user(username: str, userObject: models.User):
    if usersWrapper.has_user(username):
        usersWrapper.putUser(userObject)

        with open("users.txt", 'w') as f:
            f.write(usersWrapper.toJSON())

        # with open('data.json', 'w') as json_data:
        #     json.dump({}, json_data, cls=UserEncoder, indent=4)
        #
        # with open('data.json', 'w') as json_data:
        #     json.dump({k: v.dict() for k, v in userDict.items()}, json_data, cls=UserEncoder, indent=4)
        return "User updated successfully"
    else:
        return "User not found"


@app.delete("/delete_user/")
async def delete_user(username: str):
    if usersWrapper.has_user(username):
        usersWrapper.deleteUser(username)

        with open("users.txt", 'w') as f:
            f.write(usersWrapper.toJSON())

        return "User deleted successfully"
    else:
        return "User not found"


# @app.post("/add_movie")
# async def add_movie(movieObject: models.movies):
#     if movieObject.title in newMovieDict:
#         return "Movie already exists"
#     else:
#         newMovieDict[movieObject.title] = movieObject
#     with open('movies.json', 'w') as json_movies:
#         json.dump({k: v.dict() for k, v in newMovieDict.items()}, json_movies, cls=UserEncoder, indent=4)
#
#     return "Movie Added"
#
#
# @app.get("/get_movies")
# async def get_movies():
#     return userDict


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
