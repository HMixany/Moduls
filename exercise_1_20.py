# Input - 123
# Output_one - 5
# Output_two - 4
num = int(input('Enter number '))
num1 = num // 100
num2 = (num // 10) % 10
num3 = num % 10
print(num1, num2, num3)
sum1 = num2 + num3
sum2 = num1 + num3
print(f'Output one {sum1}\nOutput two {sum2}')