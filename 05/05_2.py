from collections import defaultdict
import re

with open('input05.txt', 'r') as f:
   input = [x.strip() for x in f.readlines()]

board = defaultdict(int)

for line in input:
    s_x, s_y, e_x, e_y = [int(x) for x in re.findall(r'\d+', line)]

    diagonal = s_x != e_x and s_y != e_y

    if s_x <= e_x:
        x_range = range(s_x, e_x+1)
    else:
        x_range = range(s_x, e_x-1, -1)

    if s_y <= e_y:
        y_range = range(s_y, e_y+1)
    else:
        y_range = range(s_y, e_y-1, -1)

    if not diagonal:
        for x in x_range:
            for y in y_range:
                board[(x, y)] += 1
    else:
        for x,y in zip(x_range, y_range):
            board[(x, y)] += 1

num_intersect = sum([intersects >= 2 for intersects in board.values()])

print(num_intersect)
