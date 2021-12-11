f = open('input.txt', 'r').read().splitlines()

ef = open('example.txt', 'r').read().splitlines()

def check_match(a, b):
    if a == '(' and b == ')':
        return True
    if a == '[' and b == ']':
        return True
    if a == '{' and b == '}':
        return True
    if a == '<' and b == '>':
        return True
    return False


def corruption_score(corrupted):
    score = 0
    for i in corrupted:
        if i == ')':
            score += 3
        elif i == ']':
            score += 57
        elif i == '}':
            score += 1197
        elif i == '>':
            score += 25137

    return score


def check_corrupted_lines(input):

    corrupted = []
    incomplete = []
    for line in input:
        stack = []
        corr = False
        for i in line:
            if i in ['(', '[', '{', '<']:
                stack.append(i)
            if i in [')', ']', '}', '>']:
                if not check_match(stack.pop(), i):
                    corrupted.append(i)
                    corr = True
                    break
        if not corr:
            incomplete.append(line)
    
    return [corrupted, incomplete]


def select_fix(a):
    if a == '(':
        return ')'
    if a == '[':
        return ']'
    if a == '{':
        return '}'
    if a == '<':
        return '>'


def incomplete_score(complement):
    score = []

    for line in complement:
        line_score = 0
        for i in line:
            line_score *= 5
            if i == ')':
                line_score += 1
            elif i == ']':
                line_score += 2
            elif i == '}':
                line_score += 3
            elif i == '>':
                line_score += 4
        score.append(line_score)
    
    score = sorted(score)

    index = int(len(score)/2)

    return score[index]


def fix_incomplete_lines(incomplete_lines):
    total_fixes = []

    for line in incomplete_lines:
        this_fix = []
        stack = []
        for i in line:
            if i in ['(', '[', '{', '<']:
                stack.append(i)
            if i in [')', ']', '}', '>']:
                stack.pop()
            
        for i in stack[::-1]:
            this_fix.append(select_fix(i))

        total_fixes.append(this_fix)

    return incomplete_score(total_fixes)


print('Example answer 1')
lines = check_corrupted_lines(ef)
print(corruption_score(lines[0]))
print('Example answer 2')
print(fix_incomplete_lines(lines[1]))

print('Answer 1')
lines2 = check_corrupted_lines(f)
print(corruption_score(lines2[0]))
print('Answer 2')
print(fix_incomplete_lines(lines2[1]))
