# Accepting arguments in decorator functions.


def decorators_arguments(function):
    def wrapper_arguments(arg1, arg2):
        print("My argumets are: {0}, {1}".format(arg1, arg2))
        function(arg1, arg2)
    return wrapper_arguments


@decorators_arguments
def hobbies(arg1, arg2):
    print("My hobbies are playing {0} and {1}".format(arg1, arg2))


hobbies("Football", "Gaming")