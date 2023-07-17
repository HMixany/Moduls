x = 0
match x:
    case 0:
        print(x)
    case x2 if x > 0:
        x2 = x2 * 8
        print(x2)
    case _:
        print('pusto')
