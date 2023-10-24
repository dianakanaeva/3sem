from lab_python_oop.color import Color
from lab_python_oop.GF import GeometricFigure

class Rectangle(GeometricFigure):
    def __init__(self, width_, height_, color):
        self.width = width_
        self.height = height_
        self.color = Color(color)
        self.type = "Прямоугольник"

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Rectangle(type={}, width={}, height={}, color={}, area={})".format(self.type, self.width, self.height, self.color, self.area())
