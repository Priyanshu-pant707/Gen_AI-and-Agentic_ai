# Types Of Inheritance 

#===================


# 1.  single inheritance
# all the inheritance we saw at the file 14 was the single level.


#===================


# Multiple inheritance 
# multiple inheritance means these will be 2 parent classes and only 1 child class and the child class will inherit all the attributes and methods of both parents.
# Note :  the constructor function will be inherited of the first class that has been inherited . This is MRO(method resolution method) followed by python.




class Animal:
    def __init__(self,name):
        self.name=name

class Human:
    def __init__(self,id):
        self.id=id

class Robots(Human,Animal):
    def __init__(self, id):
        super().__init__(id)






#=================== 
# Multilevel inheritance

class BagFactory:
    def __init__(self,material,zips,pockets):
        self.material=material
        self.zips=zips
        self.pockets=pockets
    
    
    def details(self):
        print("Your bag details are ")
        print(self.material)
        print(self.zips)
        print(self.pockets)





class Rebook(BagFactory):
    def __init__(self,material,zips,pockets,color):
        self().__init__(material,zips,pockets)
        self.color=color
    def details(self):
        print(self.color)
        return super().details()
        

class Campus(Rebook):
    def __init__(self, material, zips, pockets, color,size):
        super().__init__(material, zips, pockets, color)
        self.size=size




