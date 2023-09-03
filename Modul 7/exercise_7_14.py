'''
Функція to_indexed(source_file, output_file) зчитує вміст файлу, додає до прочитаних рядків порядковий номер і зберігає

їх у такому вигляді у новому файлі. Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та

пробілу, після чого має йти текст рядка з вхідного файлу. Нумерація рядків іде від 0.
'''


def to_indexed(source_file, output_file):
    with open(source_file, 'r') as fh:
        list_strings = fh.readlines()
    result = []
    count = 0
    for str in list_strings:
        new_str = f'{count}: {str}'
        result.append(new_str)
        count += 1
    with open(output_file, 'w') as fh:
        fh.writelines(result)
