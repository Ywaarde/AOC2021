f = open('input.txt', 'r').read()

ef = open('example.txt', 'r').read()

def crossing(data, diagonals=False):
    input = data.splitlines()

    output = []
    high_x, high_y = 1000, 1000
    for line in input:
        el = [l.split(',') for l in line.split(' -> ')]

        x1, x2 = int(el[0][0]), int(el[1][0])
        y1, y2 = int(el[0][1]), int(el[1][1])

        if ((y1 == y2) or (x1 == x2)):

            start_x = x1 if x1 < x2 else x2
            end_x = x2 if x2 > x1 else x1
            start_y = y1 if y1 < y2 else y2
            end_y = y2 if y2 > y1 else y1

            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    output.append((i,j))
        elif diagonals:
            for i in range(abs(x1 - x2)+ 1):
                if x1 < x2:
                    if y1 < y2:
                        output.append((x1 + i, y1 + i))
                    else:
                        output.append((x1 + i, y1 - i))
                else:
                    if y1 < y2:
                        output.append((x1 - i, y1 + i))
                    else:
                        output.append((x1 - i, y1 - i))

    my_matrix = [([0]*high_x) for i in range(high_y)]

    for point in output:
        my_matrix[point[0]][point[-1]] += 1
    
    result = 0

    for i in range(high_x):
        for j in range(high_y):
            if my_matrix[i][j] > 1:
                result += 1

    return result

print('Example answer 1:')
print(crossing(ef))
print('Example answer 2')
print(crossing(ef, True))

print('Answer 1:')
print(crossing(f))
print('Answer 2')
print(crossing(f, True))
    