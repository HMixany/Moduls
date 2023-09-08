def hello(*args):
    print('How can I help you?')


def add(*args):
    telephone_numbers_book[args[1]] = args[2]
    print('Contact added')


def change(*args):
    pass


def phone(*args):
    pass


def show_all(*args):
    for name, num in telephone_numbers_book.items():
        print(f'{name} {num}')


def good_bay(*args):
    seans = False
    return seans


def input_error(*args):
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



COMANDS = {'hello': hello, 'add': add, 'change': change, 'phone': phone, 'good bay': good_bay, 'show all': show_all}
telephone_numbers_book = {}
seans = True
while seans:
    input_user = input()

    list_input_user = input_user.split(' ')
    if list_input_user[0] in ('good', 'show'):
        list_input_user[0] = list_input_user[0] + ' ' + list_input_user[1]
    arguments = tuple(list_input_user)

    get_handler = handler(arguments[0])
    get_handler(*arguments)
