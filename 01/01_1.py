increases = 0

with open('input01.txt', 'r') as f:
    line = int(f.readline().strip())

    next_line = f.readline()
    while next_line:
        next_line = int(next_line.strip())

        if next_line > line:
            increases += 1

        line = next_line
        next_line = f.readline()

print(increases)