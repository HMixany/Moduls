grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    result_list = []
    count = 0
    for key, val in students.items():
        count += 1
        result_list.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(count, key, val, grades[val]))

    return result_list


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
for el in formatted_grades(students):
    print(el)