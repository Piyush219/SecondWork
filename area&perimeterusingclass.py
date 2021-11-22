class triangle:
    def __init__(self,a,b,c):
        print("This is default")
        self.a=a
        self.b=b
        self.c=c
        
    
        
    def calculate_area(self):
        print(1/2*(self.a*self.b))
        #return area
        
    def calculate_perimeter(self):
        print (self.a+self.b+self.c)


    
defaultconst=triangle(0,0,0)       
paraconst=triangle(3,4,5)
defaultconst.calculate_area()
defaultconst.calculate_perimeter()
paraconst.calculate_area()
paraconst.calculate_perimeter()



#perimeter=triangle()
#perimeter=triangle(3,4,5)


#triangle.calculate_area(area)
#triangle.calculate_perimeter(perimeter)
#area.calculate_area()
#perimeter.calculate_perimeter()

