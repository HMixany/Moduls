from pathlib import Path

path = Path('C:/Users/User/Downloads/New')


def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for i in range(len(employee_list)):
        for text in employee_list[i]:
            fh.write(text + '\n')
    fh.close()


employee_lists = [['60b90c1c13067a15887e1ae1,Tayson,3', '60b90c2413067a15887e1ae2,Vika,1'],
                  ['60b90c2e13067a15887e1ae3,Barsik,2', '60b90c3b13067a15887e1ae4,Simon,12'],
                  ['60b90c4613067a15887e1ae5,Tessi,5']]

write_employees_to_file(employee_lists, path)

fh = open(path, 'r')
fh.seek(0)
file_employees_list = fh.read()
print(file_employees_list)
fh.close()
