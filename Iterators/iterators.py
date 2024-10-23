# Iterators are methods that iterate collections like lists, tuples, etc.
# Using an iterator method, we can loop through an object and return its elements.
# Technically, a Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

# define a list
my_list = [4, 7, 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0