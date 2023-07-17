from random import randint

HEIGHT = 5
WIDTH = 5

char_x = randint(0, WIDTH - 1)
char_y = randint(0, HEIGHT - 1)
char_sign = 'X'

exit_x = randint(0, WIDTH - 1)
exit_y = randint(0, HEIGHT - 1)

row = ' |'
world_map = ''

for j in range(HEIGHT):
    pass
for i in range(WIDTH):
    row += ' |'
world_map += f'{row}\n'
print(world_map)
