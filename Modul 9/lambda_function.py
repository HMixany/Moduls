def func(x, y, z):
    return x * y * z


result = func(3, 5, 7)
print(result)


func_lambda = lambda x, y, z: x * y * z
result_lambda = func_lambda(3, 5, 7)
print(result_lambda)
print('-----------------------------------')


def func_2(f):
    f()


print(func_2(lambda: print('Hello')))


l = [(lambda i: i ** 2)(i) for i in range(5)]
print(l)