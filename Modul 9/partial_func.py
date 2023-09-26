from functools import partial


def greet(greeting, separator, emphasis, name):
    return f'{greeting}{separator} {name}{emphasis}'


new_func = partial(greet, greeting='Hello', separator=',', emphasis='.')

text = new_func(name='Sviatoslav')
print(text)
text = new_func(name='Adrian')
print(text)


# Оригінальна функція з двома аргументами
def power(base, exponent):
    return base ** exponent


# Створюємо нову фкнкцію, де base фіксований на значенні 2
square = partial(power, base=2)
# Тепер square - це функція, яка підносить до квадратучисло,передане як аргумент
result = square(exponent=3)
print(result)