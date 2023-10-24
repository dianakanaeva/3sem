from lab_python_oop.rect import Rectangle
from lab_python_oop.color import Color

class Square(Rectangle):
    def __init__(self, length_, color):
        self.length = length_
        self.color = Color(color)
        self.type = "Квадрат"

    def area(self):
        return self.length ** 2

    def __repr__(self):
        return "Square(type={}, length={}, color={}, area={})".format(self.type, self.length, self.color, self.area())

