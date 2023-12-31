'''
Розберемо просту техніку кодування та декодування на основі серій. Наприклад, у нас є список із повторюваними

спостереженнями якоїсь величини, вона може приймати значення X, Y або Z. Значення з'являються у довільному порядку та

зберігаємо ми їх у списку ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"] або рядку "XXXZZXXYYYZZ".

Внаслідок чого ми можемо зменшити обсяг інформації, що зберігається? Стиснення можна досягти заміною групи повторюваних

значень на одноразове значення та лічильник повторів: ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

Рекурсивна функція decode для декодування списку, закодованого цим способом. Як аргумент функція приймає закодований

список. Функція має повернути розшифрований список елементів.
'''


def decode(data):
    result = []
    if len(data) < 2:
        return result
    result += data[0] * data[1]
    return result + decode(data[2:])


print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))
