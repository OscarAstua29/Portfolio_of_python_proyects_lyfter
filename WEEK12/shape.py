from abc import ABC, abstractmethod
import os

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter (self,):
        pass
        
    @abstractmethod     
    def calculate_area(self,):
        pass

    def data(self,):
        pass



class Circle(Shape):

    def data(self,):
        self.radio = int(input('ENTER DE RADIO:'))

    def calculate_perimeter (self,):      
        perimeter= 2*3.14*self.radio
        print(f'Perimeter: {perimeter}')

    def calculate_area(self,):
        area= 3.14 * self.radio**2
        print(f'Area: {area}')

class Square(Shape):
    def data(self,):
        self.side = int(input('ENTER THE SIDE:'))

    def calculate_perimeter (self,):
        perimeter= self.side**2
        print(f'Perimeter: {perimeter}')

    def calculate_area(self,):
        area= 4*self.side
        print(f'Area: {area}')

class Rectangle(Shape):

    def data(self,):
        self.length = int(input('ENTER THE LENGTH:'))
        self.wide = int(input('ENTER THE WIDE:'))

    def calculate_perimeter (self,):
        perimeter= 2*(self.length + self.wide)
        print(f'Perimeter: {perimeter}')

    def calculate_area(self,):
        area= self.length * self.wide
        print(f'Area: {area}')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
 try:
    action= int(input('    SHAPES\n PRESS 1 TO CIRCLE \n PRESS 2 TO SQUARE\n PRESS 3 TO RECTANGLE\n PRESS ENTER TO EXIT\n SELECT AN OPTION:')) 
    if action == 1:
        circle_figure = Circle()
        circle_figure.data()
        circle_figure.calculate_perimeter()
        circle_figure.calculate_area()
        input('PRESS ENTER TO CONTINUE')
        clear_screen()
    elif action == 2:
        square_figure = Square()
        square_figure.data()
        square_figure.calculate_perimeter()
        square_figure.calculate_area()
        input('PRESS ENTER TO CONTINUE')
        clear_screen()
    elif action == 3: 
        rectangle_figure = Rectangle()
        rectangle_figure.data()
        rectangle_figure.calculate_perimeter()
        rectangle_figure.calculate_area()
        input('PRESS ENTER TO CONTINUE')
        clear_screen()
    else:
        break
 except:
     break