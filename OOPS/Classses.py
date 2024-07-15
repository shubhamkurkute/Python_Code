# Simple class creation.
# __init__ is a functio to define attributes that class must posses.
# In other languages __init__ is constructor.
# Dunder methods are used to customize classes.This are identified by beginning of double underscores.




class Car:
    def __init__(self,company,name,price):
        self.name = name
        self.price = price
        self.company = company

    def car_description(self):
        return f"{self.company} {self.name} cost at {self.price}"
    
    def __str__(self):
        return f"{self.company} {self.name} cost at {self.price}"

    


bentley = Car("Bentley","GT",100000000)
porsche = Car("Porsche","911gt",35000000)
print(bentley.car_description())
print(porsche.car_description())

# Dunder methods help to print description of object rather showing object address.
print(bentley)
print(porsche)


