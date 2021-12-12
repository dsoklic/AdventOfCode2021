from queue import SimpleQueue

# input = ["5483143223","2745854711","5264556173","6141336146","6357385478","4167524645","2176841721","6882881134","4846848554","5283751526"]

with open('input11.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]
input = [list(map(int,i)) for i in [list(x) for x in input]]

def legal(x, y):
    global input
    return x > -1 and x < len(input[0]) and y > -1 and y < len(input)

def increase(flashed, x, y):
    global input
    if legal(x, y):
        input[y][x] += 1

        if input[y][x] == 10:
            flashed.append((x,y))

def increase_surounding(x, y):
    global input

    flashed = []

    increase(flashed, x-1, y-1)
    increase(flashed, x-1, y)
    increase(flashed, x-1, y+1)
    increase(flashed, x, y-1)
    increase(flashed, x, y)
    increase(flashed, x, y+1)
    increase(flashed, x+1, y-1)
    increase(flashed, x+1, y)
    increase(flashed, x+1, y+1)

    return flashed

flashes = 0
for _ in range(100):
    to_flash = SimpleQueue()

    for y in range(len(input)):
        for x in range(len(input[0])):
            input[y][x] += 1

            if input[y][x] > 9:
                to_flash.put((x,y))

    # simulate all flashes
    while not to_flash.empty():
        x, y = to_flash.get()
        new_flash = increase_surounding(x,y)
        [to_flash.put(fl) for fl in new_flash]

    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] > 9:
                input[y][x] = 0
                flashes += 1

print(flashes)
