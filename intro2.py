def add(firstname: str, lastname: str = None):
    if lastname is not None:
        return firstname.capitalize() + " " + lastname.capitalize()
    return firstname.capitalize()


print(add("john"))
