# input = "[({(<(())[]>[[{[]{<()<>>\n[(()[<>])]({[<{<<[]>>(\n{([(<{}[<>[]}>{[]{[(<()>\n(((({<>}<{<{<>}{[]{[]{}\n[[<[([]))<([[{}[[()]]]\n[{[{({}]{}}([{[{{{}}([]\n{<[[]]>}<{[{[{[]{()[[[]\n[<(<(<(<{}))><([]([]()\n<{([([[(<>()){}]>(<<{{\n<{([{{}}[<[[[<>{}]]]>[]]"
# input = input.split()

with open('input10.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

bracket_pairs = {'}':'{', ']':'[', ')': '(', '>': '<'}
scoring = {')': 1, ']': 2, '}': 3, '>': 4}

def is_opener(char):
    return char in ('(', '[', '{', '<')

def calculate_line_score(line):
    last_opening_bracket = [line[0]]
    for char in line[1:]:
        if is_opener(char):
            last_opening_bracket.append(char)
        elif last_opening_bracket[-1] != bracket_pairs[char]:
            # syntax error
            return 0
        else:
            last_opening_bracket.pop()

    score = 0
    # Calculate score from remaining 
    for char in reversed(last_opening_bracket):
        closing_char = next(k for k,v in bracket_pairs.items() if v == char)
        score *= 5
        score += scoring[closing_char]

    return score

scores = [calculate_line_score(line) for line in input]
scores = list(filter(lambda x: x > 0, scores))
scores.sort()

print(scores[int(len(scores)/2)])
