data = open('input.txt', 'r').read().splitlines()

def task_1(diagnostics):
    most_common = [0] * len(diagnostics[0])

    for d in diagnostics:
        for bit in range(len(d)):
            if d[bit] == '1':
                most_common[bit] += 1
    
    gamma = ''
    epsilon = ''

    for bit in most_common:
        if bit >= len(diagnostics)/2:
            gamma += str(1)
            epsilon += str(0)
        else:
            gamma += str(0)
            epsilon += str(1)

    return (gamma, epsilon)

def task_2(diagnostics):
    
    input = diagnostics
    index = 0
    while len(input) > 1:    
        common_bit = task_1(input)[0]
        new_input = []
        for m in range(len(input)):
            if input[m][index] == common_bit[index]:
                new_input.append(input[m])
        input = new_input
        index += 1
    
    oxygen = input[0]

    input = diagnostics
    index = 0
    while len(input) > 1:
        common_1 = task_1(input)[1]
        new_input = []
        for m in range(len(input)):
            if input[m][index] == common_1[index]:
                new_input.append(input[m])
        input = new_input
        index += 1
    
    co2 = input[0]
    return (oxygen, co2)

def print_day_3(a, number):
    print("Answer task " + number)
    print(int(a[0], 2)* int(a[1], 2))

print_day_3(task_1(data), "1")
print_day_3(task_2(data), "2")
