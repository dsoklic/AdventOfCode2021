# input = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

with open('input03.txt', 'r') as f:
   input = [x.strip() for x in f.readlines()]

# oxygen
remaining_num = input
for i in range(len(input[0])):
    column = [x[i] for x in remaining_num]

    zeros = sum([x == '0' for x in column])
    ones = sum([x == '1' for x in column])

    if ones >= zeros:
        remaining_num = [x for x in remaining_num if x[i] == "1"]
    else:
        remaining_num = [x for x in remaining_num if x[i] == "0"]

    if len(remaining_num) == 1:
        oxygen = remaining_num[0]
        break

# co2
remaining_num = input
for i in range(len(input[0])):
    column = [x[i] for x in remaining_num]

    zeros = sum([x == '0' for x in column])
    ones = sum([x == '1' for x in column])

    if zeros <= ones:
        remaining_num = [x for x in remaining_num if x[i] == "0"]
    else:
        remaining_num = [x for x in remaining_num if x[i] == "1"]

    if len(remaining_num) == 1:
        co2 = remaining_num[0]
        break

print(int(oxygen,2) * int(co2,2))