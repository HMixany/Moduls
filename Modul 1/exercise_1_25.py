# Input_number_apartment - 54
# Input_number_of_floors_in_entrance - 5
# Input_number_of_apartments_on_floor - 4

# Output_entrance - 3
# Output_floor - 4
num = int(input('Enter number apartment '))
num_floor = int(input('Enter number of floors in entrance '))
num_apartment = int(input('Enter number of apartments on floor '))
apart_entrance = num_floor * num_apartment
entrance = num // apart_entrance + int(num % apart_entrance > 0)
num -= (entrance - 1) * apart_entrance
floor = num // num_apartment + int(num % num_apartment > 0)
print(f'Entrance {entrance}\nFloor {floor}')