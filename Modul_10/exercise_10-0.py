class User:
    name = 'UserName'
    age = 15
    def say_name(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def set_age(self, age):
        self.age = age

bob = User()
bob.name = 'Bob'
bob.say_name()
bob.set_age(25)
bob.say_name()


class Human:
    name = ''
    def hello(self, val):
        if self.name:
            return f'Hello {val}! I am {self.name}'
        return f'Hello {val}!'


bill = Human()
print(bill.hello('John'))
bill.name = 'Bill'
print(bill.hello('John'))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi {self.name}'


p = Person('Boris', 25)
print(p.name)
print(p.age)
print(p.greeting())

class A:
    x = 'I am A class'

class B:
    x = 'I am B class'
    y = 'I exist only in B'

class C(A,B):
#class C(B,A):
    z = 'This exists only in C'


c = C()
print(c.z)
print(c.y)
print(c.x)