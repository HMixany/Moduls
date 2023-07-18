from random import randint

HEIGHT = 5
WIDTH = 5

char_x = randint(0, WIDTH - 1)
char_y = randint(0, HEIGHT - 1)
char_sign = '\U0001F63A'

exit_x = randint(0, WIDTH - 1)
exit_y = randint(0, HEIGHT - 1)
exit_sing = '\U0001F600'

turns = 0

while True:
    world_map = ''

    for j in range(HEIGHT):
        row = '|'
        for i in range(WIDTH):
            if char_x == i and char_y == j:
                row += char_sign + '|'
            elif exit_x == i and exit_y == j:
                row += exit_sing + '|'
            else:
                row += '  |'
        world_map += f'{row}\n'
    print(world_map)

    if char_x == exit_x and char_y == exit_y:
        print('You WIN !!!')
        break

    direction = input('Input direction (w, a, d, s): ')
    if direction == 'w' and char_y > 0:
        char_y -= 1
    elif direction == 's'and char_y < HEIGHT - 1:
        char_y += 1
    elif direction == 'a'and char_x > 0:
        char_x -= 1
    elif direction == 'd'and char_x < WIDTH - 1:
        char_x += 1
    else:
        print('Input Error')
        continue
    turns += 1
