'''
Є файл зі списком працівників компанії. У кожному рядку файлу записано інформацію лише одного співробітника.

Формат запису, в межах навчання приймемо спрощений, такий як: ім'я співробітника, символ пропуску та його посада, тобто,
ким він працює.

John courier
Pipe cook
Функція get_employees_by_profession(path, profession) повинна у файлі (параметр path) знайти всіх співробітників
зазначеної професії (параметр profession)

Вимоги:

відкрийте файл за допомогою with для читання
отримайте рядки з файлу за допомогою методу readlines()
за допомогою методу find знайдіть усі рядки у файлі, де є вказана profession, та помістіть записи до списку
об'єднайте всі ці рядки в списку в один рядок за допомогою методу join (пам'ятайте про символ перенесення рядків '\n'
та зайві прогалини, які треба прибрати) приберіть значення змінної 'profession' (замініть на порожній рядок "" методом
replace) поверніть отриманий рядок із файлу
'''


def get_employees_by_profession(path, profession):
    with open(path, 'r') as fh:
        list_strings = fh.readlines()
    list_users = []
    for str in list_strings:
        if str.find(profession) != -1:
            new_str = str.replace(profession, '').strip().strip('\n')
            list_users.append(new_str)
    result = ' '.join(list_users)
    return result
