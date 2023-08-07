from random import randint
def codes_of_string(string):
    codes = dict()
    for char in string:
        if char not in codes:
            codes[char] = ord(char)

    return codes

print(codes_of_string('Hello world!'))


def filling_list(quantity):
    list = []
    for _ in range(quantity):
        list.append(randint(2, 9))
    return list

operands = filling_list(10)
operands_2 = filling_list(10)

while list:
    first_operand = operands.pop()
    second_operand = operands_2.pop()
    print(f'{first_operand} * {second_operand} = ')
