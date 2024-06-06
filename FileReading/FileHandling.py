# To open a file we use open() function which just opens the file.
# Open file function contains arguments open(filename,mode) to read file we use 'r' and 'w' to write the file.
# But mode are optional.
# open function return the handle to manipulate the file.
# Use a special character for newline to indicate represented as "\n" and is one character not two.


fhand = open("FileReading\\file.txt")

for line in fhand:   # As file contains sequence of string we use for loop to print the lines

    print(line)      # Each line is a sequence

# We can use read() to read whole file as a single string including newlines.

content  = fhand.read()
print(content)