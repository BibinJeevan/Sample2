class coordinates:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,obj):
        return(self.x+obj.x,self.y+obj.y)
obj1=coordinates(35,16)
obj2=coordinates(15,14)
print("Sum=",obj1+obj2)
