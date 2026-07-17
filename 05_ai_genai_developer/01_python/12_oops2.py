# type of methods


class Animal:
    a=12
    
    def __init__(self,name):
        self.name=name  
        
    def hello(self):  
        print(f"Hello , I am {self.name}")
    
    @classmethod   # decorator  -> class method
    def details(cls):
        print("This is a class method")
    
    @staticmethod  # decorator  -> static method, it will not target any location in the class, it will not take any parameter
    def info():
        print("This is a static method")


obj = Animal("Dog")
obj.hello()
obj.details()  # calling class method using object
Animal.details()  # calling class method using class name