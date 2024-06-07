# Collection allows you to put many values in single variable.
# List is a kind of collection.
# A list element can be any python object.
# A list can be empty.
# List are mutable unlike strings which are immutable


friends=["Raj","Abhishek","Dharma","Prathmesh","Bhalya"]
# List are mutable i.e. we can change an element of a list using the index operator.
friends[4] = "Rohan"

# List and definite loop best way.
for friend in friends:
    print(friend)
print("All are welcome")

# This allows to traverse through index.
for i in range(len(friends)):
    print(friends[i])




