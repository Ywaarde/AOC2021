f = open('input.txt', 'r').read().splitlines()

ef = open('example.txt', 'r').read().splitlines()

def build_legend(input):
    result = {}

    for line in input:
        s_s = line.split('-')
        if result.get(s_s[0]):
            result[s_s[0]].append(s_s[1])
        else:
            result[s_s[0]] = [s_s[1]]
        
        if result.get(s_s[1]):
            result[s_s[1]].append(s_s[0])
        else:
            result[s_s[1]] = [s_s[0]]
    
    return result

def all_paths(input):
    legend = build_legend(input)

    def find_paths(path, options):
        if path[-1] == 'end' or len(options) == 0:
            return [path]
        
        result = []
        for o in options:
            try:
                if o not in path or o.lower() != o:
                    if legend.get(o):
                        option_o = [i for i in legend[o] if i not in path or i.lower() != i]
                    else:
                        option_o = []
                    next_path = path + [o]
                    result += find_paths(next_path, option_o)
            except:
                print(path, o, o.lower())
                raise
        return result  

    all_paths = find_paths(['start'], legend['start'])
    
    result = 0
    for p in all_paths:
        if p[-1] == 'end':
            result += 1
    
    return result

def all_paths_extra(input):
    legend = build_legend(input)

    def double_small(path):
        counter = []
        for cave in path:
            if cave.lower() == cave:
                if cave in counter:
                    return True
                else:
                    counter.append(cave)
        return False

    def find_paths(path, options):
        if path[-1] == 'end' or len(options) == 0:
            return [path]
        
        def is_valid_option(path, o):
            return o != 'start' and (o.lower() != o or o not in path or (path.count(o) < 2 and not double_small(path)))
        
        result = []
        for o in options:
            try:
                if is_valid_option(path, o):
                    if legend.get(o):
                        option_o = [i for i in legend[o] if is_valid_option(path, i)]
                    else:
                        option_o = []
                    next_path = path + [o]
                    result += find_paths(next_path, option_o)
            except:
                print(path, o, o.lower())
                raise
        e2e = []
        for p in result:
            if p[-1] == 'end':
                e2e.append(p)
    
        return e2e  

    all_paths = find_paths(['start'], legend['start'])
    
    return len(all_paths)


print('Example 1:')
print(all_paths(ef))
print('Example 2:')
print(all_paths_extra(ef))

print('Answer 1:')
print(all_paths(f))
print('Answer 2:')
print(all_paths_extra(f))