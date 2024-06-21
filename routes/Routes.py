try:
    from fastapi import APIRouter
    import models
    from services.Services import *

    router = APIRouter()

    try:
        @router.get("/")
        async def startup():
            return "Server is up and running"
        
    except Exception as e:
        print("Error in startup in Routes.py: ", e)

    try:
        @router.post("/create_user")
        async def createUser(userObject: models.User):
            service_response = create_user(userObject)
            return service_response
        
    except Exception as e:
        print("Error in createUser in Routes.py: ", e)

    try:
        @router.get("/get_users")
        async def get_users():
            return usersWrapper
        
    except Exception as e:
        print("Error in get_users in Routes.py: ", e)

    try:
        @router.get("/get_user/")
        async def get_user(username: str):
            return get_particular_user(username)
        
    except Exception as e:
        print("Error in get_user in Routes.py: ", e)

    try:
        @router.put("/update_user/")
        async def update_user(username: str, userObject: models.User):
            service_response = update_user(username, userObject)
            return service_response
        
    except Exception as e:
        print("Error in update_user in Routes.py: ", e)

    try:
        @router.delete("/delete_user/")
        async def delete_user(username: str):
            service_response = delete_user(username)
            return service_response
        
    except Exception as e:
        print("Error in delete_user in Routes.py: ", e)

    try:
        @router.post("/create_movie")
        async def createMovie(movieObject: models.Movie):
            service_response = create_movie(movieObject)
            return service_response
        
    except Exception as e:
        print("Error in createMovie in Routes.py: ", e)

    try:
        @router.get("/get_movies")
        async def get_movies():
            return moviesWrapper
    
    except Exception as e:
        print("Error in get_movies in Routes.py: ", e)

    try:    
        @router.post("/add_movie")
        async def createMovie(movieObject: models.Movie):
            service_response = create_movie(movieObject)
            return service_response
        
    except Exception as e:
        print("Error in add_movie in Routes.py: ", e)

except Exception as e:
    print("Error in Routes.py: ", e)