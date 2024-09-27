# Accessing dictionary in various methods.


car_dict = {
    "Car": "911 GT",
    "Brand": "Porsche",
    "Model": "2012" 
}

# Accessing value through key.
carName = car_dict.get("Car")
print(carName)

# To print whole dictionary along with key and values.
print(car_dict.items())

# Changing the value using a key.
car_dict["Model"] = "2020"
print(car_dict.items())

# Can use update method to change the value.
car_dict.update({"Model": "2022"})
print(car_dict.items())
