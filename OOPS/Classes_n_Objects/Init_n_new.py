# Process of how object is created i.e. instantiated and initialized.
# __new__() is used to create and returns new empty object.
# __init__() initializes the object.
class Car:

    model = "Porsche"
 # cls is nothing but convention for class in our case it is Car.
 # *args and **kwargs is to accept number of parameters.
    def __new__(cls,*args,**kwargs):
        # Here super calls to object class i.e. parent class of all classes.
        # Object class takes only single parameter if you give multiple it throws errror.    
        instance = super().__new__(cls)    
         
        return instance
    def __init__(self,name):
        self.name = name
        


def main(): 
    car = Car()
    print(car.name)
    print(car.model)


if __name__ == "__main__":
    main()

