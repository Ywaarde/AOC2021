f = open('input.txt', 'r').read().splitlines()

ef = open('example.txt', 'r').read().splitlines()


def build_matrix(input):

    my_matrix = [([0]*len(input[0])) for i in range(len(input))]

    for i in range(len(input)):
        for j in range(len(input[0])):
            my_matrix[i][j] = int(input[i][j])
    return my_matrix


def get_neighbors(a, area):
    neighbors = []
    try:
        if a[0] > 0:
            neighbors.append((a[0]-1, a[1]))
            if a[1] > 0:
                neighbors.append((a[0]-1, a[1]-1))
        if a[1] > 0:
            neighbors.append((a[0], a[1]-1))

        if a[0] < len(area)-1:
            neighbors.append((a[0]+1, a[1]))
            if a[1] < len(area[0])-1:
                neighbors.append((a[0]+1, a[1]+1))
        if a[1] < len(area[0])-1:
            neighbors.append((a[0], a[1]+1))

        if a[0] > 0 and a[1] < len(area[0])-1:
            neighbors.append((a[0]-1, a[1]+1))

        if a[1] > 0 and a[0] < len(area)-1:
            neighbors.append((a[0]+1, a[1]-1))

    except:
        print(a)
        raise

    return neighbors


def count_flashes(data, cycles):
    input = build_matrix(data)
    flashes = 0

    for _ in range(cycles):
        will_flash = []
        for i in range(len(input)):
            for j in range(len(input[0])):
                input[i][j] += 1
                if input[i][j] == 10:
                    flashes += 1
                    will_flash.append((i, j))

        while will_flash:
            for o in will_flash:
                will_flash.remove(o)
                neighbors = get_neighbors(o, input)
                for n in neighbors:
                    input[n[0]][n[1]] += 1
                    if input[n[0]][n[1]] == 10:
                        flashes += 1
                        will_flash.append(n)
        
        for i in range(len(input)):
            for j in range(len(input[0])):
                if input[i][j] > 9:
                    input[i][j] = 0

    return flashes

def all_flash(data):
    input = build_matrix(data)
    # flashes = 0
    cycle = 0

    while True:
        flashes = 0
        cycle += 1
        will_flash = []
        for i in range(len(input)):
            for j in range(len(input[0])):
                input[i][j] += 1
                if input[i][j] == 10:
                    flashes += 1
                    will_flash.append((i, j))

        while will_flash:
            for o in will_flash:
                will_flash.remove(o)
                neighbors = get_neighbors(o, input)
                for n in neighbors:
                    input[n[0]][n[1]] += 1
                    if input[n[0]][n[1]] == 10:
                        flashes += 1
                        will_flash.append(n)
        
        for i in range(len(input)):
            for j in range(len(input[0])):
                if input[i][j] > 9:
                    input[i][j] = 0
        if flashes == 100:
            break

    return cycle


print('Example answer 1:')
print(count_flashes(ef, 100))
print('Example answer 2:')
print(all_flash(ef))
print('Answer 1:')
print(count_flashes(f, 100))
print('Example answer 2:')
print(all_flash(f))
