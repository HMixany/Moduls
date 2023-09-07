hello = 1
add = 2
change = 3
phone = 4
good_bay = 5
show_all = 6
COMANDS = {'hello': hello, 'add': add, 'change': change, 'phone': phone, '.': good_bay, 'show all': show_all}

'hello' in COMANDS.keys()    # True

list1 = ['Misha', '0671058651', 'add']

for i in filter(lambda x: x in COMANDS.keys(), list1):
    print(i)                                            # 'add'

for i in filter(lambda x: x.isdigit(), list1):
    print(i)                                            # '0671058651'
    print(list1.index(i))                               # 1