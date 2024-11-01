# List comprehension provides shorter syntax.
# Syntax for list: newlist = [expression for item in iterable if condition == True]

# This is long method to create a list
matrix = []

for i in range(3):
    matrix.append()
    for j in range(4):
        matrix[i].append(1)

# With the help of list comprehension we can do it in single line.
fruits = ["apple", "mango", "banana", "chicku"]
newlist = [x for x in fruits if 'a' in x]
print(newlist)
