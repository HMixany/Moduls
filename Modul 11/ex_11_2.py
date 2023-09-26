'''
У класу Point через конструктор __init__ оголошено два атрибути: координати x та y. Приховаємо доступ до них з допомогою
подвійного підкреслення: __x та __y

Реалізуємо для класу Point механізми setter та getter до атрибутів __x та __y за допомогою декораторів property та setter.

Приклад:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10
'''

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = new_y