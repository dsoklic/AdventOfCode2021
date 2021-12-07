import sys

# input = [16,1,2,0,4,2,7,1,2,14]
with open('input07.txt', 'r') as f:
   input = [int(x) for x in f.readline().split(',')]

min_cost = sys.maxsize
for i in range(max(input)):
    # caclulate distnaces to point i
    cost = sum([abs(i-x) for x in input])
    if cost < min_cost:
        min_cost = cost

print(min_cost)
