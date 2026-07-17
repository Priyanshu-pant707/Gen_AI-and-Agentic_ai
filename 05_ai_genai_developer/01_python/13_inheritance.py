# inheritance :
# in general terms inheritance  means property or any possession that comes to an heir.

# benefits of using inheritance is  : 1. Code reusability ,  2. organized structure  , 3. easy to maintain and extend .



class Animal:  # parent class
    def __init__(self,name):
        self.name=name
    
    def details(self):
        print(f"hello your name is {self.name}")

class Humans(Animal):  # child class
    pass



# you child class objects has all the powers to access the attributes and methods of parent class
obj=  Humans("priyanshu")
obj.details()



