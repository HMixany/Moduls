'''
Функция filter принимает в аргументах функцию и коллекцию. Применяет функцию к каждому елементу коллекции и
возвращает генератор с валидными елементами(функция вернула True)
'''

for i in range(10):
    if i % 2:
        print(i)


generator =  filter(lambda i: i % 2, range(10))   # фунція filter повертає генератор
print(generator)
#print(list(generator)                            # генератор используется только один раз. Если это раскоментировать,
                                                  # то в цикле ниже будет пустой генератор
for i in generator:
    print(i)


def func(text):
    if text in ['bad', 'mad', 'vodka', 'beer']:
        return False
    return True


for i in filter(func, ['apple', 'vodka', 'potato', 'beer']):
    print(i)
print()
print('{:^25}'.format('То же только с лямбдой:'))

bad_words = ('bad', 'mad', 'vodka', 'beer')
for i in filter(lambda j: j not in bad_words, ['apple', 'vodka', 'potato', 'beer']):
    print(i)