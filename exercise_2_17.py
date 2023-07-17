while True:
    user_input = input('Enter number: ')

    try:
        x = int(user_input)
    except ValueError as error:
        print(error)
        continue

    break


age = int(input('Year age: '))

if age < 0:
    raise ValueError('Wrong age.')