'''
При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати з даними далі.
Функцію data_preparation приймає набір даних, список списків (Приклад: [[1,2,3],[3,4], [5,6]]).

Функція повинна видаляти з переданих списків найбільше і найменше значення, але якщо розмір списку понад два елементи.
Після видалення даних з кожного списку необхідно злити їх разом в один список, відсортувати його за зменшенням та
повернути отриманий список як результат (Для прикладу вище результат буде наступним: [6, 5, 4, 3, 2]).
'''


def data_preparation(list_data):
    result = []
    for list in list_data:
        if len(list) > 2:
            list.sort()
            list.pop()
            list.pop(0)
        result.extend(list)
    result.sort(reverse=True)

    return result
