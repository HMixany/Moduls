x = int(input('Enter number '))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print('x is zero')
    case 4:
        print('x is 4')
    # Empty case with if-condition
    case _ if x < 10:
        print('x is < 10')
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
