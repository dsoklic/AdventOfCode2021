with open('input01.txt', 'r') as f:
   input = [int(x.strip()) for x in f.readlines()]

print(sum([a < b for (a,b) in [input[i:i+2] for i in range(len(input)-1)]]))
