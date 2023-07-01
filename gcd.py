first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = first if first < second else second
i = True
while i:
    if first % gcd == 0 and second % gcd == 0 or gcd == 0:
        i = False
    else:
        gcd -= 1

print(gcd)
