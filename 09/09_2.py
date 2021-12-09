# input = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678\n"
# heightmap = input.split()

with open('input09.txt', 'r') as f:
    heightmap = [x.strip() for x in f.readlines()]

def get_neightbours(heightmap, x, y):
    neighbours = []

    if y > 0:
        neighbours.append((x, y-1, int(heightmap[y-1][x])))
    if y < len(heightmap)-1:
        neighbours.append((x, y+1, int(heightmap[y+1][x])))
    if x > 0:
        neighbours.append((x-1, y, int(heightmap[y][x-1])))
    if x < len(heightmap[0])-1:
        neighbours.append((x+1, y, int(heightmap[y][x+1])))
    
    return neighbours

def get_baisin(heightmap, starting_point):
    baisin = [starting_point]

    to_explore = [starting_point]
    while to_explore:
        exploring_x, exploring_y, exploring_val = to_explore.pop()
        neightbours = get_neightbours(heightmap, exploring_x, exploring_y)

        new_nodes = [node for node in neightbours if node[2] >= exploring_val and node[2] < 9 and node not in baisin]
        baisin += new_nodes
        to_explore += new_nodes
    
    return baisin


local_minimums = []

for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        neighbours = get_neightbours(heightmap, x, y)
        min_neigbours_height = min([foo[2] for foo in neighbours])
        if int(heightmap[y][x]) < min_neigbours_height:
            local_minimums.append((x,y,int(heightmap[y][x])))

baisins = [get_baisin(heightmap, minimum_point) for minimum_point in local_minimums]
baisins.sort(key=lambda x: len(x), reverse=True)

result = len(baisins[0]) * len(baisins[1]) * len(baisins[2])

print(result)