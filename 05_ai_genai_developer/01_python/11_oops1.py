# classes
# - a class is a blue print for creating a object
# object - an instance of a class



# encapsulation :  in programming , encapsulation is about keeping some information safe and only letting it be changed for looked at in specific ways.
# polymorphism : polymorphism is the ability of a function or method to work in different ways depending on the object it is acting upon.
# inheritance :  when one class inherits some features from another class this phenomena is known as inheritance .
# abstraction :  when we only see the essential part of our code and hides the rest is the process of abstraction.




# creating class -------
class Car:
    a=12  # attribute
    
    def hello(self):
        print(self.a)

# print(Car.a)  # accessing attribute without creating object
# print(Car.hello)  # accessing method without creating object




# object creation ------
# example :
# bag factory  ->  requirements -> 1. material, 2. zips,  3.pockets

class Bag:
    def __init__(self, material, zips, pockets):  # dunder init method is used to initialize the object
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def display(self):
        print(f"Material: {self.material}, Zips: {self.zips}, Pockets: {self.pockets}")

nike =  Bag("Leather", 2, 3)  #object 1
adidas = Bag("Canvas", 1, 2)  # object 2
nike.display()
adidas.display()



