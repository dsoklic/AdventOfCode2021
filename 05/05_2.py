with open('input05.txt', 'r') as f:
   input = [x.strip() for x in f.readlines()]

board = {}

for line in input:
    start, end = line.split(' -> ')
    s_x, s_y = [int(i) for i in start.split(',')]
    e_x, e_y = [int(i) for i in end.split(',')]

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
                if (x, y) in board:
                    board[(x, y)] += 1
                else:
                    board[(x, y)] = 1
    else:
        for x,y in zip(x_range, y_range):
            if (x, y) in board:
                board[(x, y)] += 1
            else:
                board[(x, y)] = 1  

num_intersect = sum([intersects >= 2 for intersects in board.values()])

print(num_intersect)
