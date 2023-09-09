# Декоратор для обробки помилок введення користувача.
def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            print('Enter user name')
        except ValueError:
            print('Give me name and phone please')
        except IndexError:
            print('Give me name and phone please')

    return inner


@input_error
def hello(*args):
    return f'How can I help you?'


# Декорована функція для додавання нового контакту.
@input_error
def add(*args):
    if args[1] in phonebook:
        raise ValueError                                   # Викликаємо помилку, якщо контакт з таким ім'ям вже існує.
    phonebook[args[1]] = args[2]
    return f'Contact {args[1]} with phone {args[2]} has been added'   # Повідомляємо користувача про успішне додавання.


# Декорована функція для зміни номера телефону контакту.
@input_error
def change(*args):
    if args[1] not in phonebook:
        raise KeyError                                       # Викликаємо помилку, якщо контакт з таким ім'ям не існує.
    phonebook[args[1]] = args[2]
    return f'Phone number for {args[1]} has been changed to {args[2]}'        # Повідомляємо про успішну зміну номера.


# Декорована функція для отримання номера телефону контакту.
@input_error
def phone(*args):
    if args[1] not in phonebook:
        raise KeyError                                       # Викликаємо помилку, якщо контакт з таким ім'ям не існує.
    return f'{args[1]} phone number is {phonebook[args[1]]}'  # Повертаємо номер телефону контакту.


# Декорована функція для виведення всіх контактів.
@input_error
def show_all(*args):
    if not phonebook:
        raise ValueError
    result = ''
    for name, num in phonebook.items():
        result += f'{name}: {num}\n'
    return result


@input_error
def get_handler(command):
    return COMMANDS[command]


COMMANDS = {'hello': hello, 'add': add, 'change': change, 'phone': phone, 'show all': show_all}
phonebook = {}   # Створюємо пустий словник для зберігання контактів (імена - ключі, номери телефону - значення).


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
            list_input[1] = str.title(list_input[1])
            arguments = tuple(list_input)

            handler = get_handler(arguments[0].lower())
            print(handler(*arguments))


if __name__ == '__main__':
    main()