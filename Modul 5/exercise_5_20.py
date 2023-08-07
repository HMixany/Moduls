numbers = ['123', '456', '321', '75', '10', 'asd', '53d']


def delete_str(data):
    result = list()
    for element in data:
        if element.isdigit():
            result.append(element)

    return result


print(delete_str(numbers))

list_dicts = [{'Name': 'Misha', 'Last name': 'Hrytsan', 'data': '1983'},
              {'Name': 'Sonia', 'Last name': 'Hrytsan', 'data': '2016'},
              {'Name': 'Katia', 'Last name': 'Poltavec', 'data': '2007'}]
result = list()
for i in range(len(list_dicts)):
    if list_dicts[i]['Last name'].find('hrytsan') != -1:
        result.append(list_dicts[i])
    if 'Hrytsan' in list_dicts[i]['Last name']:
        result = True

print(result)
