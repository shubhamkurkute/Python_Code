# A decorator is a design pattern that lets you add new functionality to an existing object without modifying it s structure.
# Decorators are typically applied to functions.

# Assigning function to a variable.

def plus_one(number):
    return number + 1

add_one = plus_one


print(add_one(4))


# Defining function inside a function.
def one_add(number):
    def add_one(number):
        return number + 1
    result = add_one(number)
    return result

print(one_add(4))


#  Passing Functions as Arguments to other Functions
def plus_one(number):
    return number + 1


def function_call(function):
    number_to_add = 5
    return function(number_to_add)


function_call(plus_one)


# Functions Returning other Functions
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi


hello = hello_function()
hello()
