import re

input = [3,4,3,1,2]

# with open('input06.txt', 'r') as f:
#    input = [int(x) for x in re.findall(r'\d+', f.readline())]


days = 80

for day in range(days):
    for i in range(len(input)):
        input[i] -= 1

        if input[i] == -1:
            input.append(8)
            input[i] = 6

print(len(input))
