with open('input05.txt', 'r') as f:
   input = [x.strip() for x in f.readlines()]

board = {}

for line in input:
    start, end = line.split(' -> ')
    s_x, s_y = [int(i) for i in start.split(',')]
    e_x, e_y = [int(i) for i in end.split(',')]

    s_x, e_x = min(s_x, e_x), max(s_x, e_x)
    s_y, e_y = min(s_y, e_y), max(s_y, e_y)

    # print(f'{s_x} {s_y} > {e_x} {e_y}')

    if s_x != e_x and s_y != e_y:
        continue

    for x in range(s_x, e_x+1):
        for y in range(s_y, e_y+1):
            if (x, y) in board:
                board[(x, y)] += 1
            else:
                board[(x, y)] = 1
            # print(f"board element {x},{y} is now {board[(x,y)]}")

num_intersect = sum([intersects >= 2 for intersects in board.values()])

print(num_intersect)

def visualize(board):
    for y in range(20):
        for x in range(20):
            if (x,y) in board:
                print(board[(x,y)], end='')
        print()

# visualize(board)