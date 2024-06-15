import pickle
import models

FILE_NAME = 'users.pkl'


def read_from_file():
    with open(FILE_NAME, 'rb') as inp:
        return pickle.load(inp)


def write_to_file(usersWrapper: models.UsersWrapper):
    with open(FILE_NAME, 'wb') as f:
        pickle.dump(usersWrapper, f, pickle.HIGHEST_PROTOCOL)