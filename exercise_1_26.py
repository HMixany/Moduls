# Input - 2023
# Output_century - 21
n = int(input('Enter year '))
century = n // 100 + int(n % 100 > 0)
print(f'Century {century}')