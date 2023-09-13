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