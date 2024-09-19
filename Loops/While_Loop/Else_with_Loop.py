# Like conditionals loops can also use else condition.
# This else condition only executes if loop becomes false and doesnt executes when loop is breaked in middle.


# This example shows how to else executes for while loop after condition becomes false.
i = 1
while i < 3:
    print("Inside Loop", i)
    i += 1

else:
    print("Inside else")

# If loop is exited by using break else doesnt execute.
# After printing first value i.e. 1 loop is breaked as if condition becomes true and breaks the loop and hence else block is not executed.
num = 1
while num < 4:
    if (num % 2 == 0):
        break
    print("Inside Loop", num)
    num += 1
else:
    print("Inside else")
print("Outside loop and else")

