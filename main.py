from lab_python_oop.circle import Circle
from lab_python_oop.rect import Rectangle
from lab_python_oop.sq import Square
import matplotlib.pyplot as plt

rectangle = Rectangle(8, 8, "синий")
circle = Circle(8, "зеленый")
square = Square(8, "красный")

print(rectangle, '\n', circle, '\n', square)

#данные
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

#построение графика
plt.plot(x, y)

#настройка осей
plt.xlabel('x')
plt.ylabel('y')
plt.title('пример графика')

#отображение графика в файле
plt.savefig('lab_python_oop\picture.png')
