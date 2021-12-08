def is_unique_segment_digit(inp):
    length = len(inp)
    return length == 2 or length == 4 or length == 3 or length == 7

with open('input08.txt', 'r') as f:
    input = [x.strip().split(' | ') for x in f.readlines()]

groups = [b.split() for (a,b) in input]
flat_list = [item for sublist in groups for item in sublist]

result = sum([is_unique_segment_digit(x) for x in flat_list])

print(result)