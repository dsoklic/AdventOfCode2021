# input = "[({(<(())[]>[[{[]{<()<>>\n[(()[<>])]({[<{<<[]>>(\n{([(<{}[<>[]}>{[]{[(<()>\n(((({<>}<{<{<>}{[]{[]{}\n[[<[([]))<([[{}[[()]]]\n[{[{({}]{}}([{[{{{}}([]\n{<[[]]>}<{[{[{[]{()[[[]\n[<(<(<(<{}))><([]([]()\n<{([([[(<>()){}]>(<<{{\n<{([{{}}[<[[[<>{}]]]>[]]"
# input = input.split()

with open('input10.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

bracket_pairs = {'}':'{', ']':'[', ')': '(', '>': '<'}

scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}

def is_opener(char):
    return char in ('(', '[', '{', '<')

total_score = 0

for line in input:
    last_opening_bracket = [line[0]]
    for char in line[1:]:
        if is_opener(char):
            last_opening_bracket.append(char)
        elif last_opening_bracket[-1] != bracket_pairs[char]:
            # syntax error
            total_score += scoring[char]
            break
        else:
            last_opening_bracket.pop()

print(total_score)
