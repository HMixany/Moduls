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
            del self.data[name]

    def iterator(self, page_size):
        keys = list(self.data.keys())
        total_pages = (len(keys) + page_size - 1) // page_size

        for page_number in range(total_pages):
            start = page_number * page_size
            end = (page_number + 1) * page_size
            page = {k: self.data[k] for k in keys[start:end]}
            yield page



'''
class DictChunkIterator:
    def __init__(self, dictionary, chunk_size):
        self.dict = dictionary
        self.keys = list(dictionary.keys())  # Отримуємо ключи словника
        self.chunk_size = chunk_size
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.keys):
            raise StopIteration
        else:
            start = self.current_index
            end = self.current_index + self.chunk_size
            chunk = {k: self.dict[k] for k in self.keys[start:end]}
            self.current_index = end
            return chunk
            '''

