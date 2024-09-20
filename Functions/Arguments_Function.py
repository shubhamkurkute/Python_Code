# Argument is variable used while calling a funtion.

# Single Argument


def my_arg_function(fname):     # Here variable fname is parameter.
    print("Hello", fname)


my_arg_function("Shubham")      # Passing a single argument string to function.

# Passing number of arguments.


def my_name(fname, lname):
    print(fname+' '+lname)


my_name("Shubham", "Kurkute")

# Passing arbitrary arguments.


def play_game(*games):
    print("I will play %s today" % games[1])


play_game("Volleyball", "Football", "Cricket")

# Keyword Argument


def my_skills(lang1, lang2, lang3):
    print("My skills are:", lang1, lang2, lang3)


my_skills(lang1="Python", lang2="C++", lang3="Java")

# Arbitrary keyword arguments.


def my_fullname(**fullname):
    print("His name is:", fullname["fname"])
    

my_fullname(fname="Shubham", lname="Kurkute")

# Default parameter argument
# In this by default parameter is used if function call is without argument.


def my_food(food="Biryani"):
    print("Today I will eat :", food)


my_food("Chinese")      # As argument is passed default parameter is not used.
my_food()               # Uses default parameter i.e. Biryani as no argument is passed.

# Passing list as an argument.


def my_car_list(cars):
    for car in cars:
        print(car)


car_list = ["XUV 700", "Lexus", "BMW M5", "Porche 911 GT"]
my_car_list(car_list)
