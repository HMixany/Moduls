'''
Реалізовуємо клас CatDog, не використовуючи успадкування від класу Animal, але щоб екземпляр класу CatDog
поводився як і екземпляр класу Cat, тобто. він повинен вдати, що він клас Cat.(Поліморфізм)
'''


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def change_weight(self, weight):
        self.weight = weight

    def say(self):
        return 'Meow'

