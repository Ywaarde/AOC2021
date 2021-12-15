f = open('input.txt', 'r').read().splitlines()

ef = open('example.txt', 'r').read().splitlines()

def process_input(input):
    folds = []
    checks = []
    max_x, max_y = 0, 0
    for line in input:
        if line:
            if line[0] == 'f':
                folds.append(line.split(' ')[-1].split('='))
            else:
                checks.append([int(c) for c in line.split(',')])
                if checks[-1][0] > max_y:
                    max_y = checks[-1][0]
                if checks[-1][1] > max_x:
                    max_x = checks[-1][1]
    max_x += 1
    max_y += 1
    
    matrix = [([' ']*(max_y)) for _ in range(max_x)]
    for coord in checks:
        matrix[coord[-1]][coord[0]] = '#'

    return matrix, folds

def fold_y(matrix, line):
    foldover = len(matrix) - line - 1
    first_line = line - foldover

    for i in range(first_line, line):
        opposing_row = (2 * (foldover + first_line)) - (i)
        for j in range(len(matrix[0])):
            if matrix[i][j] == ' ':
                matrix[i][j] = matrix[opposing_row][j]

    return matrix[:line]

def fold_x(matrix, line):
    new_matrix = []
    foldover = len(matrix[0]) - line - 1
    first_point = line - foldover

    for i in range(len(matrix)):
        for j in range(first_point, line):
            opposing_point = (2 * (foldover + first_point)) - (j)
            if matrix[i][j] == ' ':
                matrix[i][j] = matrix[i][opposing_point]
        new_matrix.append(matrix[i][:line])
    
    return new_matrix


def fold_it(input, all):
    matrix, folds = process_input(input)

    if all:
        last_fold = len(folds)
    else:
        last_fold = 1

    for fold in folds[:last_fold]:
        if fold[0] == 'y':
            matrix = fold_y(matrix, int(fold[1]))
            
        if fold[0] == 'x':
            matrix = fold_x(matrix, int(fold[1]))
        
    count = 0
    for row in matrix:
        if last_fold > 1:
            print(''.join(row))
        for ch in row:
            if ch == '#':
                count += 1

    return count

print('Example 1:')
print(fold_it(ef, False))
print('Example 2:')
print(fold_it(ef, True))

print('Answer 1:')
print(fold_it(f, False))
print('Answer 2:')
print(fold_it(f, True))