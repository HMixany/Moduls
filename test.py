import random

list_1 = list(range(2, 10))
list_2 = list_1.copy()

random.shuffle(list_1)
random.shuffle(list_2)
for _ in range(10):
    operand_1 = random.choice(list_1)
    operand_2 = random.choice(list_2)
    print(f'{operand_1} * {operand_2} =')
print(list_1)
print(list_2)

dict = {'a': 5, 'b': 6, 'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13}
print(len(dict))


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


def show_all(*args):
    if not dict:
        raise ValueError
    if len(dict) > 10:
        chunk_size = int(input('Many contacts in the book. How much to withdraw? '))
    else:
        chunk_size = len(dict)

    iterator = DictChunkIterator(dict, chunk_size)
    for l in iterator:
        result = ''
        for name, record in l.items():
            result += f'{record}\n'
        print(result)
        input('Press enter to continue ')
    return f'No more contacts'


print(show_all())
