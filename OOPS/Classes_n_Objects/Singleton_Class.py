class Singleton(object):
    _instance = None
    _car = "Ferrari"
    def __new__(Singleton):
        if Singleton._instance is None:
            Singleton._instance =  super().__new__(Singleton)
        return Singleton._instance
    
    def car(self):
        print(self._car)
    


first  = Singleton()
first._car = "Lamborgini"
first.car()
second  = Singleton()
second.car()

