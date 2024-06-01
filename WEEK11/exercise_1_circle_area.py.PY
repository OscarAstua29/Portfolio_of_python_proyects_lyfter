class Circle:
    
    def get_area(self, radius):
        area= 3.14 *(radius*radius)
        return area
    
circle = Circle()

print(circle.get_area(4))