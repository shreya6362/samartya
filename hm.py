class car():
    def __init__(self,name,brand,color):
        self.name=name
        self.brand=brand
        self.color=color
    def myfunc(self):
        print(f" My car name is {self.name} and brand is {self.brand} also color is {self.color}")
    def __str__(self):
        return "name:"+ self.name+", brand:"+str(self.brand)+",color:"+str(self.color)
A=car("CCC","Benz","red")
A.myfunc()
print(A)