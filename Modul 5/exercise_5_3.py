def sanitize_phone_number(phone):
    new_number = (phone.strip()
                  .removeprefix('+')
                  .replace('(', '')
                  .replace(')', '')
                  .replace(' ', '')
                  .replace('-', ''))

    return new_number

print(sanitize_phone_number("38050 111 22 11   "))


def is_check_name(fullname, first_name):
    if len(fullname) > len(fullname.removeprefix(first_name)):
        return True
    else:
        return False