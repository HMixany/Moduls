'''
Функція визначення кількості днів у конкретному місяці. Ця функція повинна приймати два параметри: month - номер місяця

у вигляді цілого числа в діапазоні від 1 до 12 і year - рік, що складається із чотирьох цифр. Перевірте, чи функція

коректно обробляє місяць лютий високосного року.
'''

from datetime import datetime, date, timedelta


def get_days_in_month(month, year):
    if month == 12:
        delta = datetime(year + 1, 1, 1) - datetime(year, month, 1)
    else:
        delta = datetime(year, month + 1, 1).date() - datetime(year, month, 1).date()
    return delta.days


print(get_days_in_month(2, 2016))
print(get_days_in_month(9, 2023))
