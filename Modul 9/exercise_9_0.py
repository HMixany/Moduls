hello = 1
add = 2
change = 3
phone = 4
good_bay = 5
show_all = 6
COMANDS = {'hello': hello, 'add': add, 'change': change, 'phone': phone, '.': good_bay, 'show all': show_all}

'hello' in COMANDS.keys()    # True

list1 = ['Misha', '0671058651', 'add']

for i in filter(lambda x: x in COMANDS.keys(), list1):
    print(i)                                            # 'add'

for i in filter(lambda x: x.isdigit(), list1):
    print(i)                                            # '0671058651'
    print(list1.index(i))                               # 1

# замикання
def multiply(x):
    def inner(y):
        return x * y
    return inner


multiply_ten = multiply(10)
multiply_three = multiply(3)
print(multiply_ten(10))                                # 100
print(multiply_ten(15))                                # 150
print(multiply_three(10))                              # 30
print(multiply_three(15))                              # 45


def multiplication(x):
    def inner(y):
        def func(z):
            return x * y * z
        return func
    return inner


multiplication_10 = multiplication(10)
multiplication_10_3 = multiplication_10(3)
print(multiplication_10_3(4))                             # 120
print(multiplication(10)(3)(5))                           # 150

#--------------------------------------------------------------------
# генераторы
def func():
    print('Entry point')
    yield None
    print('After yield')          # будет exeption stopiteration. Итерация закончилась. Такой же появляется в цикле for


generator = func()
next(generator)
#next(generator)                 # вызовет exeption stopiteration.


def func(n):
    i = 0
    while i < n:
        print('Entry point')
        yield i
        print('After yield')
        i += 1


generator = func(5)
for element in generator:
    print(element)


def my_range(x, y):                      # как работает функция range
    while x < y:
        yield x
        x += 1


for i in my_range(0, 5):
    print(i)
print('-----------------------------------------')

a = (i for i in [1,2,3,4])                 # генератор
print(next(a))                             # или через принт или через for. Иначе for  запомнит состояние итерации
print(next(a))
print(next(a))
#for i in a:                            # функция next под капотом цикла for проходит по каждому елементу генератора
#    print(i)