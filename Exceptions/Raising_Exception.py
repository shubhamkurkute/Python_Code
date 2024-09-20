# Raising a exception if condition is false.
# This can be done using raise and assert keywords.


# Using a raise keyword.
i = 5

# if i > 10:
#     print("In else")
# else:
#     raise Exception(f"Number cannot be greater than ({i=})")


# Using a assert keyword

assert (i > 10), f"Number cannot be greater than ({i=})"
print(i)
