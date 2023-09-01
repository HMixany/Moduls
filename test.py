import random

list_1 = list(range(2, 10))
list_2 = list_1.copy()

random.shuffle(list_1)
random.shuffle(list_2)
for _ in range(10):
    operand_1 = random.choice(list_1)
    operand_2 = random.choice(list_2)
    print(f'{operand_1} * {operand_2} =')
print(list_1)
print(list_2)

