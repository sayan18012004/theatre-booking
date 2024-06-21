try:
    import pickle
    import models


    def read_from_file(users_file: str):
        with open(users_file, 'rb') as inp:
            return pickle.load(inp)


    def write_to_file(users_file, usersWrapper: models.UsersWrapper):
        with open(users_file, 'wb') as f:
            pickle.dump(usersWrapper, f, pickle.HIGHEST_PROTOCOL)
except Exception as e:
    print("Error in DataAccessor.py: ", e)