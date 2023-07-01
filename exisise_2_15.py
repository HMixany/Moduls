result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        if result is None:
            result = int(input())
            wait_for_number = False


#        if wait_for_number:
#            operand = int(input())
#            wait_for_number = False

        if not wait_for_number:
            operator = input()
            if not operator in ['+', '-', '*', '/', '=']:
                print(f"{operator} is not '+' or '-' or '*' or '/'. Try again")
                continue
            if operator == '=':
                print(result)
                break
            wait_for_number = True

        if wait_for_number:
            operand = int(input())
            wait_for_number = False

#        if operand is None:
#            continue

        if operator == '+':
            result = result + operand
        elif operator == '-':
            result = result - operand
        elif operator == '*':
            result = result * operand
        elif operator == '/':
            result = result / operand
        elif operator == '=':
            print(result)
            break
    except ValueError:
        print(f"{operand} is not a number. Try again")
        wait_for_number = True
print(result)
