# If the code try works - the except block is skipped.
# If the code in try fails - it jumps to except section.

greeting = "Hello Shubham"

try:
    greeting = int(greeting)   # As string cannot to converted to Int.
except Exception as error:
    istr = -1
    print(error)                 # Except block is executed.

print(istr)


# This example shows that if try block is executed and there is no exception then else block is executed.
# If except block is executed than else block is not executed.

greeting = 123
istr = 1

try:
    greeting = int(greeting)
except Exception as error:
    istr = -1
    print(error)
else:
    istr = 10

print(istr)     # Prints the value of istr.
