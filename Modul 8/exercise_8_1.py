'''
Функція get_days_from_today(date) повертає кількість днів від поточної дати, де параметр date - це рядок формату
'2020-10-09' (рік-місяць-день).

Підказки:

Параметр date розбити на рік, місяць та день можна використовуючи метод рядків split.
datetime приймає аргументи типу int, використовуйте перетворення типів.
ігноруйте години, хвилини та секунди для вашої дати, важливі повні дні.
кількість днів ви можете отримати відніманням з поточної дати, заданої в змінній date (без часу).
Наприклад: Якщо поточна дата - '5 травня 2021', то виклик get_days_from_today("2021-10-09") поверне нам -157.
'''

from datetime import datetime, date, timedelta


def get_days_from_today(date):
    today = datetime.now().date()
    list_data = date.split('-')
    current_data = datetime(int(list_data[0]), int(list_data[1]), int(list_data[2])).date()
    delta = today - current_data
    return delta.days


print(get_days_from_today("2021-10-09"))
