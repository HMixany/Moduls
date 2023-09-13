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
        super().__init__(value)
        self.value = value

    def valid_number(self):
        pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        for p in self.phones:
            if number == p.value:
                self.phones.remove(number)


    def edit_phone(self, old_number, new_number):
        for p in self.phones:
            if old_number == p.value:
                index = self.phones.index(p)
                self.phones[index] = Phone(new_number)

    def find_phone(self, num):
        if num in (p.value for p in self.phones):
            return num

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_records(self, user):
        self.data[user.name.value] = user

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name)



book = AddressBook()
john_record = Record('John')
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_records(john_record)

jane_record = Record('Jane')
jane_record.add_phone('9876543210')
book.add_records(jane_record)

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