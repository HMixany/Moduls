from pathlib import Path

path = Path('C:/Users/User/Downloads/New')


def read_employees_from_file(path):
    result = []
    fh = open(path, 'r')
    fh.seek(0)
    str_read = fh.read()
    if str_read[-1] == '\n':
        result = str_read[:-1].split('\n')
    else:
        result = str_read.split('\n')
    fh.close()
    return result


print(read_employees_from_file(path))
