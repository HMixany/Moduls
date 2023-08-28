'''str.strip(): Видаляє всі пробіли та символи нового рядка з початку і кінця строки.

str.split(): Розбиває строку на список підстрок за допомогою роздільника (пробіл - за замовчуванням) і повертає список.

str.join(iterable): Об'єднує елементи ітерабельного об'єкту (списку, кортежу і т.д.) в одну строку, розділених str.

str.find(substring): Повертає індекс першого входження підрядка substring у строку, або -1, якщо підрядок не знайдено.

str.rfind(substring): Повертає максимальний індекс входження підрядка substring у строку з кінця, або -1, якщо підрядок не знайдено.

str.replace(old, new): Заміняє всі входження old на new у строкі і повертає нову строку.

str.isdigit(): Перевіряє, чи складається строка лише з цифр.

str.isalpha(): Перевіряє, чи складається строка лише з літер.

str.islower(): Перевіряє, чи складається строка лише з символів нижнього регістра.

str.isupper(): Перевіряє, чи складається строка лише з символів верхнього регістра'''

a = 'Hi there!'
start = 0
end = 7
print(a.find('er', start, end))   # 5
print(a.find('q'))                      # -1
print(a.index('t'))                     # 3

a = 'Some words'
print(a.rfind('o'))                     # 6
print(a.rindex('o'))                    # 6

s = "I am learning strings in Python. Some new methods got now."
sentences = s.split('. ')
print(sentences)
print(sentences[0])
text = '. '.join(sentences)
print(text)

clean = '     spacious     '.strip()    # rstrip and lstrip
print(clean)

dogs_text = 'All dogs bark like dogs.'
cats_text = dogs_text.replace('dogs', 'cats')
print(dogs_text)
print(cats_text)

print('TestHook'.removeprefix('Test'))  # Hook
print('TestHook'.removeprefix('Hook'))  # TestHook
print('TestHook'.removesuffix('Test'))  # TestHook
print('TestHook'.removesuffix('Hook'))  # Test

map = {ord('з'): 'z', ord('ю'): 'u'}
translated = 'зю'.translate(map)
print(translated)                       # zu

replace_dict = {ord('u'): 'o'}
text = 'sun'
print(text.translate(replace_dict))     # son
text = 'sun'
my_table = text.maketrans('nus', 'mot')
print(text.translate(my_table))         # tom
txt = 'the sun'
my_table = txt.maketrans('nus', 'nos', 'he t')
print(txt.translate(my_table))          # son

CYRILIC = ('а', 'ч', 'ш')
LATIN = ('a', 'ch', 'sh')
TRANSLIT_DICT = {}
for c, l in zip(CYRILIC, LATIN):
    TRANSLIT_DICT[ord(c)] = l
    TRANSLIT_DICT[ord(c.upper())] = l.upper()
print('чаша'.translate(TRANSLIT_DICT))
print('ЧАША'.translate(TRANSLIT_DICT))

for i in range(16):
    s = "int: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}".format(i)
    print(s)

width = 5
for num in range(12):
    print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))

s = '{name} {last_name}'.format(last_name='Dilan', name='Bob')
print(s)
s = '{name!r} {last_name}'.format(last_name='Dilan', name='Bob')
print(s)
print('des: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))  # des: 15 hex: f bin: 1111
print('pi: {:0.3}'.format(3.1415))                               # pi: 3.14
print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))     # "1" "+2" "-3" " 4"
print('|{:<10}|{:*^10}|{:>10}'.format('left', 'center', 'right'))  # |left      |**center**|     right
print('Hello world'.casefold())
print('Hello'.center(11, '*'))

import re

s = "I am 39 years old."
age = re.search('\d+', s)
print(age)                                  # <re.Match object; span=(5, 7), match='39'>
print(age.group())                          # 39
s = "I bought 7 nuts for 6$ and 10 bolts for 3$."
numbers = re.findall('\d+', s)
print(numbers)
s = 'blue socks and red shoes'
p = re.sub(r'(blue|white|red)', 'colour', s)
print(p)