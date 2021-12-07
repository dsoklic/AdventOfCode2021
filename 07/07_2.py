import sys

# input = [16,1,2,0,4,2,7,1,2,14]
with open('input07.txt', 'r') as f:
   input = [int(x) for x in f.readline().split(',')]

def cost(a, b):
    distance = abs(a-b)
    return (distance/2.0)*(distance+1)

min_cost = sys.maxsize
for i in range(max(input)):
    # caclulate distnaces to point i

    i_cost = sum([cost(i, x) for x in input])
    if i_cost < min_cost:
        min_cost = i_cost

print(int(min_cost))
