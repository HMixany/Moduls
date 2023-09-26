class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Cell: {self.x} {self.y}'

    def __repr__(self):
        return f'Cell: {self.x} {self.y}'


class Map:
    def __init__(self):
        self.__n = 5
        self.__m = 5
        self.map = [[Cell(j, i) for i in range(self.__n)] for j in range(self.__m)]
        self.__current_x = 0
        self.__current_y = 0

    def __next__(self):
        if self.__current_x == self.__m:
            self.__current_x = 0
            self.__current_y += 1
            if self.__current_y == self.__n:
                raise StopIteration('Done')
        cell = self.map[self.__current_x][self.__current_y]
        self.__current_x += 1
        return cell


c = [[' ' for i in range(10)] for j in range(5)]
print(c)
for i in c:

    print('|'.join(i))