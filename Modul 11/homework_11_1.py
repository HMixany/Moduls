from homework_11_2 import *


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Enter user name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Give me name and phone please'
        except TypeError:
            return 'Give me command'

    return inner


@input_error
def compiling_page(page_number, contacts, total):
    result = f'\nPage number {page_number} of {total}\n'
    for name, record in contacts.items():
        result += f'{record}\n'
    return result


# Декорована функція для додавання нового контакту або оновлення існуючого.
@input_error
def add(*args):
    if args[1] in phonebook:                                   # Якщо контакт вже є
        name_record = phonebook.find(args[1])                  # Знайдемо контакт за ім'ям
        if '.' in args[2]:                                     # Якщо третім аргументом елемент дати
            text = name_record.add_birthday(args[2])
            return f'Birthday {text}'                          # Повідомить про додавання дня народження
        else:
            name_record.add_phone(args[2])                     # Додаємо новий номер, якщо контакт вже існує.
            return f'Phone {args[2]} has been added to the contact {args[1]}'
    if len(args) == 4:
        name_record = Record(args[1], args[3])
    else:
        name_record = Record(args[1])
    name_record.add_phone(args[2])
    phonebook.add_record(name_record)
    return f'Contact {args[1]} with phone {args[2]} has been added'   # Повідомляємо користувача про успішне додавання.


# Декорована функція для зміни номера телефону контакту.
@input_error
def change(*args):
    if args[1] not in phonebook:
        raise KeyError                                       # Викликаємо помилку, якщо контакт з таким ім'ям не існує.
    name_record = phonebook.find(args[1])                    # Знаходимо об'єкт Record контакту
    name_record.edit_phone(args[2], args[3])                 # Змінюємо старий номер на новий
    return f'Phone number {args[2]} for {args[1]} has been changed to {args[3]}'


# Декорована функція для видалення номеру у контакта
@input_error
def remove(*args):
    if args[1] not in phonebook:
        raise KeyError
    name_record = phonebook.find(args[1])
    name_record.remove_phone(args[2])
    return f'Phone number {args[2]} has been removed'


# Декорована функція для отримання номера телефону контакту.
@input_error
def phone(*args):
    if args[1] not in phonebook:
        raise KeyError                                       # Викликаємо помилку, якщо контакт з таким ім'ям не існує.
    name_record = phonebook.find(args[1])
    result = f"{'; '.join(p.value for p in name_record.phones)}"
    return result                                            # Повертаємо номера телефонів контакту.


# Декорована функція для отримання всієї інформаціі о контакту, або отримання сторінки контактів
@input_error
def show(*args):
    if args[1] not in phonebook:
        raise KeyError                                       # Викликаємо помилку, якщо контакт з таким ім'ям не існує.
    name_record = phonebook.find(args[1])
    return name_record


# Декорована функція для виведення всіх контактів.
@input_error
def show_all(*args):
    if not phonebook:
        raise ValueError('No contacts')
    result = ''
    chunk_size = 7
    user_page = None
    if len(args) > 1:
        chunk_size = int(args[1])
    total_page = ((len(phonebook.data) + chunk_size - 1) // chunk_size)
    if len(args) == 3:
        user_page = int(args[2])
        if user_page > total_page:
            return f'Total pages: {total_page}'
    generator = phonebook.iterator(chunk_size)
    if user_page is None:
        for page_number, page in enumerate(generator, start=1):
            result += compiling_page(page_number, page, total_page)
    else:
        page = [item for index, item in enumerate(generator, start=1) if index == user_page]
        result = compiling_page(user_page, page[0], total_page)
#        for page_number, page in enumerate(generator):
#            if (page_number + 1) == user_page:
#                result = compiling_page(page_number, page, total_page)

    return result


# Декорована функція для видалення контакту
@input_error
def delete(*args):
    phonebook.delete(args[1])
    return f'Contact {args[1]} has been deleted'


@input_error
def get_handler(*args):
    command = args[0].lower()
    return COMMANDS[command]


COMMANDS = {'remove': remove,            # Видаляє номер у контакта
            'add': add,                  # Додає новий контакт та до існуючого номер або дату народження.
            'change': change,            # Змінює старий номер на новий
            'phone': phone,              # Пошук номеру(номерів) телефону контакту за ім'ям
            'show all': show_all,        # Виводить всі записи
            'delete': delete,            # Видалення контакту
            'show': show}                # Виводить всі записи контакту за ім'ям

phonebook = AddressBook()   # Створюємо пустий словник для зберігання контактів (імена-ключі, номери телефону-значення).


def main():
    while True:
        input_user = input('Write command \t')
        list_input = []
        if input_user.lower() in ('good bay', 'close', 'exit'):
            print('Good bay!')
            break
        elif input_user[:8].lower() == 'show all':
            list_input.append(input_user[:8])
            list_input.extend(input_user[8:].split())
            arguments = tuple(list_input)
            print(get_handler(*arguments)(*arguments))
        else:
            list_input = input_user.split()
            arguments = tuple(list_input)
            handler = get_handler(*arguments)
            if handler not in COMMANDS.values():
                print('Enter error, try again')
                continue
            print(handler(*arguments))


if __name__ == '__main__':
    main()