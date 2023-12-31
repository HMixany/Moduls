from collections import UserDict


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


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value=None):
        if value is None:
            self.value = value
        elif len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)  # застосування асоціації під назваю композиція. Об'єкт Name існує поки є об'єкт Record
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        for p in self.phones:
            if number == p.value:
                self.phones.remove(p)

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                index = self.phones.index(phone)
                self.phones[index] = Phone(new_number)
                return
        raise ValueError

    def find_phone(self, num):
        for phone in self.phones:
            if phone.value == num:
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, user):  # асоціація під назвою агригація
        self.data[user.name.value] = user

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]



@input_error
def hello(*args):
    return f'How can I help you?'


# Декорована функція для додавання нового контакту або оновлення існуючого.
@input_error
def add(*args):
    if args[1] in phonebook:
#        raise ValueError                                  # Викликаємо помилку, якщо контакт з таким ім'ям вже існує.
        name_record = phonebook.find(args[1])
        name_record.add_phone(args[2])
        return f'Phone {args[2]} has been added to the contact {args[1]}'
    name_record = Record(args[1])
    name_record.add_phone(args[2])
    phonebook.add_record(name_record)
#    phonebook[args[1]] = args[2]
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


book = AddressBook()
john_record = Record('John')
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record('Jane')
jane_record.add_phone('9876543210')
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)
    print(name)
print(f"{'; '.join(p.value for p in john_record.phones)}")
print(f"{'; '.join(p.value for p in jane_record.phones)}")
john = book.find('John')
print(john)
john.edit_phone('1234567890', '3333333333')
print(john)
number = Phone()
print(number.value)
found_phone = john.find_phone('3333333333')
print(f'{john.name}: {found_phone}')
book.delete('Jane')
for name, record in book.data.items():
    print(record)
