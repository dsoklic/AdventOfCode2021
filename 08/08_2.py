from typing import List


def issubset(a, b):
    if type(a) is str:
        a = set(a)

    if type(b) is str:
        b = set(b)

    return a.issubset(b)

def get_number_mappings(combinations: List[str]):
    segments = [{'a','b','c','d','e','f','g'}]*10

    segments[1] = next(v for i,v in enumerate(combinations) if len(v) == 2)
    segments[4] = next(v for i,v in enumerate(combinations) if len(v) == 4)
    segments[7] = next(v for i,v in enumerate(combinations) if len(v) == 3)

    segments[3] = next(v for i,v in enumerate(combinations) if len(v) == 5 and issubset(segments[7], v))

    segments[9] = next(v for i,v in enumerate(combinations) if len(v) == 6 and issubset(segments[3], v))
    segments[0] = next(v for i,v in enumerate(combinations) if len(v) == 6 and issubset(segments[7], v) and v != segments[9])
    segments[6] = next(v for i,v in enumerate(combinations) if len(v) == 6 and v != segments[9] and v != segments[0])

    segments[5] = next(v for i,v in enumerate(combinations) if len(v) == 5 and issubset(v, segments[6]))
    segments[2] = next(v for i,v in enumerate(combinations) if len(v) == 5 and v != segments[3] and v != segments[5])

    return [set(x) for x in segments]

with open('input08.txt', 'r') as f:
    input = [x.strip().split(' | ') for x in f.readlines()]

# input = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf".split(' | ')]

groups = [(a.split(),b.split()) for (a,b) in input]

result = 0
for pattern, output in groups:
    mappings = get_number_mappings(pattern)
    result += int(''.join([str(mappings.index(set(digit))) for digit in output]))
        

print(result)




# print(result)