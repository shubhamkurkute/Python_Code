# Inheritance without _init__ method inside derived class.

class ParentClass:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def full_name(self):
        print(f"Full name is {self.fname} {self.lname}")
    

class ChildClass(ParentClass):
    pass


child = ChildClass("Shubham", "Kurkute")
child.full_name()

# Inheritance using __init__ method inside the derived class


class ParentClassInit:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def full_name(self):
        print(f"Full name is {self.fname} {self.lname}")
    

class ChildClassInit(ParentClass):
    def __init__(self, fname, lname, pass_year):
        super().__init__(fname, lname)
        self.pass_year = pass_year

    
    def full_info(self):
        print(f"I am {self.fname} {self.lname} passot year {self.pass_year} ")

    
child_init = ChildClassInit("Shubham", "Kurkute", 2019)
child_init.full_info()

