points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    distance = 0
    if len(coordinates) <= 1:
        return distance
    for i in range(0, len(coordinates) - 1):
        new_list = [coordinates[i], coordinates[i+1]]
        new_list.sort()
        tuple_list = tuple(new_list)
        distance += points.get(tuple_list)
    return distance

x = calculate_distance([0,1,3,2,0])
print(x)