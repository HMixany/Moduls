def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        new_string = ' ' * ((length - len(string)) // 2) + string
        return new_string
    
string = input('Enter text ')
length = int(input('Enter length text '))
print(format_string(string, length))
