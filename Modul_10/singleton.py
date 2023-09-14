class Singleton:
    instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_.instance, class_):
            class_.instance = object.__new__(class_, *args, **kwargs)
        return class_.instance            #Якщо екземпляр цього класу вже існує, повертаемо цей існуючий екземпляр


class A(Singleton):
    pass


a = A()
a_1 = A()
print(a)                           # Создається екземпляр тільки раз та при повторному создаванні повертається той же
print(a_1)