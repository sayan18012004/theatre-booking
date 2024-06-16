import pickle
import models

FILE_NAME = 'users.pkl'
FILE_NAME2 = 'movies.pkl'

def read_from_file():
    with open(FILE_NAME, 'rb') as inp:
        return pickle.load(inp)


def write_to_file(usersWrapper: models.UsersWrapper):
    with open(FILE_NAME, 'wb') as f:
        pickle.dump(usersWrapper, f, pickle.HIGHEST_PROTOCOL)
#
# def read_from_file2():
#     with open(FILE_NAME2, 'rb') as f:
#         return pickle.load(f)
#
#
# def write_to_file2(moviesWrapper: models.MoviesWrapper):
#     with open(FILE_NAME2, 'wb') as f2:
#         pickle.dump(moviesWrapper, f2, pickle.HIGHEST_PROTOCOL)
