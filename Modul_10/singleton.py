class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.instance, cls):
            cls.instance = object.__new__(cls)
        return cls.instance            #Якщо екземпляр цього класу вже існує, повертаемо цей існуючий екземпляр


class A(Singleton):
    pass


a = A()
a_1 = A()
print(a)                           # Создається екземпляр тільки раз та при повторному создаванні повертається той же
print(a_1)