'''
Функция map принимает в аргументы функцию и колекцию(или несколько колекций).
Проходит функцией по всем елементам коллекции и возвращает генератор
'''
def mult(i):
    return i ** 2


my_list = [1, 2, 3, 4, 5]
result = []
for i in my_list:
    element = mult(i)
    result.append(element)

print(result)


result_map = map(mult, my_list)
print(result_map)
print(list(result_map))                  # чтобы следующий цикл сработал закоментируй
for i in result_map:
    print(i)
print('----------------------------------------------------------------------------')


for key, val in map(lambda i: (i[0], i[1]), {'a': 1, 'b': 2}.items()):
    print(key)
    print(val)
print('-------------------------------------------------------------------')


list_1 = [1, 2, 3, 4, 5]
list_2 = ['a', 'b', 'c', 'd', 'e']
for n in map(lambda x, y: f'{y}: {x}', list_1, list_2):
    print(n)

print('------------------------------------------------------------------')
generator = map(lambda i: (i[0], i[1]), {'a': 1, 'b': 2, 'c': 3, 'd': 4}.items())
for i in generator:
    print(i)

print('-------------------------------------------------------------------')
dict = {'a': 5, 'b': 6, 'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13}


def iterator(dict, page_size):
    keys = list(dict.keys())
    total_pages = (len(keys) + page_size - 1) // page_size

    for page_number in range(total_pages):
        start_index = page_number * page_size
        end_index = (page_number + 1) * page_size
        page = {k: dict[k] for k in keys[start_index:end_index]}
        yield page

generator = iterator(dict, 3)

print(generator)
for page_number, page in enumerate(iterator(dict, 3)):
    if page_number == 3:
        print(page)
    print(page_number)
