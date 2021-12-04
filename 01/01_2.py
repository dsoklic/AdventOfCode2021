increases = 0

with open('input01.txt', 'r') as f:
   lines = [int(x) for x in f.readlines()]

# lines = [199,200,208,210,200,207,240,269,260,263]

prev_sum = sum(lines[0:3])
for i in range(1, len(lines) - 2):
    next_sum = sum(lines[i:i+3])

    if next_sum > prev_sum:
        increases += 1

    prev_sum = next_sum

print(increases)