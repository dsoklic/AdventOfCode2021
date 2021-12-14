from collections import defaultdict

transforations = {}

with open('input14.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()

        if '->' in line:
            pair, addition = line.split(' -> ')
            transforations[tuple(pair)] = addition
        elif line:
            polymer = line

polymer_pairs = defaultdict(int)
starting_char = polymer[0]

for i in range(len(polymer)-1):
    a = polymer[i]
    b = polymer[i+1]
    polymer_pairs[(a,b)] += 1

for _ in range(40):
        new_polymer_pairs = defaultdict(int)
        for pair, count in polymer_pairs.items():
            if pair in transforations:
                added_char = transforations[pair]
                new_polymer_pairs[(pair[0],added_char)] += count
                new_polymer_pairs[(added_char,pair[1])] += count
            else:
                new_polymer_pairs[pair] += count
        
        polymer_pairs = new_polymer_pairs


# count
letter_counter = defaultdict(int)
letter_counter[starting_char] = 1
for pair, count in polymer_pairs.items():
    letter_counter[pair[1]] += count


frequency = list(letter_counter.values())
frequency.sort()

result = frequency[-1] - frequency[0]

print(result)
