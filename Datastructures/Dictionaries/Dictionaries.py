# Dictionary is also a collection and it not ordered like List
# Dictionary stores value in order of key-value pair
# Defining and creating a dictionary.

dictionary = dict()
dictionary["Vadapav"] = 20
dictionary["Kacchi Dabeli"] = 15
dictionary["Pani Puri"] = 15
print(dictionary)


# Printing all keys and values.
print(dictionary.keys())
print(dictionary.values())

# Two iteration variables, where one is map to key and another is map to value.
for key,value in dictionary.items():
    print(key,value)
    
# Also declare a dictionary.

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)