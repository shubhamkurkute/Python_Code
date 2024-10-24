# Creating a upper case decorator.

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator        # Allows to use decorator
def say_hi():
    return 'hello there'

print(say_hi())
