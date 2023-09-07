def hello():
    print('How can I help you?')


def add(name, numbers):
    telephone_numbers_book[name] = numbers


def change():
    pass


def phone():
    pass


def show_all(*args):
    for name, num in telephone_numbers_book.items():
        print(f'{name} {num}')


def good_bay(*args):
    seans = False
    return seans


def input_error():
    pass


def input_error(func):
    def inner(comand):
        try:
            return func(comand)
        except KeyError:
            print('Error comand')
        except ValueError:
            print('Error value')
        except IndexError:
            print('Error index')

    return inner
@input_error
def handler(comand):
    return COMANDS[comand]



COMANDS = {'hello': hello, 'add': add, 'change': change, 'phone': phone, '.': good_bay, 'show all': show_all}
telephone_numbers_book = {}
seans = True
while seans:
    input_user = input()
    for i in filter(lambda x: )
    list_input_user = input_user.split(' ')
    get_handler = handler(list_input_user[0])
    get_handler(list_input_user[1], list_input_user[2])
