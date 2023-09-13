from functools import reduce


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input('Enter num '))
result = reduce(lambda x, y: x * y, range(1, num + 1))         # факторіал за допомогою функції reduce
print(factorial(num))
print(result)
