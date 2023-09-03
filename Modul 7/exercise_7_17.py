'''
Повернемося до попереднього завдання та виконаємо зворотне. Рекурсивна функція encode для кодування списку або рядка.

Як аргумент функція приймає список ( наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]) або рядок

(наприклад, "XXXZZXXYYYZZ"). Функція повинна повернути закодований список елементів

(наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).
'''


def encode(data):
    if not data:
        return []
    result = [data[0]]
    count = 1
    index = 1
    for i in range(1, len(data)):
        if data[0] == data[i]:
            count += 1
            index += 1
        else:
            break
    result.append(count)
    return result + encode(data[index:])


print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))
print(encode("XXXZZXXYYYZZ"))
