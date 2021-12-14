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

for _ in range(10):
    new_polymer = ""
    for i in range(len(polymer)-1):
        a = polymer[i]
        b = polymer[i+1]

        new_polymer += a
        if (a,b) in transforations:
            new_polymer += transforations[(a,b)]

    new_polymer += polymer[-1]
    polymer = new_polymer

letter_counter = defaultdict(int)

for letter in polymer:
    letter_counter[letter] += 1

frequency = list(letter_counter.values())
frequency.sort()

result = frequency[-1] - frequency[0]

print(result)
