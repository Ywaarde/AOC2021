f = open('input.txt', 'r').read().split(',')

ef = open('example.txt', 'r').read().split(',')

def growth_i(data, limit):
    school = []
    for i in data:
        school.append(int(i))

    school_i = [0] * 9
    for i in school:
        school_i[i] += 1

    new = school_i
    for _ in range(limit):
        new_fish = new[0]
        new[0] = 0
        for i in range(1, 9):
            new[i -1] = new[i]
        new[6] += new_fish
        new[8] = new_fish
    
    return sum(new)
        

def growth_rec(input, day):
    if day == 80:
        return len(input)

    new = []
    for i in input:
        if i == 0:
            new.append(8)
            new.append(6)
        else:
            new.append(i-1)

    return growth_rec(new , day+1)

def growth(input, limit):

    for _ in range(limit):
        new = []
        for i in input:
            if i == 0:
                new.append(8)
                new.append(6)
            else:
                new.append(i-1)
        input = new
    
    return len(input)

print('Example answer 1:')
print(growth_i(ef, 80))
print('Example answer 2:')
print(growth_i(ef, 256))

print('Answer 1:')
print(growth_i(f, 80))
print('Answer 2:')
print(growth_i(f, 256))
