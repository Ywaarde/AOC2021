f = open('input.txt', 'r').readlines()

ef = open('example.txt', 'r').readlines()

def count_special_digits(input):
    digits = []
    for line in input:
        io = line.split('|')
        digits += io[1].split()
    
    no1748 = [d for d in digits if len(d) in [2, 3, 4, 7]] #python!
    
    return len(no1748)

def count_sums(input):
    result = 0
    for line in input:
        io = line.split('|')
        signal = io[0].split()
        digits = io[1].split()
   
        key = [0] * 10

        for s in signal:
            if len(s) == 2:
                key[1] = set(s)
            if len(s) == 3:
                key[7] = set(s)
            if len(s) == 4:
                key[4] = set(s)
            if len(s) == 7:
                key[8] = set(s)
        
        for s in signal:
            if len(s) == 6:
                if key[4].issubset(s):
                    key[9] = set(s)
                elif key[7].issubset(s):
                    key[0] = set(s)
                else:
                    key[6] = set(s)
        
        for s in signal:
            if len(s) == 5:
                if key[1].issubset(s):
                    key[3] = set(s)
                elif set(s)-key[6]:
                    key[2] = set(s)
                else:
                    key[5] = set(s)
        
        number = ''
        for d in digits:
            for i in range(10):
                if set(d) == key[i]:
                    number += str(i)
        
        result += int(number)
    
    return result

print('Example answer 1:')
print(count_special_digits(ef))
print('Example answer 2')
print(count_sums(ef))

print('Answer 1:')
print(count_special_digits(f))
print('Answer 2:')
print(count_sums(f))





    