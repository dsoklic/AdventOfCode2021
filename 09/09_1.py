# input = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678\n"

with open('input09.txt', 'r') as f:
    heightmap = [x.strip() for x in f.readlines()]

def get_neightbours(heightmap, x, y):
    neighbours = []

    if y > 0:
        neighbours.append(heightmap[y-1][x])
    if y < len(heightmap)-1:
        neighbours.append(heightmap[y+1][x])
    if x > 0:
        neighbours.append(heightmap[y][x-1])
    if x < len(heightmap[0])-1:
        neighbours.append(heightmap[y][x+1])
    
    return [int(x) for x in neighbours]

risk_level = 0

for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        min_neigbours = min(get_neightbours(heightmap, x, y))
        if int(heightmap[y][x]) < min_neigbours:
            risk_level += int(heightmap[y][x]) + 1

print(risk_level)
