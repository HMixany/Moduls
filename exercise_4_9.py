def is_valid_pin_codes(pin_codes):
    result = None
    if len(pin_codes) != len(set(pin_codes)) or len(pin_codes) == 0:
        result = False
    else:
        result = True

    for i in pin_codes:
        if type(i) != str:
            result = False
            break
        if not i.isdigit():
            result = False
            break
        if len(i) != 4:
            result = False
            break


    return result

print(is_valid_pin_codes(['1234', '4321', '5678']))
print(is_valid_pin_codes(['1234', '43218', '5678']))
print(is_valid_pin_codes(['1234', '4321', '5678', '1234']))
print(is_valid_pin_codes(['1234', '4321', 'qwer']))
print(is_valid_pin_codes([]))
print(is_valid_pin_codes([1234, '9876', '4567']))
