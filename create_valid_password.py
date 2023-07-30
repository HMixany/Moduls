from random import randint


def get_random_password():
    random_password = ''
    for _ in range(8):
        random_num = chr(randint(40, 126))
        random_password += random_num

    return random_password


def is_valid_password(password):
    valid_password = False
    if len(password) == 8:
        valid_digit = any(char.isdigit() for char in password)
        valid_upper = any(char.isupper() for char in password)
        valid_lower = any(char.islower() for char in password)

        if valid_digit and valid_upper and valid_lower:
            valid_password = True

    return valid_password


def get_password():
    count = 0
    while count <= 100:
        random_password = get_random_password()
        if is_valid_password(random_password):
            return random_password
        count += 1


print(get_password())
