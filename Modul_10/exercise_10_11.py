'''
Створимо клас NumberString, успадкуємо його від класу UserString, визначимо для нього метод number_count(self),
який буде рахувати кількість цифр у рядку.
'''

from collections import UserString


class NumberString(UserString):
    def number_count(self):
        self.count = 0
        for char in self.data:
            if char.isdigit():
                self.count += 1

        return self.count