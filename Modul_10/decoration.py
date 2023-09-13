#import functools

def simple_decorator(func):
#    @functools.wraps(func)                        # интраспекция. Дает доступ к нативной функции. При вызове
                                                   # func.__name__ выдаст имя функции вызываемой
    def simple_wrapper(*args, **kwargs):
        print('Before func')                       # Тут можно обернуть в try exception , открыть файл и записать
        result = func(*args, **kwargs)                      # результат выполнения функции в файл. Затем закрыть файл
        print('After func')
        return result
    return simple_wrapper


@simple_decorator                                    # func = simple_decorator(func)
def func():
    return 'Hello world!'


@simple_decorator
def mul(x, y):
    return x * y


print(func())
print(mul(7, 5))
print('----------------------------------------------')

#--------------------------------------------------------------------------------------------------------------------
#import functools

def simple_decorator_1(func):
#    @functools.wraps(func)                        # интраспекция. Дает доступ к нативной функции. При вызове
                                                   # func.__name__ выдаст имя функции вызываемой
    def simple_wrapper(*args, **kwargs):
        print('Before func')                       # Тут можно обернуть в try exception , открыть файл и записать
        result = func(*args, **kwargs)                      # результат выполнения функции в файл. Затем закрыть файл
        print('After func')
        return result
    return simple_wrapper


def simple_decorator_2(func):
    def simple_wrapper(*args, **kwargs):
        print('Before func 2')
        result = func(*args, **kwargs)
        print('After func 2')
        return result
    return simple_wrapper
@simple_decorator_1                                  # func = simple_decorator(func)
@simple_decorator_2                                  # вкладываем один декоратор во второй
def func():
    print('func')
    return 'Hello world!'


@simple_decorator_1
@simple_decorator_2
def mul(x, y):
    return x * y


print(func())
print(mul(7, 5))
print('------------------------------------')

#-----------------------------------------------------------------------------------------------------

def decor_with_args(arg):                    # для передачи аргументов в декоратор нужно обернуть в еще один декоратор
    def simple_decorator(func):
        def simple_wrapper(*args, **kwargs):
            print(f'Before func {arg}')                       # Тут можно обернуть в try exception , открыть файл и записать
            result = func(*args, **kwargs)                      # результат выполнения функции в файл. Затем закрыть файл
            print(f'After func {arg}')
            return result
        return simple_wrapper
    return simple_decorator


@decor_with_args('abc')                                    # для передачи аргументов в декоратор нужно обернуть в еще
def func():                                                # один декоратор
    print('func')
    return 'Hello world!'


@decor_with_args('abc')
def mul(x, y):
    return x * y


print(func())
print(mul(7, 5))