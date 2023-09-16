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

    return inner


@input_error
def hello(*args):
    return f'How can I help you?'


# Декорована функція для додавання нового контакту або оновлення існуючого.
@input_error
def add(*args):
    if args[1] in phonebook:
        name_record = phonebook.find(args[1])
        name_record.add_phone(args[2])                     # Додаємо новий номер, якщо контакт вже існує.
        return f'Phone {args[2]} has been added to the contact {args[1]}'
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
    return f'Phone number {args[2]} for {args[1]} has been changed to {args[3]}'# Повідомляємо про успішну зміну номера.


# Декорована функція для отримання номера телефону контакту.
@input_error
def phone(*args):
    if args[1] not in phonebook:
        raise KeyError                                       # Викликаємо помилку, якщо контакт з таким ім'ям не існує.
    name_record = phonebook.find(args[1])
    return name_record                                       # Повертаємо номера телефонів контакту.


# Декорована функція для виведення всіх контактів.
@input_error
def show_all(*args):
    if not phonebook:
        raise ValueError
    result = ''
    for name, record in phonebook.data.items():
        result += f'{record}\n'
    return result


# Декорована функція для видалення контакту
@input_error
def delete(*args):
    phonebook.delete(args[1])
    return f'Contact {args[1]} has been deleted'


@input_error
def get_handler(command):
    return COMMANDS[command]


COMMANDS = {'hello': hello, 'add': add, 'change': change, 'phone': phone, 'show all': show_all, 'delete': delete}
phonebook = AddressBook()   # Створюємо пустий словник для зберігання контактів (імена-ключі, номери телефону-значення).


def main():
    while True:
        input_user = input('Write command \t')
        if input_user.lower() in ('good bay', 'close', 'exit'):
            print('Good bay!')
            break
        elif input_user.lower() == 'show all':
            print(get_handler(input_user.lower())())
        else:
            list_input = input_user.split()
            arguments = tuple(list_input)
            handler = get_handler(arguments[0].lower())
            print(handler(*arguments))


if __name__ == '__main__':
    main()