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


bag1= BagFactory("lather",3,4)


class Rebook(BagFactory):
    def __init__(self,material,zips,pockets,color):
        self().__init__(material,zips,pockets)
        self.color=color
    def details(self):
        print(self.color)
        return super().details()
        

bag2= Rebook("polyster",4,2,"red")




