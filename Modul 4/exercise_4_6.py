def split_list(grade):
    first = []
    second = []
    sum = 0
    if len(grade) != 0:
        for i in grade:
            sum += i
        result = sum / len(grade)
        for i in grade:
            if i <= result:
                first.append(i)
            else:
                second.append(i)
    return first, second

print(split_list([2,3,4,5]))

def lookup_key(data, value):
    list = []
    for key, val in data.items():
        if val == value:
            list.append(key)
    return list

print(lookup_key({1:'Hel', 2:'Mul'}, 'Hel'))