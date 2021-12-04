# input = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]

with open('input02.txt', 'r') as f:
   input = f.readlines()

x = 0
y = 0

for cmd in input:
    split = cmd.split(' ')
    direction = split[0]
    magnitude = int(split[1])

    if direction == "forward":
        x += magnitude
    elif direction == "down":
        y += magnitude
    elif direction == "up":
        y -= magnitude

print(x * y)
