# A lambda function is a small anonymous function.
# A lambda function  can take any number of arguments but can only one expression.


x = lambda a: a*10
print(x(10))

# Why use lambda function.
# The power lambda is better shown when used inside a function as a anonymous function.


def my_function(n):
    return lambda a: a*n


doubler = my_function(2)
print(doubler(10))
