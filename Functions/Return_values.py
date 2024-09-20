# How to return a value.

# Return a single value.
def addition(num1, num2):
    return num1 + num2


print(addition(5, 10))

# Returning multiple return values.


def add_n_multiply(num1, num2):
    return num1+num2, num1*num2


add, multiply = add_n_multiply(20, 10)
print("Addition of two numbers:", add)
print("Multiplication of two numbers:", multiply)


# Returning multiple values using list.


def name_n_age():
    name = "Shubham"
    age = 24
    return [name, age]


list = name_n_age()
print(list)
