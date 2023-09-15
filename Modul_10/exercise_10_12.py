'''
Створимо клас IDException, який успадковуватиме клас Exception.

Також реалізуємо функцію add_id(id_list, employee_id), яка додає до списку id_list ідентифікатор користувача
employee_id та повертає вказаний оновлений список id_list.

Функція add_id буде викликати власне виключення IDException, якщо employee_id не починається з '01', інакше
employee_id буде додано до списку id_list.
'''


class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if employee_id[:2] == '01':
        id_list.append(employee_id)
    else:
        raise IDException
    return id_list