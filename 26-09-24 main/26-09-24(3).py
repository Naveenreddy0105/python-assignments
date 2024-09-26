'''3.Create a class Rectangle that has instance variables length and width. 
  Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
  Exercise:
    >Create instances of the Rectangle class with different lengths and widths.
    >Calculate and print the area for each rectangle.
'''

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_area(self):
        area_length=self.length
        area_width=self.width
        area=area_length*area_width
        print(f"Rectangle Area:{area}square units")
      
rect1=Rectangle(2,3)
rect2=Rectangle(10,20)
rect3=Rectangle(5,15)
       
print("Rectangle 1(2*3):")
rect1.calculate_area()
print("Rectangle 2(10*20):")
rect2.calculate_area()
print("Rectangle 3(5*15):")
rect3.calculate_area()