class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.list = [self.x, self.y]
        self.dict = {'x': self.x, 'y': self.y}

    def __str__(self):  # При перетворенні об'єкту в строку. Визов print(object), str(object)
        return f'str: ({self.x}, {self.y})'  # за замовченням поверне об'єкт

    def __repr__(self):  # Звернення до об'єкту з метою подивитись його строчне роедставлення визиває цей метод
        return f'rpr: ({self.x}, {self.y})'  # за замовченням поверне об'єкт

    def __getitem__(self, item):  # Коли до об'єкту застосовують [item],в яких якийсь ключ,викликається цей метод
        return self.list[item]  # Дозволяє звертатись до об'єкту по індексу як до списку або ключу як до dict

    def __setitem__(self, key, value):  # Викликається коли до об'єкту застосовують '[] ='
        if isinstance(key, str):  # Якщо ключ строка, змінимо значення в словнику за ключем
            self.dict[key] = value
        elif isinstance(key, int):  # Якщо ключ число, змінимо значення в списку за індексом
            self.list[key] = value

    def __call__(self, *args, **kwargs):  # Викликається при визові єкземпляру об'єкта. При виклику функціі.
        # Екземпляр об'єкту можно викликати як функцію з уруглими дужками. Ще називають його Функтар
        print('This is object has been called')

    def __enter__(self):             # Метод менеджеру контксту with... as...:
        print('Enterind the context')
        return self                  # Пthtlf' об'єкт в as

    def __exit__(self, exc_type, exc_val, exc_tb):   # Метод менеджеру контекста, приймає помилки в аргументах для
        # правильного завершення контексту
        print('Finishing context')


# ----------------------------------------------------------------------------------------------------------------
# Ітератор
class Iterator:
    def __init__(self):
        self.start = 0

    def __next__(self):                        # Щоб об'єкт класу міг ітеруватися, він повинен мати методи next та iter
        print(f'Hey, I am iteration number {self.start}')   # Люба операція на шагу ітераціі
        self.start += 1                            # Шаг ітерації
        if self.start == 20:                       # Умова коли зупинити ітерацію
            raise StopIteration
        return self.start

    def __iter__(self):
        return self


#class MyIterable:
#    def __iter__(self):
#        return Iterator()
# ----------------------------------------------------------------------

# Інкапсуляція.
#
# public    - загальнодоступна область, доступні поля із внє об'єкта
# protected - доступні із внутрі класу та його нащадків
# private   - доступ тіки з нутрі класу

class Character:
    def __init__(self, name):
        self.name = name       # public. Після створення екземпляру цього класу до name можно звертатись,
        # використовувати та змінювати char = Character('John') , char.name
        self._damage = 10      # protected. Зовні класу та нащадків не досяжний. Досяжний внутрі класу Character, та
        # його нащадку Enemy. Але доступ можно отримати і зовні. char._damage. Та змінити
        self.__hp = 100        # private. Доступен тільки внутрі класу. Але зовні теж можно добратися. Якщо ввести
        # char.__dict__ буде видно як. char._Character__hp. Теж можно і змінити.
        # З методами також як і з полями:

    def public(self):
        pass

    def _protected(self):
        pass

    def __private(self):
        pass

    def get_hp(self):            # Геттер @property
        return self.__hp

    def set_hp(self, hp):        # Сеттер
        if 0 < hp <= 100:
            self.__hp = hp

    @property                    # Геттер. Як би преобразовує приват поле в паблік
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):         # Сеттер. Якщо не буде проперті не буде робити
        if 0 < value <= 10:
            self.__hp = value
        else:
            raise ValueError

class Enemy(Character):
    pass


char_position = Position(3, 10)
print(char_position)
print({char_position})
print(char_position[0])
char_position.list[0] = 8
print(char_position[0])
print(char_position.list)
char_position()
print('-----------------------')
my_iterable = Iterator()                                        # MyIterable()
for i in my_iterable:
    print(i)
