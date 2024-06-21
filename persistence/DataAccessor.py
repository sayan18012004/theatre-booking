try:
    import pickle, os, models


    try:
        def read_from_file(input_file: str):
            if os.path.getsize(input_file) == 0:
                return models.UsersWrapper() if 'users' in input_file else models.MoviesWrapper()
            else:
                with open(input_file, 'rb') as inp:
                    return pickle.load(inp)
    
    except Exception as e:
        print("Error in read_from_file from DataAccessor.py: ", e)

    try:
        def write_to_file(input_file: str, givenWrapper):
            with open(input_file, 'wb') as f:
                pickle.dump(givenWrapper, f, pickle.HIGHEST_PROTOCOL)
    
    except Exception as e:
        print("Error in write_to_file from DataAccessor.py: ", e)

except Exception as e:
    print("Error in DataAccessor.py: ", e)