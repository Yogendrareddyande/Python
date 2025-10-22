class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def area(self):
        print(self.l*self.b)
    @staticmethod
    def parimeter(length,breath):
        print(2*length*breath)

a=rectangle(10,5)
a.area() 
rectangle.parimeter(10,5)       