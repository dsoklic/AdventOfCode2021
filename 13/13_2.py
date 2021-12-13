dots = set()
folds = []

with open('input13.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()

        if ',' in line:
            pair = [int(x) for x in line.split(',')]
            dots.add(tuple(pair))
        
        if '=' in line:
            left,position = line.split('=')
            direction = left[-1]
            folds.append((direction,int(position)))

for fold_direction, fold_position in folds:
    if fold_direction == 'y': # horizontal
        for dot in [dot for dot in dots if dot[1] > fold_position]:
            dots.remove(dot)
            x,y = dot
            y = 2*fold_position - y
            dots.add((x,y))
    elif fold_direction == 'x': # vertical
        for dot in [dot for dot in dots if dot[0] > fold_position]:
            dots.remove(dot)
            x,y = dot
            x = 2*fold_position - x
            dots.add((x,y))

max_x = max(x[0] for x in dots)
max_y = max(x[1] for x in dots)

for y in range(max_y+1):
    for x in range(max_x+1):
        if (x,y) in dots:
            print('#',end='')
        else:
            print(' ',end='')
    print()