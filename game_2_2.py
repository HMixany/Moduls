from random import randint

HEIGHT = 5
WIDTH = 5

char_x = randint(0, WIDTH - 1)
char_y = randint(0, HEIGHT - 1)
char_sign = 'X'

exit_x = randint(0, WIDTH - 1)
exit_y = randint(0, HEIGHT - 1)
exit_sing = 'O'

enemy_x = randint(0, WIDTH - 1)
enemy_y = randint(0, HEIGHT - 1)
enemy_sing = 'E'

turns = 0

def generation_map(char_x, char_y, char_sign,
                   enemy_x, enemy_y, enemy_sign,
                   exit_x, exit_y, exit_sing,
                   width=WIDTH, height=HEIGHT):

    world_map = ''
    for j in range(height):
        row = '|'
        for i in range(width):
            if char_x == i and char_y == j:
                row += char_sign + '|'
            elif enemy_x == i and enemy_y == j:
                row += enemy_sign + '|'
            elif exit_x == i and exit_y == j:
                row += exit_sing + '|'
            else:
                row += '  |'
        world_map += f'{row}\n'

    return world_map

def move(direction, x, y , width=WIDTH, height=HEIGHT):
    if direction == 'w' and y > 0:
        y -= 1
    elif direction == 's'and y < height - 1:
        y += 1
    elif direction == 'a'and x > 0:
        x -= 1
    elif direction == 'd'and x < width - 1:
        x += 1
    else:
        print('Input Error')

    return x, y



while True:

    print(generation_map(char_x, char_y,char_sign,
                         enemy_x, enemy_y, enemy_sing,
                         exit_x, exit_y, exit_sing))

    if char_x == exit_x and char_y == exit_y:
        print('You WIN !!!')
        break

    direction = input('Input direction (w, a, d, s): ')
    char_x, char_y = move(direction, char_x, char_y)
    turns += 1
