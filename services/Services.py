try:
    from persistence.DataAccessor import *
    from models import *

    try:
        users_file = 'users.pkl'
        movies_file = 'movies.pkl'
        usersWrapper = read_from_file(users_file)
        moviesWrapper = read_from_file(movies_file)

    except Exception as e:
        print("Error initiating variable from Services.py: ", e)

    try:
        def create_user(userObject: User):
            if usersWrapper.has_user(userObject.username):
                return "User already exists"
            else:
                usersWrapper.putUser(userObject)

            write_to_file(users_file, usersWrapper)

            return "user created successfully"
    
    except Exception as e:
        print("Error in create_user from Services.py: ", e)


    try:
        def get_particular_user(username: str):
            if usersWrapper.has_user(username):
                return usersWrapper.getUser(username)
            else:
                return "User not found"

    except Exception as e:
        print("Error in get_particular_user from Services.py: ", e)

    try:
        def update_user(username: str, userObject: User):
            if usersWrapper.has_user(username):
                usersWrapper.putUser(userObject)

                write_to_file(users_file, usersWrapper)

                return "User updated successfully"
            else:
                return "User not found"
    except Exception as e:
        print("Error in update_user from Services.py: ", e)

    try:
        def delete_user(username: str):
            if usersWrapper.has_user(username):
                usersWrapper.deleteUser(username)

                write_to_file(users_file, usersWrapper)

                return "User deleted successfully"
            else:
                return "User not found"
    except Exception as e:
        print("Error in delete_user from Services.py: ", e)

    try:
        def create_movie(movieObject: Movie):
            if moviesWrapper.has_movie(movieObject.title):
                return "Movie already exists"
            else:
                moviesWrapper.putMovie(movieObject)

            write_to_file(movies_file, moviesWrapper)

            return "Movie created successfully"
        
    except Exception as e:
        print("Error in create_movie from Services.py: ", e)

except Exception as e:
    print("Error in Services.py: ", e)