from collections import UserDict


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
            self.data.pop(name)


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
