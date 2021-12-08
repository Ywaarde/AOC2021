f = open('input.txt', 'r').read()

movements = f.splitlines()

for m in range(len(movements)):
    movements[m] = movements[m].split()
    movements[m][1] = int(movements[m][1])

hor = 0
depth = 0

for move in movements:
    if move[0] == 'forward':
        hor += move[1]
    if move[0] == 'down':
        depth += move[1]
    if move[0] == 'up':
        depth -= move[1]

print('first task')
print(hor*depth)

hor = 0
depth = 0
aim = 0
for move in movements:
    if move[0] == 'down':
        aim += move[1]
    if move[0] == 'up':
        aim -= move[1]
    if move[0] == 'forward':
        hor += move[1]
        depth += aim * move[1]

print('second task')
print(hor*depth)