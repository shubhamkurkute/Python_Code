# Example for is operator and == operator
# As is also checks the type of datatype it is stronger than == operator
# == operator doesnt check datatype of variable and only compares the value of variable.

dot = 2.0
num =2
if num is dot:
    print("Float and integer are same for is keyword")
elif(num==dot):
    print("Float and integer are same for == operator")

