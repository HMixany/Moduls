'''
Суть карирования в быстром расширении функционала. Можно добавить функции не задевая созданные.
'''
def summ(x, y):
    return x + y


def mul(x, y):
    return x * y


def sub(x, y):
    return x - y


operations = {'+': summ, '-': sub, '*': mul}


def operate(operator):
    return operations[operator]


x = 50
y = 10
operator = input('Enter operator ')
handler = operate(operator)
print(handler(x, y))

