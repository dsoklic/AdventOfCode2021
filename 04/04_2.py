def get_winning_boards(input_boards):
    winners = []
    # check all horizontals
    for board_n in range(len(boards)):
        for y in range(5):
            if all([x == "x" for x in boards[board_n][y]]):
                winners.append(board_n)
    
    # check all verticals
    for board_n in range(len(boards)):
        for x in range(5):
            column = [line[x] for line in boards[board_n]]
            if all([x == "x" for x in column]):
                winners.append(board_n)

    return list(set(winners))

with open('input04.txt', 'r') as f:
   input = [x.strip() for x in f.readlines()]

drawn_numbers = input[0].split(',')

boards = []
for starting_line in range(2, len(input), 6):
    boards.append([x.split() for x in input[starting_line:starting_line+5]])

for number in drawn_numbers:

    for board_n in range(len(boards)):
        for y in range(5):
            for x in range(5):
                if boards[board_n][y][x] == number:
                    boards[board_n][y][x] = "x"

    # check if line
    winners = get_winning_boards(boards)
    winners.sort(reverse=True)

    if winners:
        for winner in winners:
            last_removed_board = boards[winner]
            del boards[winner]

        last_number = int(number)

    
    if not boards:
        break

# calculate result
winning_board = last_removed_board
sum_remaining = 0
for line in winning_board:
    sum_remaining += sum([int(n) for n in line if n != "x"])

print(sum_remaining * last_number)
