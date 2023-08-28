from pathlib import Path

path = Path('C:/Users/User/Downloads/New')


def get_cats_info(path):
    result = []
    with open(path, 'r') as fh:
        list_lines = fh.readlines()

        for line in list_lines:
            line = line.replace('\n', '')
            list_str = line.split(',')
            dict_line = {'id': list_str[0], 'name': list_str[1], 'age': list_str[2]}
            result.append(dict_line)

    return result


print(get_cats_info(path))
