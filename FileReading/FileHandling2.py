# Functions to find some line which starts with certain strings.
# startswith(string) function is used to find the line that starts with certain string. This string is argument for the function. 
#rstrip() function is used to ignore the nextline so as the lines doesnt contain any space in between and print lines continously.

try:
    file = open("FileReading\\fil.txt")
    print("File readed succesfully")
except:
    print("Error file reading")
    quit()

    
for line in file:
    line = line.rstrip()
    if line.startswith("Python"):
        print(line)
