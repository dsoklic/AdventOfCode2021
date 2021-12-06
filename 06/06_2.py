import re
from collections import defaultdict

# input = [3,4,3,1,2]

with open('input06.txt', 'r') as f:
   input = [int(x) for x in re.findall(r'\d+', f.readline())]

days = 256

fish_pool = defaultdict(int)
for fish in input:
    fish_pool[fish] += 1

for day in range(days):
    fish_pool = {key-1:val for key,val in fish_pool.items()}
    fish_pool = defaultdict(int, fish_pool)

    num_new_fish = fish_pool[-1]
    if -1 in fish_pool:
        del fish_pool[-1]

    fish_pool[6] += num_new_fish
    fish_pool[8] += num_new_fish

print(sum(fish_pool.values()))
