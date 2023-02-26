class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("Area:",self.length*self.breadth)
    def perimeter(self):
        print("Perimeter:",2*(self.length+self.breadth))
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
rect1=rectangle(l,b)
rect1.area()
rect1.perimeter()
