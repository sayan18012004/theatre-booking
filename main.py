import pickle
import uvicorn
from fastapi import FastAPI

import models

app = FastAPI()

# Create a dictionary to store user data

usersWrapper = models.UsersWrapper()
with open('users.pkl', 'rb') as inp:
    usersWrapper = pickle.load(inp)

# newMovieDict = {}


# Creating End-points
@app.post("/create_user")
async def create_user(userObject: models.User):
    if usersWrapper.has_user(userObject.username):
        return "User already exists"
    else:
        usersWrapper.putUser(userObject)

    with open("users.pkl", 'wb') as f:
        pickle.dump(usersWrapper, f, pickle.HIGHEST_PROTOCOL)

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

        with open("users.pkl", 'wb') as f:
            pickle.dump(usersWrapper, f, pickle.HIGHEST_PROTOCOL)

        return "User updated successfully"
    else:
        return "User not found"


@app.delete("/delete_user/")
async def delete_user(username: str):
    if usersWrapper.has_user(username):
        usersWrapper.deleteUser(username)

        with open("users.pkl", 'wb') as f:
            pickle.dump(usersWrapper, f, pickle.HIGHEST_PROTOCOL)

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
