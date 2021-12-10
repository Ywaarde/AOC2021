f = open('input.txt', 'r').read().splitlines()

ef = open('example.txt', 'r').read().splitlines()


def build_matrix(input):

    my_matrix = [([0]*len(input[0])) for i in range(len(input))]

    for i in range(len(input)):
        for j in range(len(input[0])):
            my_matrix[i][j] = int(input[i][j])
    return my_matrix


def low_points(data):
    input = build_matrix(data)
    low_points = []

    max_xc = len(input[0]) - 1
    max_yc = len(input) - 1

    for i in range(len(input)):
        for j in range(len(input[0])):
            candidate = [input[i][j], 0, (i,j)]

            #pad edges
            if i in [0, max_yc]: 
                candidate[1] += 1
            if j in [0, max_xc]:
                candidate[1] += 1

            if i > 0 and input[i-1][j] > candidate[0]:
                candidate[1] += 1
            if j < max_xc and input[i][j+1] > candidate[0]:
                candidate[1] += 1
            if i < max_yc and input[i+1][j] > candidate[0]:
                candidate[1] += 1
            if j > 0 and input[i][j-1] > candidate[0]:
                candidate[1] += 1

            if candidate[1] == 4:
                low_points.append(candidate)

    return low_points


def not_in_basin(candidate, basins):
    for b in basins:
        if candidate in b:
            return False
    return True

def in_basin(candidate, basins):
    for b in basins:
        if candidate in b:
            return True
    return False

def is_neighbor(a, b):
    if not (a[0] == b[0] or a[1] == b[1]):
        return False

    if a[0] == b[0]:
        if (a[1] - 1) == b[1] or (a[1] + 1) == b[1]:
            return True
    if a[1] == b[1]:
        if (a[0] - 1) == b[0] or (a[0] + 1) == b[0]:
            return True
    return False

def put_in_basin(candidate, basins):
    basin_found = False

    for b in basins:
        this_basin = False
        for elem in b:
            if is_neighbor(elem, candidate):
                this_basin = True
                basin_found = True
                break
        if this_basin:
            b.append(candidate)

    if not basin_found:
        basins.append([candidate])
    
    return basins

def merge_overlap(basins):
    new_basins = []

    for b1 in basins:
        new_b = b1
        for b2 in basins:
            if not set(b1).isdisjoint(b2):
                new_b += b2
        new_b = set(new_b)
        if new_b not in new_basins:
            new_basins.append(new_b)

    return new_basins


def basins_bf(data): #idiot dit not read the assignment
    input = build_matrix(data)
    basins = []
    in_basin = []

    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] != 9:
                in_basin.append((i,j))
    
    for i in in_basin:
        basins = put_in_basin(i, basins)
    
    basins = merge_overlap(basins)

    b_length = [ len(b) for b in basins ]
    
    b_length = sorted(b_length)

    return b_length[-1]*b_length[-2]*b_length[-3]

def get_neighbors(a, area):
    neighbors = []
    try:
        if a[0] > 0 and area[(a[0]-1)][a[1]] != 9:
            neighbors.append([(a[0]-1), a[1]])
        if a[1] > 0 and area[a[0]][(a[1]-1)] != 9:
            neighbors.append([a[0], (a[1]-1)])
        
        if a[0] < len(area)-1 and area[a[0]+1][a[1]] != 9:
            neighbors.append([a[0]+1, a[1]])
        if a[1] < len(area[0])-1 and area[a[0]][a[1]+1] != 9:
            neighbors.append([a[0], a[1]+1])
    except:
        print(a)
        raise
    
    return neighbors
    

def scour_basin(seed, area):
    basin = []
    neighbors = get_neighbors(seed, area)

    while neighbors:
        new_neighbors = []
        for i in neighbors:
            if i not in basin:
                basin.append(i)
                new_neighbors += get_neighbors(i, area)
        neighbors = new_neighbors

    return basin


def find_basins(low_points, data):
    input = build_matrix(data)
    basins = []
    for lp in low_points:
        
        basins.append(scour_basin(lp[2], input))

    b_length = [ len(b) for b in basins ]
    
    b_length = sorted(b_length)

    return b_length[-1]*b_length[-2]*b_length[-3]


print('Example answer 1:')
low_points_ex = low_points(ef)
print(sum([d[0]+1 for d in low_points_ex]))
print('Example answer 2')
# print(basins_bf(ef))
print(find_basins(low_points_ex, ef))

print('Answer 1:')
low_points_r = low_points(f)
print(sum([d[0]+1 for d in low_points_r]))
print('Answer 2:')
print(find_basins(low_points_r, f))

