from queue import PriorityQueue

input = []
with open('input15.txt', 'r') as f:
    for line in f.readlines():
        input.append([int(x) for x in line.strip()])

# prepare input
def inc(val):
    if val == 9:
        return 1
    else:
        return val+1

# copy horizontally
for i in range(len(input)):
    line = input[i]
    new_line = [line]
    for _ in range(4):
        new_line.append(list(map(inc, new_line[-1])))
    
    input[i] = [item for sublist in new_line for item in sublist]

# copy vertically
num_lines = len(input)
for _ in range(4):
    last_n_lines = input[-num_lines:]
    for line in last_n_lines:
        input.append(list(map(inc, line)))


coordinate_queue = PriorityQueue()

coordinate_queue.put((0, (0,0)))
visited = set()

while not coordinate_queue.empty():
    cost, coordinates = coordinate_queue.get()

    if coordinates in visited:
        continue

    visited.add(coordinates)

    x,y = coordinates

    if y == len(input)-1 and x == len(input[0])-1:
        print(cost)
        break

    if x < len(input[0])-1:
        next_cost = int(input[y][x+1]) + cost
        coordinate_queue.put((next_cost, (x+1,y)))
        
    if y < len(input)-1:
        next_cost = int(input[y+1][x]) + cost
        coordinate_queue.put((next_cost, (x,y+1)))

    if x > 0:
        next_cost = int(input[y][x-1]) + cost
        coordinate_queue.put((next_cost, (x-1,y)))

    if y > 0:
        next_cost = int(input[y-1][x]) + cost
        coordinate_queue.put((next_cost, (x,y-1)))
        