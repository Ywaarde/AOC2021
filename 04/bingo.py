f = open('input.txt', 'r').read().splitlines()

ef = open('example.txt', 'r').read().splitlines()

def build_boards(data):

    boards = []

    for row in data:
        if not row.strip():
            continue
        else:
            boards.append(row.split())

    grok = {}

    no_bords = len(boards)/5

    for i in range(int(no_bords)):
        grok[i] = []
        for j in range(5):
            grok[i].append(boards[(i*5)+j])
        for j in range(5):
            grok[i].append([boards[(i*5)+k][j] for k in range(5)])
    
    return grok


def calc_result(board, factor, drawn, boards):
    result = 0
    for row in boards[board][:5]:
        for i in row:
            if i not in drawn:
                result += int(i)
    result *= int(factor)
    return result

def first_winner(data):

    drawings = data[0].split(',')
    boards = build_boards(data[1:])

    drawn_fw = []
    winner = False
    wi = -1
    wd = []
    wx = -1
    while not winner:
        x = drawings.pop(0)
        drawn_fw.append(x)
        for key, _ in boards.items():
            for row in boards[key]:
                if set(row).issubset(drawn_fw):
                    winner = True
                    wi = key
                    wd = drawn_fw
                    wx = x
                    break
    
    return calc_result(wi, wx, wd, boards)

def last_winner(data):

    drawings = data[0].split(',')
    boards = build_boards(data[1:])

    drawn_lw = []
    no_winner = 0
    lw = -1
    ld = []
    lx = -1
    winning_boards = []

    while len(winning_boards) < len(boards):
        y = drawings.pop(0)
        drawn_lw.append(y)
        for key, _ in boards.items():
            if key not in winning_boards:
                for row in boards[key]:
                    if set(row).issubset(drawn_lw):
                        no_winner += 1
                        lw = key
                        ld = drawn_lw
                        lx = y
                        winning_boards.append(key)
                        break
 
    return calc_result(lw, lx, ld, boards)

print('Example answer 1:')
print(first_winner(ef))
print('Example answer 2')
print(last_winner(ef))

print('Answer 1:')
print(first_winner(f))
print('Answer 2')
print(last_winner(f))
