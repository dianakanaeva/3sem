from lab_python_oop.GF import GeometricFigure
from lab_python_oop.color import Color
import math

class Circle(GeometricFigure):
    def __init__(self, rad_, color):
        self.radius = rad_
        self.color = Color(color)
        self.type = "Круг"

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "Circle(type={}, radius={}, color={}, area={})".format(self.type, self.radius, self.color, self.area())
