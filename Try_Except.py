# If the code try works - the except block is skipped.
# If the code in try fails - it jumps to except section.

greeting = "Hello Shubham"

try:
    greeting = int(greeting)   #As string cannot to converted to Int.

except:
    istr = -1                   # Except block is executed.

print(istr);

greeting = 123
istr = 1

try:
    greeting = int(greeting)
except:
    istr = -1

print(istr)
