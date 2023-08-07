def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    lists_phones = {'JP': [], 'UA': [], 'TW': [], 'SG': []}
    for number in list_phones:
        new_number = sanitize_phone_number(number)
        if len(new_number) > len(new_number.removeprefix('81')):
            lists_phones['JP'].append(new_number)
        elif len(new_number) > len(new_number.removeprefix('65')):
            lists_phones['SG'].append(new_number)
        elif len(new_number) > len(new_number.removeprefix('886')):
            lists_phones['TW'].append(new_number)
        else:
            lists_phones['UA'].append(new_number)

    return lists_phones

def get_phone_numbers_countries(list_phones):
    list_numbers = dict()
    for number in list_phones:
        new_number = sanitize_phone_number(number)
        if new_number.startswith('81'):
            list_numbers.setdefault('JP', []).append(new_number)
        elif new_number.startswith('65'):
            list_numbers.setdefault('SG', []).append(new_number)
        elif new_number.startswith('886'):
            list_numbers.setdefault('TW', []).append(new_number)
        else:
            list_numbers.setdefault('UA', []).append(new_number)

    return list_numbers
