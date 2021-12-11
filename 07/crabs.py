f = open('input.txt', 'r').read()

ef = open('example.txt', 'r').read()

def cost(n):
    return n

def sum(n):
        return (n*(n+1))//2

def crabs(data, func):
    school = []
    high = 0
    for i in data.split(','):
        if int(i) > high:
            high = int(i)
        school.append(int(i))

    school_i = [0] * (high+1)
    for i in school:
        school_i[i] += 1

    lowest_cost = 0
    position = 0
    for i in range(len(school_i)):
        cost = 0
        for j in range(len(school_i)):
            cost += school_i[j]*func(abs(j-i))
        if i == 0:
            lowest_cost = cost
            position = i
        elif cost < lowest_cost:
            lowest_cost = cost
            position = i
    
    return (position, lowest_cost)

print('Example answer 1:')
print(crabs(ef, cost))
print('Example answer 2:')
print(crabs(ef, sum))

print('Answer 1:')
print(crabs(f, cost))
print('Answer 2:')
print(crabs(f, sum))