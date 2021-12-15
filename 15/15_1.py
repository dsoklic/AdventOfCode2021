from queue import PriorityQueue

with open('input15.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

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
        