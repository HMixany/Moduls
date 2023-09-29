class A:
    @staticmethod  # Дозволяє визвати цей метод без создания екземпляру класу. Він не має доступу до екземпляру.
    def method():
        print('asd')


A().method()


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    # Если нужно обработать или использовать только атрибуты класса(MIN_COORD MAX_COORD) тогда создают метод класса
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
            print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v = Vector(2, 500)
v2 = Vector(5, 77)
print(v.get_coord())
print(v2.get_coord())
print(Vector.norm2(7, 8))
