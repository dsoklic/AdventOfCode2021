# input = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

with open('input03.txt', 'r') as f:
   input = [x.strip() for x in f.readlines()]

gamma = []
epsilon = []

for i in range(len(input[0])):
    column = [x[i] for x in input]

    zeros = sum([x == '0' for x in column])
    ones = sum([x == '1' for x in column])

    if ones > zeros:
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')

gamma = int(''.join(gamma),2)
epsilon = int(''.join(epsilon),2)

print(gamma * epsilon)