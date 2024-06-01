from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter

    def calculate_area(self):
        area = 3.14 * (self.radius ** 2)
        return area

class Square (Shape):

    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        perimeter = 4 * self.side_length
        return perimeter

    def calculate_area(self):
        area = self.side_length ** 2
        return area

class Rectangle (Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def calculate_area(self):
        area = self.length * self.width
        return area


circle = Circle(5)
print("Circle Perimeter:", circle.calculate_perimeter())
print("Circle Area:", circle.calculate_area())

square = Square(4)
print("Square Perimeter:", square.calculate_perimeter())
print("Square Area:", square.calculate_area())

rectangle = Rectangle(3, 5)
print("Rectangle Perimeter:", rectangle.calculate_perimeter())
print("Rectangle Area:", rectangle.calculate_area())