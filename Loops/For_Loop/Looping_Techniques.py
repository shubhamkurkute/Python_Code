# Looping techniques are used for loops.

#  Way 1: Using Enumerate()
# Enumerate is used to loop through the containers printing the index number along with the value.

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)       # Prints index and value of the component in container.

# Way 2: Using zip()
# zip() is used to combine 2 or more containers printing the values sequentially. 
# The loop exists only till the smaller container ends.

names = ['Deep', 'Sachin', 'Simran']  # list
ages = (24, 27)           # tuple
for name, age in zip(names, ages):
    print('Name: ', name)
    print('Age: ', age)
    print()

#  Way 3: Using items()
#  Used to read dictionary as it contains key value pair.

d = {"geeks": "for", "only": "geeks"}
# using items to print the dictionary key-value pair
print("The key value pair using items is : ")
for i, j in d.items():
    print(i, j)
